import os
import json
import logging
import threading

from config.settings import MAP_FILE

# === ЗАГРУЗКА МАППИНГА СООБЩЕНИЙ ===
LOCK = threading.Lock()

def load_mapping():
    if not os.path.exists(MAP_FILE):
        return {}
    try:
        with open(MAP_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.warning(
            f"[MAP] Ошибка загрузки маппинга: {e}. Заменяем на пустой словарь."
        )
        return {}

# == Сохранение соответствия ==
def save_mapping(key, value):
    with LOCK:
        data = load_mapping()
        data[str(key)] = value
        try:
            with open(MAP_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logging.error(f"[MAP] Ошибка при сохранении файла {MAP_FILE}: {e}")

# == Получение Telegram message_id по Discord message_id ==
def get_telegram_reply_id(discord_message_id):
    data = load_mapping()
    return data.get(str(discord_message_id))

__all__ = [
    "save_mapping",
    "get_telegram_reply_id"
]
