from .handlers import (
    set_bot,
    set_save_scores,
    register_game_handlers,
)

from .dc_reroll import register_reroll_command

from .dc_roll import register_roll_command

def register_games_commands(bot):
    register_roll_command(bot)
    register_reroll_command(bot)
