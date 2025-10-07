"""
Configuration file for Telegram Autoresponder Bot
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Admin Configuration (optional)
ADMIN_ID = os.getenv('ADMIN_ID', None)

# Bot Settings
BOT_USERNAME = os.getenv('BOT_USERNAME', '@your_bot')
RESPONSE_DELAY = int(os.getenv('RESPONSE_DELAY', 0))  # Delay in seconds before responding

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'bot.log')

# Feature Flags
ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'false').lower() == 'true'
ENABLE_RATE_LIMITING = os.getenv('ENABLE_RATE_LIMITING', 'false').lower() == 'true'

# Validate configuration
if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
    raise ValueError("Please set your BOT_TOKEN in the .env file!")