from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from blockchain.contract_reader import fetch_total_supply
import config

CONTRACT_ADDRESS, ACTION = range(2)

# Start command
def start(update, context):
    update.message.reply_text("Hello! I can fetch Ethereum contract info for you. Use /contract to start.")

# Command to start contract info process
def contract(update, context):
    update.message.reply_text("Please enter the contract address you'd like to query:")
    return CONTRACT_ADDRESS

# Handle contract address input
def contract_address_handler(update, context):
    context.user_data['contract_address'] = update.message.text
    update.message.reply_text("What info would you like to retrieve? Send /supply to get total supply.")
    return ACTION

# Fetch total supply when requested
def total_supply(update, context):
    contract_address = context.user_data['contract_address']
    result = fetch_total_supply(contract_address)
    update.message.reply_text(result)
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("Operation canceled.")
    return ConversationHandler.END

def main():
    # Set up the bot with the token
    updater = Updater(config.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Set up conversation handler with states CONTRACT_ADDRESS and ACTION
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('contract', contract)],
        states={
            CONTRACT_ADDRESS: [MessageHandler(Filters.text & ~Filters.command, contract_address_handler)],
            ACTION: [CommandHandler('supply', total_supply)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("start", start))

    # Start polling Telegram
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
