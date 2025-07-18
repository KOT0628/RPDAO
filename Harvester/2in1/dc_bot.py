# === СТАНДАРТНЫЕ БИБЛИОТЕКИ ===
import os
import re
import sys
import json
import time
import random
import logging
import asyncio
import datetime
import schedule
import threading

# === СТОРОННИЕ БИБЛИОТЕКИ ===
import tweepy
import aiohttp
import discord
import requests
from discord.ext import commands
from discord.ui import Button, View
from tweepy.errors import TooManyRequests

# === ЛОКАЛЬНЫЕ ИМПОРТЫ ===
from config.settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    DISCORD_TOKEN,
    BEARER_TOKEN,
    TWITTER_USER_ID,
    TWITTER_USERNAME,
    GUILD_ID,
    BTC_CHANNEL_ID,
    TWITTER_CHANNEL_ID,
    LAST_PRICE,
    LAST_TWEET_FILE,
    MAP_FILE,
    BACKGROUND_PATH,
    FONT_PATH,
)
from utils.image import create_price_image
from utils.helpers import escape_markdown

...
