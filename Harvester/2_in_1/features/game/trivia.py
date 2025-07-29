import os
import random
import logging
import threading

import telebot

from threading import Timer
from word2number import w2n

from telebot.apihelper import ApiTelegramException

from config.settings import TRIVIA_FILE, CHAT_ID, RU_NUMBERS
from features.discord_bridge import send_text
from utils.check_admin import is_admin, admin_only
from utils.helpers import (
    safe_delete_message,
    delete_command_after,
    require_bot_active,
)
from utils.scoreboard import add_point_trivia, scores, save_scores, points

# === ДОБАВЛЯЕМ ВИКТОРИНУ TRIVIA ===
# == Состояние викторины ==
used_trivia_questions = set()
trivia_questions = []                                      # нужно загрузить при запуске
trivia_game_active = False                                 # Вся викторина активна
trivia_active = False                                      # Идёт вопрос
trivia_question_pending = False                            # Готовится следующий вопрос
trivia_random_delay = None                                 # Выбор режима

# == Переменные вопроса ==
current_trivia = None
current_mask_en = None
current_mask_ru = None
hint_index = 0
hint_number = 1
hint_timer = None
hint_message_ids = []                                      # Храним все ID подсказок
last_hint_id = None                                        # ID последней подсказки
next_trivia_timer = None
question_message_id = None
question_counter = 1
first_question_sent = False

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
        logging.info(f"[TG_TRIVIA] Загружено {len(trivia_questions)} вопросов")
    except Exception as e:
        logging.error(f"[TG_TRIVIA] Ошибка загрузки вопросов: {e}")

# == Вспомогательные функции TRIVIA ==
# = Простая поддержка чисел от 0 до 999 прописью на русском =
def parse_russian_number(text):
    words = text.lower().strip().split()
    total = 0
    for word in words:
        if word in RU_NUMBERS:
            total += RU_NUMBERS[word]
        else:
            return None
    return total

# = Преобразует ответ в число (если возможно) или чистит текст =
def normalize_answer(text):
    clean = text.strip().lower()
    
    # Пробуем английсое число
    try:
        return str(w2n.word_to_num(clean))
    except:
        pass

    # Пробуем русское число
    num = parse_russian_number(clean)
    if num is not None:
        return str(num)

    return clean

# = Настройка расписания =

...

# == Отправка первого вопроса ==

...

# == Отправка следующего вопроса ==

...

    # Выход, если викторина уже остановлена

    ...

    # Защита от повторного запуска

    ...

    # Получаем вопросы, которые ещё не использовались

    ...

    # Все вопросы использованы

    ...
            # Сообщение о новом раунде

        ...

        # Повторный запуск списка вопросовт через 1 минуту

        ...

    # Выбираем и задаём новый вопрос

    ...

    # Разбиваем EN и RU версии вопроса

    ...

# == Подсказки ==

...

    # Не отправляем подсказку, если викторина не активна

    ...
    
    # Разбиваем EN и RU версии вопроса

    ...
    
    # Открываем случайную букву в каждой маске

    ...

    # Если хотя бы одна маска полностью раскрыта - никто не угадал

    ...

    # Показываем подсказку

    ...

    # Добавляем ID подсказки в список

    ...

    # Удаляем все подсказки кроме последней

    ...

    # Оставляем только последний ID

    ...

# == Удаление подсказок ==

...

# == Общая логика команды /rpdao_trivia ==

...

    # = Выбор режима =

    ...

# == Регистрация обработчиков ==

...

# == Общая логика команды /rpdao_trivia_off ==

...

# == Регистрация обработчиков ==

...

# == Обработка ответов ==

...

        # = 1. TRIVIA логика =

        ...

        # = 2. Пересылка текста в Discord =
        send_text(message)

__all__ = [
    "set_bot",
    "register_handlers",
    "set_save_scores",
    "load_trivia_questions",
    "start_trivia_handlers",
    "stop_trivia_handlers",
]
