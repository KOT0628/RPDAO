import os
import random
import logging
import threading

import telebot

from threading import Timer

from telebot.apihelper import ApiTelegramException

from config.settings import TRIVIA_FILE, CHAT_ID
from features.discord_bridge import send_text
from utils.check_admin import is_admin
from utils.helpers import safe_delete_message, delete_command_after
from utils.scoreboard import add_point_trivia, scores, save_scores, points

# === ДОБАВЛЯЕМ ВИКТОРИНУ TRIVIA ===
# == Состояние викторины ==
used_trivia_questions = set()
trivia_questions = []                                      # нужно загрузить при запуске
trivia_game_active = False                                 # Вся викторина активна
trivia_active = False                                      # Идёт вопрос
trivia_question_pending = False                            # Готовится следующий вопрос

# == Переменные вопроса ==
current_trivia = None
current_mask_en = None
current_mask_ru = None
hint_index = 0
hint_number = 1
hint_timer = None
next_trivia_timer = None
question_message_id = None

bot = None                                                 # будет установлен извне

# == Внешние установки ==
# = Установка бота =
def set_bot(b):
    global bot
    bot = b

# = Запись в лидерборд =
def set_save_scores(callback):
    global save_scores
    save_scores = callback

# == Загрузка вопросов ==
def load_trivia_questions():
    global trivia_questions
    try:
        with open(TRIVIA_FILE, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if ':' in line]
            trivia_questions = [tuple(line.split(':')) for line in lines]
        logging.info(f"[TRIVIA] Загружено {len(trivia_questions)} вопросов")
    except Exception as e:
        logging.error(f"[TRIVIA] Ошибка загрузки вопросов: {e}")

# == Отправка следующего вопроса ==

...

# == Подсказки ==

...

# == Запуск викторины (только админ) ==

...

# == Остановка викторины (только админ) ==

...

# == Обработка ответов ==

...

__all__ = [
    "set_bot",
    "register_handlers",
    "set_save_scores",
    "load_trivia_questions",
    "start_trivia",
    "stop_trivia",
]
