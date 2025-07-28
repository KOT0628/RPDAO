import time
import logging

import schedule

from features.price import send_price_image

# === НАСТРОЙКА РАСПИСАНИЯ ===
# == Отправка цены BTC 1 раз в 4 часа ==
schedule.every(4).hours.do(send_price_image)

# === ЗАПУСК ПЛАНИРОВЩИКА ==
def run_scheduler():
    logging.info("[SCHEDULER] Планировщик запущен.")
    while True:
        schedule.run_pending()
        time.sleep(1)

__all__ = ["run_scheduler"]
