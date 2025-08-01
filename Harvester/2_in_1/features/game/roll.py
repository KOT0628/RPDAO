import random
import logging
import threading

from . import game_state
from .reroll import use_reroll
from config.settings import CHAT_ID
from utils.check_admin import admin_only
from utils.helpers import (
    safe_delete_message,
    delete_command_after,
    require_bot_active,
)
from utils.scoreboard import add_point, scores, save_scores

# === ИГРА /roll ===
# == Глобальные переменные ==
roll_round_active = False
roll_results = {}                               # user_id: (score, display_name, username)
roll_finish_timer = None
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

# == Состояние раунда ==
def is_roll_active():
    return roll_round_active

def get_roll_players():
    return list(roll_results.keys())

# == Старт раунда ==

...

# == Общая логика команды /start_roll ==

...

# == Регистрация обработчиков ==

...

# == Завершение раунда ==
...

# == Принудительная остановка ==

...

# == Регистрация обработчиков ==

...

# == Обработчик команды /roll ==

...

__all__ = [
    "set_bot",
    "set_save_scores",
    "start_roll_handlers",
    "use_roll",
    "stop_roll_handlers",
    "start_roll_round",
    "is_roll_active",
    "get_roll_players",
]
