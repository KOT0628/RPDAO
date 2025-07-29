import logging
import threading

from utils import helpers
from utils.check_admin import admin_only
from utils.helpers import safe_delete_message, delete_command_after

# === ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ===
bot = None                                      # будет установлен извне

# === ВНЕШНИЕ УСТАНОВКИ ===
# == Установка бота ==
def set_bot(b):
    global bot
    bot = b

# === КОМАНДЫ УПРАВЛЕНИЯ ===
# == Обработка команды /stop ==

...

# == Обработка команды /start ==

...

# == Объединим функции управления ===
def stop_start_handlers(bot):
    set_bot(bot)
    stop_handlers(bot)
    start_handlers(bot)

__all__ = ["stop_start_handlers"]
