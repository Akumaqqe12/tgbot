import sqlite3
import telebot
from dotenv import dotenv_values
config = dotenv_values('.env')


bot = telebot.TeleBot(config["TELELALALA__LDLDLD"])
print("bot is running")

# помощь
@bot.message_handler(commands = ['start' , 'help'])
def zzzxxxcc(message):
    connection = sqlite3.connect(config['DB_NAME'])
    cursor = connection.cursor()
    cursor.execute('SELECT count(*) FROM superhero')
    data = cursor.fetchall()
    connection.close()

    bot.send_message(message.chat.id, f'У меня имеется инфа по {data[0][0]} рофлерам')

# лялял комманды для добра :3
@bot.message_handler(commands = ['good'])
def fldk(message):
    connection = sqlite3.connect(config['DB_NAME'])
    cursor = connection.cursor()
    cursor.execute('SELECT count(*) FROM superhero WHERE alignment_id = 1')
    data = cursor.fetchall()
    connection.close()

    bot.send_message(message.chat.id, f'У нас есть {data[0][0]} добряков')

# лялял комманды для добра :3
@bot.message_handler(commands = ['evil'])
def fldk(message):
    connection = sqlite3.connect(config['DB_NAME'])
    cursor = connection.cursor()
    cursor.execute('SELECT count(*) FROM superhero WHERE alignment_id = 2')
    data = cursor.fetchall()
    connection.close()

    bot.send_message(message.chat.id, f'У нас есть {data[0][0]} злодеев')

# хз зачем
@bot.message_handler(content_types = ['text'])
def lalalal(message):
    print(f'Юзер{message.from_user.first_name} id = {message.chat.id}: {message.text}')
    bot.send_message(message.chat.id, "Manera piet kefir " + "" + message.text)


bot.polling(none_stop = True)
