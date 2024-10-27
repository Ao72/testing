import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os
import glob

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your bot token
BOT_TOKEN = "7839351456:AAGX6jgW7svU4WYs5rNeh6JVSbjJE2ps85E"

# Define the folders for each keyword
IMAGE_FOLDERS = {
    "uwu": "ScoopCast",
    "cat": "Cat"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text("Hello! this aman sinha from SuperSuper Send me the the magic word:) ")

async def send_images(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send images based on the received keyword."""
    keyword = update.message.text.lower()
    if keyword in IMAGE_FOLDERS:
        folder_path = IMAGE_FOLDERS[keyword]
        images = glob.glob(f"{folder_path}/*")
        
        for image_path in images:
            with open(image_path, 'rb') as photo:
                await context.bot.send_photo(chat_id=update.message.chat_id, photo=photo)
    else:
        await update.message.reply_text("Sorry, I don't recognize that keyword. Try uwu'.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_images))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
