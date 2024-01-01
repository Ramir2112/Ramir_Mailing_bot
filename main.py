import telebot
import os
from telebot import types

bot = telebot.TeleBot("6460276264:AAGmrcwuj__CF9Vb_zZucsvHWwG35nOvIWg")

joinedfile = open('C:/Users/Ramir/Desktop/Работа/Python/Ramirbot/join.txt', "r")
joinedUsers = set()
for line in joinedfile:
    joinedUsers.add(line.strip())
joinedfile.close()

@bot.message_handler(commands=['start'])
def startjoin(message):
    if not  str(message.chat.id) in joinedUsers:
        joinedfile = open('C:/Users/Ramir/Desktop/Работа/Python/Ramirbot/join.txt', "a")
        joinedfile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)
    bot.send_message(message.chat.id, "Добро пожаловать! Вы подписались на рассылку❤ Бота писал сам @RAMIR_ERROR на языке Python. Так же подписывайтесь на моё сообщество ВКонтакте")


@bot.message_handler(commands=['ramirsend'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

if __name__ == '__main__':
     bot.polling(none_stop=True)