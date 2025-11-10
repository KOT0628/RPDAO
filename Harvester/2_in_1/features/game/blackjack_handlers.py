import logging
import threading

from telebot.types import CallbackQuery

from .blackjack.game_state import active_games, waiting_player
from .blackjack.blackjack import Game, Player
from .blackjack.views import action_keyboard
from utils.blackjack_logger import get_blackjack_logger
from utils.helpers import (
    safe_delete_message,
    delete_command_after,
    require_bot_active,
)
from utils.scoreboard import add_point_blackjack, scores, save_scores, load_scores

bot = None

# === Установка бота ===
def set_bot(b):
    global bot
    bot = b

# === Общая логика команды /blackjack ===

...

# == Регистрация обработчиков ==

...

# === Проверка таймаута ожидания второго игрока ===

...

# === Начало партии ===

...

# === Обработчик кнопок (Hit / Stand) ===

...

# === Завершение игры ===

...

__all__ = [
    "set_bot",
    "start_blackjack",
    "start_blackjack_callbacks"
]
