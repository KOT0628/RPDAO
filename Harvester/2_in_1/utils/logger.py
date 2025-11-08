import os
import logging

from logging.handlers import TimedRotatingFileHandler

from config.settings import LOG_FILE

# === ИНИЦИАЛИЗАЦИЯ COLORAMA ===
try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

# === ЦВЕТА ===
CYAN = "\033[96m"                                          # голубой
GREEN = "\033[92m"                                         # зелёный
YELLOW = "\033[93m"                                        # жёлтый
RED = "\033[91m"                                           # красный
PURPLE = "\033[95m"                                        # пурпурный
RESET = "\033[0m"

# === КАСТОМНЫЙ ФОРМАТТЕР ===
class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: CYAN,
        logging.INFO: GREEN,
        logging.WARNING: YELLOW,
        logging.ERROR: RED,
        logging.CRITICAL: PURPLE,
    }
    def format(self, record):
        color = self.COLORS.get(record.levelno, RESET)
        record.levelname = f"{color}{record.levelname}{RESET}"
        record.msg = f"{color}{record.msg}{RESET}"
        return super().format(record)

# === ПАРАМЕТРЫ ===
LOG_DIR = os.path.dirname(LOG_FILE)
os.makedirs(LOG_DIR, exist_ok=True)

# === СОЗДАЁМ ОБЩИЙ ЛОГГЕР ===
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# === УДАЛЯЕМ ВСЕ СТАРЫЕ ХЕНДЛЕРЫ (если уже настроено через basicConfig) ===
logger.handlers.clear()

# === ОБРАБОТЧИК С РОТАЦИЕЙ РАЗ В СУТКИ ===
file_handler = TimedRotatingFileHandler(
    LOG_FILE,
    when="midnight",
    interval=1,
    backupCount=7,                                         # Хранить 7 дней
    encoding='utf-8'
)
file_handler.suffix = "%Y-%m-%d"

# === ФОРМАТ ЛОГОВ ===
# == Файловый вывод ==
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
    "%Y-%m-%d %H:%M:%S"
)

file_handler.setFormatter(file_formatter)

# == Консольный вывод ==
console_handler = logging.StreamHandler()
console_formatter = ColorFormatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
    "%Y-%m-%d %H:%M:%S"
)

console_handler.setFormatter(console_formatter)

# === ПРИКРЕПЛЯЕМ ОБРАБОТЧИКИ ===
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# === ПОДДЕРЖКА CLEAR ===
def clear_log_file():
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.truncate(0)
        logging.info("[LOGGER] Файл логов успешно очищен.")
    except Exception as e:
        logging.error(f"[LOGGER] Ошибка при очистке файла логов: {e}")

__all__ = ["clear_log_file"]
