import telebot
from confg import Token
from logic import Film 

bot = telebot.TeleBot(Token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Я могу тебе по рекомендовать фильми просто пиши факт и я найду!
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message): 
    bot.send_chat_action(message.chat.id, 'typing')
    film = Film()
    text = message.text
    films = film.Ai_start(text)
    bot.reply_to(message, films)
   

@bot.message_handler(commands=['random'])
def echo_message(message): 
    bot.send_chat_action(message.chat.id, 'typing')
    film = Film()
    text = "пришли случайные фильмы"
    films = film.Ai_start(text)
    bot.reply_to(message, films)

@bot.message_handler(commands=['popular'])
def echo_message(message): 
    bot.send_chat_action(message.chat.id, 'typing')
    film = Film()
    text = "пришли самые популярные фильмы"
    films = film.Ai_start(text)
    bot.reply_to(message, films) 



@bot.message_handler(commands=['actor'])
def echo_message(message): 
    bot.send_chat_action(message.chat.id, 'typing')
    text = message.text
    txt = text.split("/actor" )[1]
    film = Film()
    text = "Дай фильм с этими акторамы :" + txt 
    films = film.Ai_start(text)
    bot.reply_to(message, films)  


@bot.message_handler(commands=['director'])
def echo_message(message): 
    bot.send_chat_action(message.chat.id, 'typing')
    text = message.text
    txt = text.split("/director" )[1]
    film = Film()
    text = "Дай фильм с этими режисерам :" + txt 
    films = film.Ai_start(text)
    bot.reply_to(message, films) 



bot.infinity_polling()