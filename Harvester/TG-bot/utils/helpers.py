import os
import re
import random
import logging
import threading
import datetime

import telebot

from threading import Timer

from telebot.apihelper import ApiTelegramException

# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===
# == Экранируем спецсимволы ==
def escape_md(text):
    """Экранирует спецсимволы MarkdownV2"""
    return re.sub(r'([_\*\[\]\(\)~`>#+\-=|{}.!\\])', r'\\\1', str(text))

# == Фильтрация старых сообщений ==
def is_recent(message):
    now = datetime.datetime.utcnow()
    msg_time = datetime.datetime.utcfromtimestamp(message.date)
    # Не обрабатывать сообщения старше 15 секунд
    return (now - msg_time).total_seconds() < 15

# == Безопасное удаление сообщений ==
def safe_delete_message(bot, chat_id, message_id):
    try:
        bot.delete_message(chat_id, message_id)
        # logging.info(f"Удалена команда в чате {chat_id}")
    except ApiTelegramException as e:
        if "message to delete not found" in str(e):
            logging.debug(f"Сообщение {message_id} уже удалено.")
        else:
            logging.warning(
                f"Не удалось удалить сообщение {message_id} из чата {chat_id}: {e}"
            )
    except Exception as e:
        logging.warning(
            f"Ошибка при удалении сообщения {message_id} из чата {chat_id}: {e}"
        )

# == Удаление слэш-команд ==
def delete_command_after(bot, seconds=5):
    def decorator(func):
        def wrapper(message, *args, **kwargs):
            result = func(message, *args, **kwargs)
            threading.Timer(
                seconds,
                lambda: safe_delete_message(bot, message.chat.id, message.message_id)
            ).start()
            return result
        return wrapper
    return decorator

# == Выбор случайного фона ==
def get_random_background(folder):
    try:
        files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png'))]
        return os.path.join(folder, random.choice(files))
    except Exception as e:
        logging.error(f"Ошибка при выборе фонового изображения: {e}")
        return None

__all__ = [
    "escape_md",
    "is_recent",
    "safe_delete_message",
    "delete_command_after",
    "get_random_background"
]
