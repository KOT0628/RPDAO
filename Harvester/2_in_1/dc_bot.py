# === СТАНДАРТНЫЕ БИБЛИОТЕКИ ===
import os
import sys
import time
import random
import logging
import asyncio

# === СТОРОННИЕ БИБЛИОТЕКИ ===
import tweepy
import aiohttp
import discord
import requests

from discord.ext import commands
from tweepy.asynchronous import AsyncClient

# === ЛОКАЛЬНЫЕ ИМПОРТЫ ===
import utils.dc_helpers as helpers

from config.settings import BEARER_TOKEN, DISCORD_TOKEN, GUILD_ID
from features import tweets
from features.game import register_games_commands
from features import register_utils_commands
from features.dc_price import update_btc_channel_name
from features.ticket_notify import on_guild_channel_create as ticket_handler
from utils import logger
from utils.scheduler import run_scheduler
from utils.tweets_guard import load_twitter_block_flag

# === ЗАГРУЗКА ДАННЫХ ===
# == Загрузка последней цены $BTC ==
previous_price = helpers.load_last_price()

# == Загрузка последнего твита ==
last_tweet_id = helpers.load_last_tweet_id()

# === ИНИЦИАЛИЗАЦИЯ DISCORD КЛИЕНТА ===
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# === ИНИЦИАЛИЗАЦИЯ TWITTER КЛИЕНТА ===
twitter_client = AsyncClient(bearer_token=BEARER_TOKEN)

# == Проверка флага блокировки Twitter ==
try:
    flag = load_twitter_block_flag()
except Exception as e:
    logging.warning(f"[DC_MAIN] Не удалось загрузить флаг блокировки Twitter: {e}")
    flag = False

tweets.set_twitter_flags(flag)
logging.info(
    f"[DC_MAIN] Стартовое состояние Twitter: {'Отключено' if flag else 'Включено'}"
)

# === ЦИКЛЫ ЗАДАЧ ===
# == Обновление цены BTC в названии канала ==
async def btc_loop():
    await bot.wait_until_ready()
    while True:
        try:
            await update_btc_channel_name(bot)
        except Exception as e:
            logging.exception(f"[DC_MAIN] Ошибка в btc_loop: {e}")
        await asyncio.sleep(600)                               # каждые 10 минут

# == Проверка и отправка новых твитов ==
async def twitter_loop(bot, twitter_client):
    logged_disabled = False
    while True:
        try:
            if not tweets.twitter_enabled:
                logging.info("[TWITTER_LOOP] Twitter отключён - пропуск итерации.")
                logged_disabled = True
            else:
                logged_disabled = False
                await tweets.fetch_and_send_tweets(bot, twitter_client)
        except Exception as e:
            logging.exception(f"[DC_MAIN] Ошибка в twitter_loop: {e}")
        await asyncio.sleep(1800 + random.randint(-120, 120))  # каждые ~30 минут

# === ИНИЦИАЛИЗАЦИЯ ===
# == Обработчик создания канала с тикетами ==
@bot.event
async def on_guild_channel_create(channel):
    await ticket_handler(channel)

# == Инициализация бота ==
@bot.event
async def on_ready():
    logging.info(f"[DC_MAIN] Бот вошёл как {bot.user}")
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))

    asyncio.create_task(btc_loop())
    asyncio.create_task(twitter_loop(bot, twitter_client))
    asyncio.create_task(tweets.check_reset_twitter_flag())

# === ЗАПУСК БОТА ===
def run_discord_bot():
    # == Установка бота в модули ==
    register_games_commands(bot)
    register_utils_commands(bot)

    try:
        bot.run(DISCORD_TOKEN)
    except KeyboardInterrupt:
        logging.info("[DC_MAIN] Бот остановлен вручную.")
        sys.exit(0)
    except Exception as e:
        logging.info("[DC_MAIN] Остановлено пользователем.")
        logging.exception(
            f"[DC_MAIN] Неожиданное исключение. Ошибка: {e}. "
            f"Перезапуск через 15 секунд..."
        )
        time.sleep(15)                                         # ждём 15 секунд
        os.execv(sys.executable, [sys.executable] + sys.argv)

# == Для прямого запуска ==
if __name__ == "__main__":
    run_discord_bot()
