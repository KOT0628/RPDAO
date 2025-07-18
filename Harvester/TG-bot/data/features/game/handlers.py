from . import roll
from . import reroll
from . import trivia

def set_bot(bot):
    roll.set_bot(bot)
    reroll.set_bot(bot)
    trivia.set_bot(bot)

def set_save_scores(callback):
    roll.set_save_scores(callback)
    reroll.set_save_scores(callback)
    trivia.set_save_scores(callback)

def register_game_handlers(bot):
    roll.start_roll(bot)
    roll.use_roll(bot)
    roll.stop_roll(bot)

    reroll.start_reroll(bot)
    reroll.use_reroll(bot)
    reroll.stop_reroll(bot)

    trivia.start_trivia(bot)
    trivia.stop_trivia(bot)
    trivia.register_handlers(bot)

__all__ = [
    "set_bot",
    "set_save_scores",
    "register_game_handlers",
]
