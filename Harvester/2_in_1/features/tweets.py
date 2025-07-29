import pytz
import logging
import asyncio

from datetime import datetime, timedelta

import tweepy
import aiohttp
import discord
import requests

from discord.ui import Button, View
from requests.exceptions import SSLError
from tweepy.asynchronous import AsyncClient
from tweepy.errors import TooManyRequests

import utils.dc_helpers as helpers

from config.settings import (
    GUILD_ID,
    TWITTER_USER_ID,
    TWITTER_USERNAME,
    TWITTER_CHANNEL_ID,
)
from utils.tweets_guard import (
    allow_check,
    mark_checked,
    block_due_to_limit,
    should_skip_fetch,
)

# === ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ===
twitter_enabled = True
twitter_disabled = False

def set_twitter_flags(disabled: bool):
    global twitter_disabled, twitter_enabled
    twitter_disabled = disabled
    twitter_enabled = not disabled

# === ОТКЛЮЧЕНИЕ ПРОВЕРКИ ТВИТОВ ===

...

# === ВКЛЮЧЕНИЕ ПРОВЕРКИ ТВИТОВ ===

...

# == Включение N числа каждого месяца ==

...

# === ПРОВЕРКА И ОТПРАВКА ТВИТОВ ===

...

__all__ = [
    "fetch_and_send_tweets",
    "check_reset_twitter_flag",
]
