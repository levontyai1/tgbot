from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TOKEN = '' # token of telegram bot

def start(update, context):
    txt = "Hello, it is learn-bot"
    update.message.reply_text(txt)


def echo(update, context):
    txt = update.message.text

    if txt.lower() in ['hello', 'wassup']:
        txt = "Sup bro"
    elif txt.lower() in ['bye']:
        txt = "See you later bro"
    else:
        txt = "I dont understand your message. I understand only 'hello', 'wassup' and 'bye' messages"

    update.message.reply_text(txt)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print('Bot is strated...')

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
