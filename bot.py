from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8574494792:AAEra6buky1C-fyqtFrHErvlohGo3uPfFNc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦅 Mabuhay ang Agila!\nWelcome sa The Fraternal Order of Eagles - Philippine Eagles Inc. Helper!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()