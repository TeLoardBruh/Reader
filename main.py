import logging
import os
import uuid
from gtts import gTTS
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from gtts.lang import tts_langs
from dotenv import load_dotenv


# --- Config ---
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")  # Replace with your BotFather token
OUTPUT_DIR = "tts_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

if not TOKEN:
    raise ValueError("⚠️ TELEGRAM_TOKEN environment variable not set!")

# --- Logging ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# --- Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Send me text and I’ll turn it into voice!\n\n"
        "Commands:\n"
        "/en Your text (English)\n"
        "/km Your text (Khmer)\n"
    )

async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE, lang="en") -> None:
    if not context.args:
        await update.message.reply_text("⚠️ Please provide text after the command.")
        return

    text = " ".join(context.args)

    if len(text) > 3000:  # safety limit
        await update.message.reply_text("⚠️ Text too long. Please send under 3000 characters.")
        return

    try:
        # Generate unique filename
        file_id = str(uuid.uuid4())
        filename = os.path.join(OUTPUT_DIR, f"{file_id}.mp3")

        # Generate TTS
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)

        # Send audio back
        with open(filename, "rb") as f:
            await update.message.reply_audio(f, title="Generated TTS")

        # Cleanup
        os.remove(filename)

    except Exception as e:
        logging.error(f"TTS error: {e}")
        await update.message.reply_text("❌ Error generating speech. Try again.")

async def tts_en(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await text_to_speech(update, context, lang="en")

async def tts_km(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await text_to_speech(update, context, lang="km")

# --- Main ---
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    langs = tts_langs()
    print(langs)
    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("en", tts_en))
    app.add_handler(CommandHandler("kh", tts_km))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
