
import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

from main import(
    start,
    algebra,
    geometriya,
    kanallar,
    guruh
)

app=Flask((__name__))

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
@app.route('/webhook', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return {'status': 200}

    elif request.method == 'POST':
        # get data from request
        data: dict = request.get_json(force=True)

        # convert data to Update obj
        update: Update = Update.de_json(data, bot)

        # Dispatcher
        dp: Dispatcher = Dispatcher(bot, None, workers=0)

        # handlers
        dp.add_handler(CommandHandler('start',start))
        # Add handler for photo message
       # dp.add_handler(MessageHandler(Filters.photo,photo))
        dp.add_handler(MessageHandler(Filters.text('Algebra'),algebra))
        dp.add_handler(MessageHandler(Filters.text('Geometriya'),geometriya))
        dp.add_handler(MessageHandler(Filters.text('Kanallar'),kanallar))
        dp.add_handler(MessageHandler(Filters.text('Main menu'),start))
        dp.add_handler(MessageHandler(Filters.text("Guruhga Qo'shish"),guruh))
        #dp.add_handler(CallbackQueryHandler(phone_list,pattern='phone_list'))
      #  dp.add_handler(CallbackQueryHandler(phone,pattern='phone'))
       # dp.add_handler(CallbackQueryHandler(add_cart,pattern='add_cart'))
        #dp.add_handler(CallbackQueryHandler(query))

        # process update
        dp.process_update(update=update)

        return {'status': 200}

bot=Bot(TOKEN)

#print(bot.set_webhook('https://Turklitseybot.pythonanywhere.com/webhook'))
#print(bot.delete_webhook())
print(bot.get_webhook_info())