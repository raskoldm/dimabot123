import dima
import telebot
import urllib.request as urlib2

token = dima.token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', '/stop')
    user_markup.row('/посомтреть как выглядит красавчик')
    user_markup.row('/оценить насколько вы красавчик')
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '/посомтреть как выглядит красавчик':
        url = "https://24smi.org/public/media/235x307/celebrity/2017/02/14/VTbS2hRAEwfe_vladimir-putin.jpg"
        urlib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    if message.text == '/оценить насколько вы красавчик':
        bot.send_message(message.chat.id, 'Вы не красивый, досвидания!')



bot.polling(none_stop=True,interval=0)