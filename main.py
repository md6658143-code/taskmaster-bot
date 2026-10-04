import os, json
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
APPROVED_FILE = "approved_users.json"

def load_approved():
    try:
        with open(APPROVED_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_approved(data):
    with open(APPROVED_FILE, "w") as f:
        json.dump(data, f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot cholche ✅ /myid likho")

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Tomar ID: {update.effective_user.id}")

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id!= ADMIN_ID:
        await update.message.reply_text("Tumi admin na")
        return
    if len(context.args)!= 1:
        await update.message.reply_text("Use: /approve USER_ID")
        return
    uid = int(context.args[0])
    approved = load_approved()
    if uid not in approved:
        approved.append(uid)
        save_approved(approved)
        await update.message.reply_text(f"Approved {uid}")
    else:
        await update.message.reply_text("Age thekei approved")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("myid", myid))
    app.add_handler(CommandHandler("approve", approve))
    app.run_polling()

if __name__ == "__main__":
    main()
