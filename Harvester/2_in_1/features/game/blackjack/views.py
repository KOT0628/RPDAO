from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def action_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("➕ Hit", callback_data="hit"),
        InlineKeyboardButton("✋ Stand", callback_data="stand")
    )
    return markup

__all__ = [action_keyboard]
