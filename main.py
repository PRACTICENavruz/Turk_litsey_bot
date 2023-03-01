from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os

TOKEN = os.environ['TOKEN']


def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['Algebra ','Geometriya'],
        ['Kanallar',"Guruhga Qo'shish"]
    ]
    )
    bot=context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum sizga Turk litsey yechimilarni qaysi qismi kerak ',
    reply_markup=keyboar
    )

def algebra(update:Update,context:CallbackContext):
    chat_id=update.message.chat_id
    
    keyboar=ReplyKeyboardMarkup([
        ['Main menu'],
        ['Kanallar']
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id,text='https://t.me/turklitsey_geometriya_yechimlari/9',reply_markup=keyboar)

def geometriya(update:Update,context:CallbackContext):
    chat_id=update.message.chat_id
    
    keyboar=ReplyKeyboardMarkup([
        ['Main menu'],
        ['Kanallar']
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id,text='https://t.me/turklitsey_geometriya_yechimlari/6',reply_markup=keyboar)
def guruh(update:Update,context:CallbackContext):
    chat_id=update.message.chat_id
    
    Kanal=InlineKeyboardButton(text="Guruhga Qo'shish",url='https://telegram.me/Turk_litsey_bot?startgroup=start',callback_data='1')
    
    keyboar=InlineKeyboardMarkup([
        [Kanal]
    ])
    bot=context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Turk litsey yechimilar",
    reply_markup=keyboar)
def kanallar(update:Update,context:CallbackContext):
    chat_id=update.message.chat_id
    Kanal3=InlineKeyboardButton(text="Guruhga Qo'shish",url='https://telegram.me/Turk_litsey_bot?startgroup=start',callback_data='1')
    
    Kanal=InlineKeyboardButton(text='Algebra turk litsey',url='https://t.me/Turk_litsey_yechimi',callback_data='1')
    Kanal1=InlineKeyboardButton(text='Geometriya turk litsey ',url='https://t.me/turklitsey_geometriya_yechimlari',callback_data='2')
    Kanal2=InlineKeyboardButton(text='Matematika turk litsey',url='https://t.me/TurkLitseyYechim',callback_data='3')
    keyboar=InlineKeyboardMarkup([
        [Kanal],
        [Kanal2],
        [Kanal1],
        [Kanal3]
    ])
    bot=context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Matematikadan eng zo'r masala va yechimlar\n Kitoblar 📚 \n👌Online testlar🥇\nOnline darslar🏆",
    reply_markup=keyboar)

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
# Add handler for photo message
#updater.dispatcher.add_handler(MessageHandler(Filters.photo,photo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Algebra'),algebra))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Geometriya'),geometriya))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Kanallar'),kanallar))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Guruhga Qo'shish"),guruh))
#updater.dispatcher.add_handler(CallbackQueryHandler(phone_list,pattern='phone_list'))
#updater.dispatcher.add_handler(CallbackQueryHandler(phone,pattern='phone'))
#updater.dispatcher.add_handler(CallbackQueryHandler(query))

updater.start_polling()
updater.idle()
