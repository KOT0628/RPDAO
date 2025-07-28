import os
import logging

from dotenv import load_dotenv

# === РАБОТА С ФАЙЛАМИ ===
# == Файл логов ==
LOG_FILE = "data/logs.txt"

# == Последняя цена BTC (Discord) ==
LAST_PRICE = "data/last_price.txt"

# == Последний отправленный твит (Discord) ==
LAST_TWEET_FILE = "data/last_tweet.txt"

# == Маппинг сообщений (Discord) ==
MAP_FILE = "data/message_map.json"

# == Генерация изображений ==
BACKGROUND_PATH = "assets/backgrounds/background.jpg"
FONT_PATH = "assets/fonts/SpicyRice-Regular.ttf"
BTC_IMAGE_OUTPUT = "data/btc_price_output.jpg"

# === ЗАГРУЗКА ПЕРЕМЕННЫХ ОКРУЖЕНИЯ ===
load_dotenv()

# === ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ===
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_USER_ID = os.getenv("TWITTER_USER_ID")
TWITTER_USERNAME = "Red_Planet_Dao"                                  # имя пользователя

GUILD_ID = int(os.getenv("GUILD_ID", 0))                             # Сервер Discord
BTC_CHANNEL_ID = int(os.getenv("BTC_CHANNEL_ID", 0))                 # Канал, где меняется имя
TWITTER_CHANNEL_ID = int(os.getenv("TWITTER_CHANNEL_ID", 0))         # Канал, куда отправляются твиты

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("CHAT_ID")

# === Проверка переменных окружения ===
missing_vars = []
if not DISCORD_TOKEN: missing_vars.append("DISCORD_TOKEN")
if not BEARER_TOKEN: missing_vars.append("TWITTER_BEARER_TOKEN")
if not TWITTER_USER_ID: missing_vars.append("TWITTER_USER_ID")
if not TELEGRAM_BOT_TOKEN: missing_vars.append("TELEGRAM_TOKEN")
if not TELEGRAM_CHAT_ID: missing_vars.append("TELEGRAM_CHAT_ID")
if not GUILD_ID: missing_vars.append("GUILD_ID")
if not BTC_CHANNEL_ID: missing_vars.append("BTC_CHANNEL_ID")
if not TWITTER_CHANNEL_ID: missing_vars.append("TWITTER_CHANNEL_ID")

if missing_vars:
    raise ValueError(
        f"Не найдены переменные окружения: {', '.join(missing_vars)}"
    )
