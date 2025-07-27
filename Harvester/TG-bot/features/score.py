import json
import logging
import threading

from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton, CallbackQuery

from config.settings import CHAT_ID
from utils.helpers import safe_delete_message, delete_command_after
from utils.scoreboard import user_score_pages, scores

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

# == Показ страницы лидерборда ==

...

# == Пагинация с восстановлением текущей страницы ==

...

# == Объединим функции score, score_mode, score_pagination ==
def register_handlers(bot):
    set_bot(bot)
    score(bot)
    score_mode(bot)
    score_pagination(bot)

__all__ = ["register_handlers"]
