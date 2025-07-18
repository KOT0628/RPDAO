import os
import json

from collections import defaultdict

from config.settings import SCORE_FILE

# === ФОРМИРОВАНИЕ ТАБЛИЦЫ ЛИДЕРОВ ===

# == Глобальный словарь user_id -> last_page ==
user_score_pages = defaultdict(int)

# == Начисление очков за TRIVIA ==
points = 1

# == Загружаем счёт ==
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

scores = load_scores()

# == Сохраняем счёт ==
def save_scores(scores):
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)

# == Начисление очков в Roll и Reroll ==
def add_point(winner_id, scores):
    scores[str(winner_id)] = scores.get(str(winner_id), 0) + 1
    save_scores(scores)

# == Начисление очков в TRIVIA ==
def add_point_trivia(user_id, scores):
    scores[str(user_id)] = scores.get(str(user_id), 0) + points
    save_scores(scores)

__all__ = [
    "save_scores",
    "add_point",
    "add_point_trivia",
    "user_score_pages",
    "scores",
    "points"
]
