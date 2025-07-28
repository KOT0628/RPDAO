import os
import re
import time
import logging

from logging.handlers import TimedRotatingFileHandler

import html
import deepl
import schedule

from langdetect import detect
from deep_translator import GoogleTranslator
from google.cloud import translate_v2 as translate

from config.settings import DEEPL_API_KEY

# === ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ===
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
deepl_translator = deepl.Translator(DEEPL_API_KEY)

# === НАСТРОЙКИ ЛОГИРОВАНИЯ ===
# == Ссоздание папки ==
LOG_DIR = os.path.join("data", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "translate.log")

# == Логгер ==
logger = logging.getLogger("translate")
logger.setLevel(logging.INFO)

# = Чтобы не дублировать обработчики =
if not logger.handlers:
    handler = TimedRotatingFileHandler(
        LOG_FILE, when="midnight", interval=1, backupCount=7, encoding='utf-8'
    )
    handler.suffix = "%Y-%m-%d"

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

# === УНИВЕРСАЛЬНЫЙ ПЕРЕВОДЧИК (DeepL → deep-translator fallback) ===

...

__all__ = ["translate_smart"]
