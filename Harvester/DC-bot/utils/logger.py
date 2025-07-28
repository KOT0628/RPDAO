import logging

from config.settings import LOG_FILE

# === НАСТРОЙКИ ЛОГИРОВАНИЯ ===
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# == Очистка файла логов ==
def clear_log_file():
    try:
        with open(LOG_FILE, "w") as f:
            f.truncate(0)
        logging.info("[LOGGER] Файл логов успешно очищен.")
    except Exception as e:
        logging.error(f"[LOGGER] Ошибка при очистке файла логов: {e}")

__all__ = ["clear_log_file"]
