import json
import logging
import threading

from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton, CallbackQuery

from config.settings import CHAT_ID
from utils.helpers import (
    safe_delete_message,
    delete_command_after,
    require_bot_active,
)
from utils.scoreboard import show_score_page, handle_score_pagination, user_score_pages

# === ВНЕШНИЕ УСТАНОВКИ ===
# == Установка бота ==
def set_bot(b):
    global bot
    bot = b

# === ЛИДЕРБОРД ===
# == Обработчик команды /score ==

...

# == Обработка выбора способа показа ==

...

# == Объединим функции score, score_mode, handle_score_pagination ==
def register_handlers(bot):
    score(bot)
    set_bot(bot)
    score_mode(bot)
    handle_score_pagination(bot)

__all__ = ["register_handlers"]
