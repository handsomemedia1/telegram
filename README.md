# Telegram Autoresponder Bot

A simple Telegram bot that automatically responds to messages based on keywords and triggers.

## Features

- ✅ Automatic responses based on keyword triggers
- ✅ Customizable response rules via JSON file
- ✅ Support for placeholders (name, time)
- ✅ Command handlers (/start, /help, /status)
- ✅ Error logging and handling
- ✅ Easy configuration via .env file

## Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (get it from [@BotFather](https://t.me/botfather))

## Installation

1. **Clone or download this project**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Telegram Bot**
   - Open Telegram and search for [@BotFather](https://t.me/botfather)
   - Send `/newbot` and follow the instructions
   - Copy the bot token you receive

4. **Configure the bot**
   - Open the `.env` file
   - Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token
   ```
   BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

5. **Customize responses (optional)**
   - Edit `responses.json` to add or modify auto-response rules
   - Add keywords and corresponding responses

## Usage

### Start the bot

```bash
python bot.py
```

You should see:
```
Bot started successfully!
```

### Test the bot

1. Open Telegram and search for your bot (use the username you got from BotFather)
2. Send `/start` to initialize the bot
3. Send any message to test the autoresponder

### Available Commands

- `/start` - Initialize the bot and see welcome message
- `/help` - Display help information
- `/status` - Check bot status and current time

## Customizing Responses

Edit `responses.json` to customize how the bot responds:

```json
{
  "triggers": [
    {
      "keywords": ["hello", "hi"],
      "response": "Hello {name}! How can I help you?"
    }
  ]
}
```

### Placeholders

- `{name}` - User's first name
- `{time}` - Current time (HH:MM format)

## File Structure

```
telegram-autoresponder-test/
├── bot.py              # Main bot logic
├── config.py           # Configuration settings
├── responses.json      # Auto-response rules
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (bot token)
└── README.md          # This file
```

## Configuration Options

Edit `.env` to configure:

- `BOT_TOKEN` - Your Telegram bot token (required)
- `ADMIN_ID` - Your Telegram user ID (optional)
- `RESPONSE_DELAY` - Delay in seconds before responding (default: 0)
- `LOG_LEVEL` - Logging level: INFO, DEBUG, WARNING, ERROR (default: INFO)

## Troubleshooting

### Bot doesn't respond
- Check if the bot token is correct in `.env`
- Ensure the bot is running (`python bot.py`)
- Check for errors in the console

### "responses.json not found" error
- Make sure `responses.json` is in the same directory as `bot.py`

### Import errors
- Install dependencies: `pip install -r requirements.txt`
- Make sure you're using Python 3.8 or higher

## Support

For issues or questions:
1. Check the console for error messages
2. Verify your bot token is correct
3. Ensure all files are in the correct location

## License

This project is free to use and modify for personal and commercial purposes.

## Contributing

Feel free to fork and improve this bot! Suggestions and contributions are welcome.

---

**Happy botting!** 🤖