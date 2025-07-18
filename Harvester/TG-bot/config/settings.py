import os
import logging

import deepl

from dotenv import load_dotenv

# === РАБОТА С ФАЙЛАМИ ===
# == Файл блокировки ==
LOCK_FILE = "data/bot.lock"

# == Файл логов ==
LOG_FILE = "data/logs.txt"

# == Таблица лидеров ==
SCORE_FILE = "data/scores.json"

# == Список вопросов TRIVIA ==
TRIVIA_FILE = "data/trivia_questions.txt"

# == Генерация изображений ==
BACKGROUND_PATH = "assets/backgrounds/background.jpg"
FONT_PATH = "assets/fonts/SpicyRice-Regular.ttf"
BTC_IMAGE_OUTPUT = "data/btc_price_output.jpg"
GM_IMAGE_OUTPUT = "data/gm_output.jpg"
GN_IMAGE_OUTPUT = "data/gn_output.jpg"

# === ЗАГРУЗКА ПЕРЕМЕННЫХ ОКРУЖЕНИЯ ===
load_dotenv()

# === ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ===
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = str(os.getenv("CHAT_ID"))
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
DISCORD_AVATAR_URL = os.getenv("DISCORD_AVATAR_URL")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
deepl_translator = deepl.Translator(DEEPL_API_KEY)

# Проверка обязательных переменных
if not TOKEN or not CHAT_ID:
    logging.critical(
        "TELEGRAM_TOKEN или CHAT_ID не заданы в переменных окружения."
    )
    sys.exit(1)

# Проверяем наличие папки temp, если нет - создаём
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)
