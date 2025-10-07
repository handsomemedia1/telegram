"""
Telegram Autoresponder Bot
A simple bot that automatically responds to messages based on triggers
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import json
from datetime import datetime
from config import BOT_TOKEN, ADMIN_ID

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load responses from JSON file
def load_responses():
    """Load auto-response rules from responses.json"""
    try:
        with open('responses.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("responses.json not found!")
        return {"triggers": [], "default_response": "Hello! How can I help you?"}

responses_data = load_responses()

# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = (
        f"👋 Hello {user.first_name}!\n\n"
        "I'm an autoresponder bot. Send me any message and I'll respond automatically.\n\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Show help message\n"
        "/status - Check bot status"
    )
    await update.message.reply_text(welcome_message)
    logger.info(f"User {user.id} started the bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = (
        "🤖 *Autoresponder Bot Help*\n\n"
        "This bot automatically responds to your messages based on keywords.\n\n"
        "*Available Commands:*\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/status - Check if bot is active\n\n"
        "Just send me a message and I'll respond!"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show bot status"""
    status_message = (
        "✅ *Bot Status: Active*\n\n"
        f"⏰ Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"👤 Your ID: `{update.effective_user.id}`\n"
        f"💬 Chat ID: `{update.effective_chat.id}`"
    )
    await update.message.reply_text(status_message, parse_mode='Markdown')

# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages and send auto-responses"""
    user_message = update.message.text.lower()
    user = update.effective_user
    
    logger.info(f"Message from {user.id}: {update.message.text}")
    
    # Check for triggers
    response = None
    for trigger in responses_data.get('triggers', []):
        keywords = [kw.lower() for kw in trigger.get('keywords', [])]
        if any(keyword in user_message for keyword in keywords):
            response = trigger.get('response')
            break
    
    # Use default response if no trigger matched
    if not response:
        response = responses_data.get('default_response', "I received your message!")
    
    # Replace placeholders
    response = response.replace('{name}', user.first_name)
    response = response.replace('{time}', datetime.now().strftime('%H:%M'))
    
    await update.message.reply_text(response)

# Error Handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors caused by updates"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Bot started successfully!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()