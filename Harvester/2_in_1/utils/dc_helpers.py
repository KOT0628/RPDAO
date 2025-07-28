import os
import re

from config.settings import LAST_PRICE, LAST_TWEET_FILE

# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===
# == Экранируем спецсимволы ==
def escape_markdown(text):
    # Экранируем спецсимволы для MarkdownV2
    escape_chars = r'_*\[\]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

# == Загружаем последнюю цену BTC ==
def load_last_price():
    if os.path.exists(LAST_PRICE):
        with open(LAST_PRICE, "r") as f:
            try:
                return float(f.read().strip())
            except:
                return None
    return None

# == Сохраняем последнюю цену BTC ==
def save_last_price(price):
    with open(LAST_PRICE, "w") as f:
        f.write(str(price))

# == Загружаем последний отправленный твит ==
def load_last_tweet_id():
    if os.path.exists(LAST_TWEET_FILE):
        with open(LAST_TWEET_FILE, "r") as f:
            return f.read().strip()
    return None

# == Сохраняем последний отправленный твит ==
def save_last_tweet_id(tweet_id):
    with open(LAST_TWEET_FILE, "w") as f:
        f.write(str(tweet_id))

# == Глобальные переменные ==
previous_price = load_last_price()                         # Храним предыдущую цену
last_tweet_id = load_last_tweet_id()                       # Храним предыдуший твит
seen_tweet_ids = set()

__all__ = [
    "escape_markdown",
    "previous_price",
    "save_last_price",
    "last_tweet_id",
    "save_last_tweet_id",
    "seen_tweet_ids",
]
