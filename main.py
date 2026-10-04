import os, json
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID","0"))
FILE = "approved_users.json"

def load():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except:
        return []

def save(d):
    with open(FILE,"w") as f:
        json.dump(d,f)

async def start(u,c):
    await u.message.reply_text("Bot chalu ✅")

async def myid(u,c):
    await u.message.reply_text(f"ID: {u.effective_user.id}")

async def approve(u,c):
    if u.effective_user.id!=ADMIN_ID:
        await u.message.reply_text("Admin na")
        return
    if len(c.args)!=1:
        await u.message.reply_text("Use /approve ID")
        return
    uid=int(c.args[0])
    d=load()
    if uid not in d:
        d.append(uid)
        save(d)
    await u.message.reply_text(f"OK {uid}")

def main():
    a=Application.builder().token(BOT_TOKEN).build()
    a.add_handler(CommandHandler("start",start))
    a.add_handler(CommandHandler("myid",myid))
    a.add_handler(CommandHandler("approve",approve))
    a.run_polling()

if __name__=="__main__":
    main()
