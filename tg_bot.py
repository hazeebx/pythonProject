from telegram import Update
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Updater, MessageHandler, Filters


def send_message(bot_token, chat_id, message_text):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message_text)

def message_handler(update, context):
    # Check if the update is a channel post
    if update.channel_post:
        # Get the channel post object
        channel_post = update.channel_post

        # Process the channel post
        # In this example, we'll just print the text of the channel post
        recieved = channel_post.text
        print(recieved)
    else:
        # Process the message (for direct messages or messages in groups)
        # In this example, we'll just print the text of the message
        print("Message Text:", update.message.text)


def main(a):
    # Replace 'YOUR_BOT_API_TOKEN' with your bot's API token
    updater = Updater("6839264217:AAHR26B2X13KBFMt-ZN1YcFJa0JBIcp-ir4", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register a message handler
    dp.add_handler(MessageHandler(Filters.all, message_handler))

    # Register a command handler to trigger sending a message
    dp.add_handler(CommandHandler("sendmessage", send_message))

    # Start the Bot
    updater.start_polling()

    # Replace 'YOUR_CHANNEL_ID' with the ID of the channel you want to send the message to
    chat_id = '-1002139101529'
    # Replace 'YOUR_MESSAGE_TEXT' with the text of the message you want to send
    message_text = a

    # Call the send_message function
    send_message("6839264217:AAHR26B2X13KBFMt-ZN1YcFJa0JBIcp-ir4", chat_id, message_text)

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main("test")