import os
import logging

from logging.handlers import TimedRotatingFileHandler

from config.settings import LOG_FILE

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
formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
    "%Y-%m-%d %H:%M:%S"
)

file_handler.setFormatter(formatter)

# === КОНСОЛЬНЫЙ ВЫВОД ===
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

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
