import random
import logging
import threading

from . import game_state
from utils.check_admin import admin_only
from utils.helpers import (
    safe_delete_message,
    delete_command_after,
    require_bot_active,
)
from utils.scoreboard import add_point, save_scores, scores
from config.settings import CHAT_ID

# === ИГРА /reroll ===
# == Глобальные переменные ==
bot = None                                      # будет установлен извне

# == Внешние установки ==
# = Установка бота =
def set_bot(b):
    global bot
    bot = b

# = Запись в лидерборд =
def set_save_scores(callback):
    global save_scores
    save_scores = callback

# == Общая логика команды /reroll_on ==

...

# == Регистрация обработчиков ==

...

# == Общая логика команды /reroll_off ==

...

# == Регистрация обработчиков ==

...

# == Память для игры /reroll ==
CHOICES = {
    '🪨': 'Камень',
    '✂️': 'Ножницы',
    '📄': 'Бумага'
}
BEATS = {
    '🪨': '✂️',
    '✂️': '📄',
    '📄': '🪨'
}

# == Обработчик команды /reroll ==

...

__all__ = [
    "set_bot",
    "set_save_scores",
    "start_reroll_handlers",
    "use_reroll",
    "stop_reroll_handlers"
]
