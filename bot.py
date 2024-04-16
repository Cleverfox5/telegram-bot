import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('token') #the token of your telegram bot

@bot.message_handler(commands=['start', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f"<b>Здравствуйте, {message.chat.first_name}!!!</b>", parse_mode="Html")

@bot.message_handler(commands=['website', 'site'])
def site(message):
    webbrowser.open('https://pypi.org/project/pyTelegramBotAPI/')

@bot.message_handler(commands=['about_me'])
def about_me_function(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    #создание кнопки
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Удалить фото", callback_data="delete")#Указываем, какую функцию вызываем в обработчике
    btn3 = types.InlineKeyboardButton("Нажми!!!!", callback_data="edit")
    markup.row(btn2, btn3)#добавление кнопок в строку
    #создание кнопки с авто-размещением
    #markup.add(types.InlineKeyboardButton("Перейти на сайт", url='https://google.com'))
    bot.reply_to(message, "ВААААААА, красивое!!!!", reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)#обработчик нажатия кнопки
def callback_massage(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)#Удаляем предпоследнее сообщение в чате
    elif callback.data == "edit":
        bot.edit_message_text("я гей", callback.message.chat.id, callback.message.message_id)

@bot.message_handler()
def repeat_function(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, message.text) #...lower() - приводит введённый текст к нижнему регистру
    else:
        bot.send_message(message.chat.id, "Нормально общайся")

bot.polling(non_stop= True)