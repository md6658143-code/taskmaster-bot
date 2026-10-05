import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Live! /task likho")

async def task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = " ".join(context.args)
    if not txt:
        await update.message.reply_text("Likho: /task Buy milk")
        return
    await update.message.reply_text(f"Task saved: {txt}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("task", task))
app.run_polling()
