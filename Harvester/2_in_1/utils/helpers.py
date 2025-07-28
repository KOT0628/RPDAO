import os
import re
import random
import logging
import threading
import datetime

import telebot

from threading import Timer

from telebot.apihelper import ApiTelegramException

# === ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ===
bot_active = True

# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===
# == Экранируем спецсимволы ==
def escape_md(text):
    # Экранируем спецсимволы для MarkdownV2
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
        # logging.info(f"[TG] Удалена команда в чате {chat_id}")
    except ApiTelegramException as e:
        if "message to delete not found" in str(e):
            logging.debug(f"[TG] Сообщение {message_id} уже удалено.")
        else:
            logging.warning(
                f"[TG] Не удалось удалить сообщение {message_id} из чата "
                f"{chat_id}: {e}"
            )
    except Exception as e:
        logging.warning(
            f"[TG] Ошибка при удалении сообщения {message_id} из чата "
            f"{chat_id}: {e}"
        )

# == Удаление слэш-команд ==
def delete_command_after(bot, seconds=5):
    def decorator(func):
        def wrapper(message, *args, **kwargs):
            result = func(message, *args, **kwargs)
            threading.Timer(
                seconds,
                lambda: safe_delete_message(
                    bot,
                    message.chat.id,
                    message.message_id
                )
            ).start()
            return result
        return wrapper
    return decorator

# == Декоратор состояния слэш-команд ==
def require_bot_active(func):
    global bot_active

    def wrapper(message):
        if not bot_active and message.text != '/start':
            return
        return func(message)
    return wrapper

# == Выбор случайного фона ==
def get_random_background(folder):
    try:
        files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png'))]
        return os.path.join(folder, random.choice(files))
    except Exception as e:
        logging.error(
            f"[RANDOM] Ошибка при выборе фонового изображения: {e}"
        )
        return None

__all__ = [
    "escape_md",
    "is_recent",
    "safe_delete_message",
    "delete_command_after",
    "get_random_background",
    "get_points",
    "require_bot_active",
]
