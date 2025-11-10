import os
import logging

import deepl

from dotenv import load_dotenv

# === РАБОТА С ФАЙЛАМИ ===
# == Game Zone Images ==
BLACKJACK_IMAGE = "assets/blackjack.png"
GAME_IMAGE = "assets/game_zone.jpg"
ROLL_IMAGE = "assets/roll.jpg"
REROLL_IMAGE = "assets/reroll.jpg"
TRIVIA_IMAGE = "assets/trivia.jpg"
LEADERBOARD_IMAGE = "assets/leaderboard.jpg"

# == Оффициальные ссылки RPDAO ==
LINK_IMAGE = "assets/link.png"
WEB_URL = "https://linktr.ee/rpdao"
X_URL = "https://x.com/Red_Planet_Dao"
DC_URL = "https://discord.gg/g4b8RsbnNd"
TG_URL = "https://t.me/rpdao"
YT_URL = "https://www.youtube.com/@rpdao"
MEDIUM_URL = "https://medium.com/@redplanetdao"
INFO_URL_RU = "https://t.me/rpdao/183129"
INFO_URL_EN = "https://t.me/rpdao_news/155"

# == Файл блокировки ==
LOCK_FILE = "data/bot.lock"

# == Файлы логов ==
LOG_FILE = "data/logs/logs.log"

# == Таблица лидеров ==
SCORE_FILE = "data/leaderboard/scores.json"

# == Список вопросов TRIVIA ==
TRIVIA_FILE = "data/game/trivia_questions.txt"

# == Поддержка русских чисел на Python для TRIVIA ==
RU_NUMBERS = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14,
    "пятнадцать": 15, "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18,
    "девятнадцать": 19, "двадцать": 20, "тридцать": 30, "сорок": 40,
    "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80,
    "девяносто": 90, "сто": 100, "двести": 200, "триста": 300, "четыреста": 400,
    "пятьсот": 500, "шестьсот": 600, "семьсот": 700, "восемьсот": 800,
    "девятьсот": 900
}

# == Последняя цена BTC (Discord) ==
LAST_PRICE = "data/discord/last_price.txt"

# == Последний отправленный твит (Discord) ==
LAST_TWEET_FILE = "data/twitter/last_tweet.txt"

# == Маппинг сообщений (Discord) ==
MAP_FILE = "data/discord/message_map.json"

# == Генерация изображений ==
BACKGROUND_PATH = "assets/backgrounds/background.jpg"
FONT_PATH = "assets/fonts/SpicyRice-Regular.ttf"
BTC_IMAGE_OUTPUT = "data/img_output/btc_price_output.jpg"
GM_IMAGE_OUTPUT = "data/img_output/gm_output.jpg"
GN_IMAGE_OUTPUT = "data/img_output/gn_output.jpg"

# === ЗАГРУЗКА ПЕРЕМЕННЫХ ОКРУЖЕНИЯ ===
load_dotenv()

# === ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ===
# == Переводчики ==
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if GOOGLE_APPLICATION_CREDENTIALS:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
deepl_translator = deepl.Translator(DEEPL_API_KEY)

# == Telegram ==
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = str(os.getenv("CHAT_ID"))
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
DISCORD_AVATAR_URL = os.getenv("DISCORD_AVATAR_URL")

# = Проверка обязательных переменных =
if not TOKEN or not CHAT_ID:
    logging.critical(
        "[TG_SET] TELEGRAM_TOKEN или CHAT_ID не заданы в переменных окружения."
    )
    sys.exit(1)

# = Проверяем наличие папки temp, если нет - создаём =
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

# == Discord ==
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_USER_ID = os.getenv("TWITTER_USER_ID")
TWITTER_USERNAME = "Red_Planet_Dao"                                  # имя пользователя

GUILD_ID = int(os.getenv("GUILD_ID", 0))                             # Сервер Discord
BTC_CHANNEL_ID = int(os.getenv("BTC_CHANNEL_ID", 0))                 # Канал, где меняется имя
COMMAND_CHANNEL_ID = int(os.getenv("COMMAND_CHANNEL_ID", 0))         # Канал, где используются основные команды
GAME_CHANNEL_ID = int(os.getenv("GAME_CHANNEL_ID", 0))               # Канал, где используются игровые команды
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
if not COMMAND_CHANNEL_ID: missing_vars.append("COMMAND_CHANNEL_ID")
if not GAME_CHANNEL_ID: missing_vars.append("GAME_CHANNEL_ID")
if not TWITTER_CHANNEL_ID: missing_vars.append("TWITTER_CHANNEL_ID")

if missing_vars:
    raise ValueError(f"[DC] Не найдены переменные окружения: {', '.join(missing_vars)}")
