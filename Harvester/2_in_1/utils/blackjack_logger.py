import os
import logging

from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# === Инициализация COLORAMA ===
try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

# === Цвета ===
TURQ = "\033[36m"                                        # бирюзовый
RESET = "\033[0m"

# === Базовый каталог для логов Blackjack ===
BASE_DIR = os.path.join("data", "logs", "blackjack")
os.makedirs(BASE_DIR, exist_ok=True)

# === Кэш логгеров, чтобы не создавать дубликаты ===
_blackjack_loggers = {}

def get_blackjack_logger(chat_id: int) -> logging.Logger:
    """
    Возвращает уникальный логгер для конкретного чата.
    Логи пишутся в data/logs/blackjack/chat_<id>/<дата>.log
    """
    global _blackjack_loggers

    if chat_id in _blackjack_loggers:
        return _blackjack_loggers[chat_id]

    # == Создаём каталог для конкретного чата ==
    chat_dir = os.path.join(BASE_DIR, f"chat_{chat_id}")
    os.makedirs(chat_dir, exist_ok=True)

    log_file = os.path.join(chat_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

    # == Настраиваем логгер ==
    logger = logging.getLogger(f"blackjack_{chat_id}")
    logger.setLevel(logging.INFO)
    
    # не дублировать в общий лог
    logger.propagate = False

    # == Проверка, чтобы не было двойных хендлеров ==
    if not logger.handlers:
        # === Файловый хендлер с ротацией ===
        file_handler = TimedRotatingFileHandler(
            log_file,
            when="midnight",
            interval=1,
            backupCount=7,
            encoding="utf-8"
        )
        file_handler.suffix = "%Y-%m-%d"
        file_formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)

        # == Консольный хендлер с цветом ==
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            f"{RESET}[%(asctime)s.%(msecs)03d] {TURQ}[%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    _blackjack_loggers[chat_id] = logger
    return logger

__all__ = ["get_blackjack_logger"]
