import os
import json
import logging
import threading

from collections import defaultdict
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from wcwidth import wcswidth

from config.settings import SCORE_FILE
from utils.helpers import safe_delete_message

# === ФОРМИРОВАНИЕ ТАБЛИЦЫ ЛИДЕРОВ ===
# == Глобальные переменные ==
bot = None                                             # будет установлен извне

# == Внешние установки ==
# = Установка бота =
def set_bot(b):
    global bot
    bot = b

# == Глобальный словарь user_id -> last_page ==
user_score_pages = defaultdict(int)

# == Начисление очков за TRIVIA ==
points = 0

# == Загружаем счёт ==
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            raw_scores = json.load(f)

        # Авто-конвертация в новую структуру
        converted_scores = {}
        for uid, data in raw_scores.items():
            if isinstance(data, int):
                # старый формат
                converted_scores[uid] = {"points": data, "name": f"ID:{uid}"}
            else:
                # уже новый формат
                converted_scores[uid] = data

        return converted_scores

    return {}

scores = load_scores()

# == Сохраняем счёт ==
def save_scores(scores):
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)

# == Начисление очков в Roll и Reroll ==
def add_point(user_id, scores, user_obj=None):
    uid = str(user_id)

    # Определяем имя
    if user_obj:
        name = f"@{user_obj.username}" if user_obj.username else user_obj.first_name
    else:
        name = f"ID:{uid}"

    # Инициализация
    if uid not in scores or not isinstance(scores[uid], dict):
        scores[uid] = {"points": 0, "name": name}

    # Обновляем очки
    scores[uid]["points"] += 1

    # Обновляем имя, если оно изменилось
    if user_obj:
        scores[uid]["name"] = name

    save_scores(scores)

# == Начисление очков в TRIVIA ==
def add_point_trivia(user_id, scores, user_obj=None):
    uid = str(user_id)

    # Определяем имя
    if user_obj:
        name = f"@{user_obj.username}" if user_obj.username else user_obj.first_name
    else:
        name = f"ID:{uid}"

    # Инициализация
    if uid not in scores or not isinstance(scores[uid], dict):
        scores[uid] = {"points": 0, "name": name}

    # Обновляем очки
    scores[uid]["points"] += points

    # Обновляем имя, если оно изменилось
    if user_obj:
        scores[uid]["name"] = name

    save_scores(scores)

# == Начисление очков в BlackJack ==
def add_point_blackjack(user_id, name, scores, delta):
    if not user_id:
        return None

    # Конвертируем имя пользователя
    user_id = str(user_id)
    if user_id not in scores:
        scores[user_id] = {"name": name, "points": 0}

    # Обновляем очки
    scores[user_id]["points"] += delta

    return scores[user_id]["points"]

# === ФОРМИРОВАНИЕ ОТОБРАЕНИЯ ТАБЛИЦЫ ЛИДЕРОВ ===
# == Показ страницы лидерборда ==

...

# == Пагинация с восстановлением текущей страницы ==

...

__all__ = [
    "save_scores",
    "add_point",
    "add_point_trivia",
    "user_score_pages",
    "scores",
    "points",
    "show_score_page",
    "handle_score_pagination",
    "set_bot",
]
