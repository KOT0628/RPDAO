# === СТАНДАРТНЫЕ БИБЛИОТЕКИ ===
import os
import sys
import time
import logging
import asyncio

# === СТОРОННИЕ БИБЛИОТЕКИ ===
import tweepy
import aiohttp
import discord
import requests

from discord.ext import commands

# === ЛОКАЛЬНЫЕ ИМПОРТЫ ===
from config.settings import BEARER_TOKEN, DISCORD_TOKEN, GUILD_ID
from features import register_all_commands
from features.price import update_btc_channel_name
from features.tweets import fetch_and_send_tweets
from utils import helpers
from utils import logger
from utils.scheduler import run_scheduler

# === ЗАГРУЗКА ДАННЫХ ===
# == Загрузка последней цены $BTC ==
previous_price = helpers.load_last_price()

# == Загрузка последнего твита ==
last_tweet_id = helpers.load_last_tweet_id()

# === ИНИЦИАЛИЗАЦИЯ DISCORD КЛИЕНТА ===
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True                             # если планируется обработка текста сообщений

bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree                                            # для слеш-команд

# === ИНИЦИАЛИЗАЦИЯ TWITTER КЛИЕНТА ===
twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN)  # авторизация Twitter

# === ЦИКЛЫ ЗАДАЧ ===
# == Каждая операция идёт последовательно ==
async def btc_loop():
    await bot.wait_until_ready()
    while True:
        await update_btc_channel_name(bot)                 # обновление цены BTC
        await asyncio.sleep(600)                           # обновление каждые 10 минут

async def twitter_loop():
    await bot.wait_until_ready()
    while True:
        await fetch_and_send_tweets(bot, twitter_client)   # проверка твитов
        await asyncio.sleep(600)                           # обновление каждые 10 минут

@bot.event
async def on_ready():
    logging.info(f"[MAIN] Бот вошёл как {bot.user}")
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    await update_btc_channel_name(bot)
    await fetch_and_send_tweets(bot, twitter_client)

    asyncio.create_task(btc_loop())
    asyncio.create_task(twitter_loop())

# === ЗАПУСК БОТА ===
def run_discord_bot():
    # Установка бота в модули
    register_all_commands(bot)

    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        logging.info("[MAIN] Остановлено пользователем.")
        logging.exception(
            f"[MAIN] Неожиданное исключение. Ошибка: {e}. "
            f"Перезапуск через 15 секунд..."
        )
        time.sleep(15)                                     # Ждём 15 секунд перед повтором
        os.execv(sys.executable, [sys.executable] + sys.argv)

# == Для прямого запуска ==
if __name__ == "__main__":
    run_discord_bot()
