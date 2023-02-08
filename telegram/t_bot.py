import telebot

token = "6280256013:AAFxiErfho7BYdIwMp7gXva1xgacj4vlW60"

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку по программе.
/add - добавить задачу в список ( название задачи запрошиваем у пользователя).
/show -напечатать все добавленные задачи.
/random - добавлять случайную задачу на дату Сегодня"""

tasks = {}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
