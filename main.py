from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from stream import start_streaming, stop_streaming, check_status
from keep_alive import keep_alive
import config

app = ApplicationBuilder().token(config.BOT_TOKEN).build()

is_streaming = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_streaming
    if is_streaming:
        await update.message.reply_text("Stream already running.")
    else:
        is_streaming = True
        await update.message.reply_text("Starting stream...")
        start_streaming()
        await update.message.reply_text("Stream started.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_streaming
    if not is_streaming:
        await update.message.reply_text("Stream is not running.")
    else:
        stop_streaming()
        is_streaming = False
        await update.message.reply_text("Stream stopped.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Streaming ✅" if check_status() else "Not streaming ❌")

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", stop))
app.add_handler(CommandHandler("status", status))

keep_alive()
app.run_polling()


