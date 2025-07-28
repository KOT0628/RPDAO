import logging
import asyncio

import tweepy
import aiohttp
import discord

from discord.ui import Button, View
from tweepy.errors import TooManyRequests

from config.settings import (
    GUILD_ID,
    TWITTER_USER_ID,
    TWITTER_USERNAME,
    TWITTER_CHANNEL_ID,
)
import utils.helpers as helpers

# === ПРОВЕРКА И ОТПРАВКА ТВИТОВ ===

...

__all__ = ["fetch_and_send_tweets"]
