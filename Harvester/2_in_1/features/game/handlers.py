from . import blackjack_handlers
from . import game_menu
from . import roll
from . import reroll
from . import trivia

def set_bot(bot):
    blackjack_handlers.set_bot(bot)
    game_menu.set_bot(bot)
    roll.set_bot(bot)
    reroll.set_bot(bot)
    trivia.set_bot(bot)

def set_save_scores(callback):
    roll.set_save_scores(callback)
    reroll.set_save_scores(callback)
    trivia.set_save_scores(callback)

# print("[DEBUG] Импорт handlers.py")
def register_game_handlers(bot):
    blackjack_handlers.start_blackjack(bot)
    blackjack_handlers.start_blackjack_callbacks(bot)
    
    roll.start_roll_handlers(bot)
    roll.use_roll(bot)
    roll.stop_roll_handlers(bot)

    reroll.start_reroll_handlers(bot)
    reroll.use_reroll(bot)
    reroll.stop_reroll_handlers(bot)

    trivia.start_trivia_handlers(bot)
    trivia.stop_trivia_handlers(bot)
    trivia.register_handlers(bot)
    
    game_menu.register_game_menu_handlers(bot)

__all__ = [
    "set_bot",
    "set_save_scores",
    "register_game_handlers",
]
