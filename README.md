link -> to read [text](https://docs.python-telegram-bot.org/en/stable/)

# Telegram TTS Bot

A Telegram bot that converts text to speech (English & Khmer).  
Users can send commands like `/en Your text` or `/km Your text` to generate voice messages.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/telegram-tts-bot.git
cd telegram-tts-bot

# Telegram TTS Bot

A Telegram bot that converts text to speech (English & Khmer).  
Users can send commands like `/en Your text` or `/km Your text` to generate voice messages.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/telegram-tts-bot.git
cd telegram-tts-bot
Create a virtual environment:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate      # Windows
source venv/bin/activate     # Linux/Mac
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file:

ini
Copy code
TELEGRAM_TOKEN=YOUR_BOT_TOKEN
Run the bot:

bash
Copy code
python main.py
Commands
/start – Shows instructions

/en <text> – English TTS

/km <text> – Khmer TTS

yaml
Copy code

---

Make pip freeze > requirements.txt