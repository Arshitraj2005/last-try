import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot config
import config  # Make sure this file has BOT_TOKEN and OWNER_ID

logging.basicConfig(level=logging.INFO)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != config.OWNER_ID:
        return await update.message.reply_text("❌ You are not authorized to control this bot.")
    await update.message.reply_text("✅ Live stream started (dummy response)")

# /stop command
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != config.OWNER_ID:
        return await update.message.reply_text("❌ You are not authorized to control this bot.")
    await update.message.reply_text("🛑 Live stream stopped (dummy response)")

# /status command
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != config.OWNER_ID:
        return await update.message.reply_text("❌ You are not authorized to control this bot.")
    await update.message.reply_text("📡 Live stream is currently running (dummy status)")

app = ApplicationBuilder().token(config.BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", stop))
app.add_handler(CommandHandler("status", status))

app.run_polling()
