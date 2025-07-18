import logging
import threading

from utils.helpers import safe_delete_message

# === ПРОВЕРКА ПРАВ АМИНИСТРАТОРА ===
def is_admin(bot, message):
    try:
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.status in ['administrator', 'creator']
    except Exception as e:
        logging.error(f"Ошибка при проверке прав администратора: {e}")
        msg = bot.reply_to(
            message,
            f"❌ Unable to verify rights.\n\n"
            f"❌ Не удалось проверить права."
        )
        threading.Timer(
            30,
            lambda: safe_delete_message(message.chat.id, msg.message_id)
        ).start()
        return False

__all__ = ["is_admin"]
