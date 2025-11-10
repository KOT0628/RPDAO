import logging
import threading

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.settings import (
    LINK_IMAGE,
    WEB_URL,
    RP_DNA,
    X_URL,
    DC_URL, 
    TG_URL,
    YT_URL,
    MEDIUM_URL,
    INFO_URL_RU,
    INFO_URL_EN
)    
from utils.helpers import (
    delete_command_after,
    safe_delete_message,
    require_bot_active,
)

# === ОБРАБОТЧИК КОМАНДЫ /link ===

...

__all__ = ["register_link_handlers"]
