from telegram.ext import Updater
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import BaseFilter


if __name__ == '__main__':
    token = '938075561:AAEfv4Mcm9qOW3_EPgCy770usqDdAL8I34M'
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    def get_login(api_k, api_s):  # log in to zerodha API panel
        global kws, kite, request_tkn, access_token
        kite = KiteConnect(api_key=api_k)

        # print("[*] Generate access Token : ", kite.login_url())
        data = kite.generate_session(request_tkn, api_secret=api_s)
        kite.set_access_token(data["access_token"])
        access_token = data['access_token']

    # def start(update, context):
    #     context.bot.send_message(chat_id=update.effective_chat.id, text="Mr Ronit not available, please talk to me!")
    def start(update, context):
        # context.bot.send_message(chat_id="@algobrainTrade", text="debugging")
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Mr Ronit not available, please talk to me!")
        print(update.effective_chat.id)

    def set_token(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Permission to only Mr Ronit Jain, you can talk to me")

    def update_api(update, context):
        access_token = update.message.text.split()[1]
        print(access_token)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="api key set")

    def echo(update, context):
        reply = gizoogle.text(update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

    class Api_filter(BaseFilter):
        def filter(self, message):
            return 'api' in message.text or 'Api' in message.text
    # Remember to initialize the class.
    api_filter = Api_filter()

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    token_handler = CommandHandler('set_token', set_token)
    dispatcher.add_handler(token_handler)

    api_handler = MessageHandler(api_filter, update_api)
    dispatcher.add_handler(api_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
