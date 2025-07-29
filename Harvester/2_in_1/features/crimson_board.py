import json
import logging
import threading

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.helpers import (
    delete_command_after,
    safe_delete_message,
    require_bot_active,
)

# === ПУТИ И НАСТРОЙКИ ===
CRIMSON_FILE = "data/leaderboard/crimson_scores.json"
MAX_PER_PAGE = 10

# Хранение текущих страниц для пользователей
crimson_pages = {}

# === ЗАГРУЗКА/ФОРМАТ ===

...

# == Формирование таблицы ==

...

# == Кнопки только для нужного пользователя ==

...

# === ОБРАБОТЧИК КОМАНДЫ /crimson_board ===

...

    # == Обработка выбора способа показа ==

    ...

__all__ = ["register_crimson_board"]
