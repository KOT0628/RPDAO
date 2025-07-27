import os
import re
import time
import logging

import deepl
import schedule

from langdetect import detect
from deep_translator import GoogleTranslator

from config.settings import DEEPL_API_KEY

# === ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ===
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
deepl_translator = deepl.Translator(DEEPL_API_KEY)

# === НАСТРОЙКИ ЛОГИРОВАНИЯ ===
logger = logging.getLogger("translate")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("data/translate.txt", encoding='utf-8')
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

if not logger.handlers:                         # Чтобы не дублировать
    logger.addHandler(file_handler)

# Очистка логов
LOG_FILE = "data/translate.txt"

def clear_log_file_translate():
    try:
        with open(LOG_FILE, "w") as f:
            f.truncate(0)
        logger.info("[TRANSLATE] Файл логов успешно очищен.")
    except Exception as e:
        logger.error(f"[TRANSLATE] Ошибка при очистке файла логов: {e}")

# === УНИВЕРСАЛЬНЫЙ ПЕРЕВОДЧИК (DeepL → deep-translator fallback) ===

...

__all__ = [
    "translate_smart",
    "clear_log_file_translate"
]
