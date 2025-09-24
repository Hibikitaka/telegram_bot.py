from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# BotFather で取得したトークンを直接入れる
TOKEN = "7913497593:AAHPw8X2YWWL8FxS-73scjeXg3e-q6lcON4"

# --- コマンドハンドラー ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 こんにちは！\n私はオウム返しボットです。\n/help で使い方を確認できます。"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "使い方:\n"
        "/start - ボットの挨拶\n"
        "/help - このヘルプ表示\n"
        "それ以外のメッセージはオウム返しされます。"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "私はあなたのメッセージをそのまま返すボットです！"
    )

# --- メッセージハンドラー（オウム返し） ---
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # テキストメッセージのみを返す
    await update.message.reply_text(update.message.text)

# --- メイン処理 ---
def main():
    app = Application.builder().token(TOKEN).build()

    # コマンド登録
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))

    # オウム返し登録（テキスト & コマンド以外）
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
