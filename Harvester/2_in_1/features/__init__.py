from .crimson_board import register_crimson_board

from .dc_price import (
    register_price_command,
    update_btc_channel_name,
)

from .discord_bridge import (
    set_bot,
    send_to_discord,
    send_photo_to_discord,
    send_text,
    send_photo,
)

from .gm_gn import (
    set_bot,
    register_handlers,
)

from .link import register_link_handlers

from .price import (
    send_price_image,
    use_price,
    set_bot,
)

from .score import register_handlers

from .stop_start import stop_start_handlers

from .tag import tag_handlers

from .telegram_bridge import register_tg_bridge_command

from .ticket_notify import on_guild_channel_create

from .tweets import (
    fetch_and_send_tweets,
    check_reset_twitter_flag,
    set_twitter_flags,
)

def register_utils_commands(bot):
    register_price_command(bot)
    register_tg_bridge_command(bot)
