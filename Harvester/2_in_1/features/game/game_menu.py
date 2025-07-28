import logging
import threading

from telebot import TeleBot
from telebot.types import (
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

from config.settings import (
    CHAT_ID,
    GAME_IMAGE,
    ROLL_IMAGE,
    REROLL_IMAGE,
    TRIVIA_IMAGE,
    LEADERBOARD_IMAGE,
)
from utils.helpers import (
    safe_delete_message,
    delete_command_after,
    require_bot_active,
)
from utils.scoreboard import user_score_pages, show_score_page

# === ИГРОВАЯ ЗОНА RPDAO ===
# == Глобальные переменные ==
bot = None

# == Хранилище последних меню по chat_id ==
last_game_menus = {}                                   # {chat_id: message_id}

# == Внешние установки ==
# = Установка бота =
def set_bot(b):
    global bot
    bot = b

# == Главное меню (GAME ZONE) ==

...

# == Подменю ==

...

# == Регистрация хендлеров ==

...

    # = Callback-переключатели =

    ...

    # = Логика Leaderboard =

    ...

        # Сохраняем текущую страницу, если не была сохранена

        ...

        # Удаляем сообщение с кнопками

        ...

__all__ = [
    "set_bot",
    "register_game_menu_handlers",
]
