import telebot
from telebot.types import Message
from os import environ
from dotenv import load_dotenv
from captcha.image import ImageCaptcha
import random
import string

load_dotenv()

BOT_TOKEN = environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

currentCaptchas = {}

def generate_string(N=6):
    letters = string.ascii_lowercase
    return''.join(random.choice(letters) for i in range(N))

@bot.message_handler(commands=['start', 'help'])
def send_captcha(message: Message, bot=bot):
    global currentCaptchas

    captcha = ImageCaptcha()
    result = generate_string()
    image = captcha.generate(result)
    currentCaptchas[message.chat.id] = result
    return bot.send_photo(message.chat.id, photo=image, caption='Please enter captcha')

@bot.message_handler(func=lambda message: True)
def handle_message(message: Message, bot=bot):
    global currentCaptchas

    if message.chat.id not in currentCaptchas:
        return send_captcha(message)

    if message.text.lower() == currentCaptchas[message.chat.id]:
        del currentCaptchas[message.chat.id]
        return bot.send_message(message.chat.id, 'Correct')
    else:
        return bot.send_message(message.chat.id, 'Incorrect')

if __name__ == '__main__':
    bot.infinity_polling()