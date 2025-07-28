from .price import (
    register_price_command,
    update_btc_channel_name,
)

from .reroll import register_reroll_command

from .roll import register_roll_command

from .telegram_bridge import register_tg_bridge_command

from .tweets import fetch_and_send_tweets

def register_all_commands(bot):
    register_price_command(bot)
    register_roll_command(bot)
    register_reroll_command(bot)
    register_tg_bridge_command(bot)
  
