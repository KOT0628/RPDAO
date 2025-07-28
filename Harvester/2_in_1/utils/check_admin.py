import logging
import threading

from functools import wraps
from telebot.types import Message, CallbackQuery

from utils.helpers import safe_delete_message

# === ПРОВЕРКА ПРАВ АМИНИСТРАТОРА ===

...

# == Декоратор для для проверки прав админов ==

...

__all__ = ["admin_only"]
