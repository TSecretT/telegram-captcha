import sys
sys.path.append('.')

from main import currentCaptchas, send_captcha, handle_message, generate_string

class Chat:
    id: int = 12345

class Message:
    def __init__(self) -> None:
        self.chat = Chat()
        self.text: str = 'asdfg'

class Bot:
    
    def send_photo(self, chat, photo, caption):
        return

    def send_message(self, chat, message):
        reply = Message()
        reply.text = message
        return reply


bot = Bot()

def test_string_generation():
    assert len(generate_string()) == 6
    assert len(generate_string(N=10)) == 10
    assert isinstance(generate_string(), str)

def test_first_message():
    message = Message()
    send_captcha(message, bot=bot)
    assert message.chat.id in currentCaptchas

def test_reply_captcha_incorrect():
    message = Message()
    message.text = ''
    reply = handle_message(message, bot)
    assert reply.text == 'Incorrect'
    assert message.chat.id in currentCaptchas

def test_reply_captcha_correct():
    message = Message()
    message.text = currentCaptchas[message.chat.id]
    reply = handle_message(message, bot)
    assert reply.text == 'Correct'
    assert message.chat.id not in currentCaptchas