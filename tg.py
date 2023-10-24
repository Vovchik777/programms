from bot.bot import Bot
from bot.handler import MessageHandler, BotButtonCommandHandler
import json
import random

ran_num = random.randint(1, 100)
ran_num = str(ran_num)

TOKEN = "5779612331:AAHX8l4VPBE9MQb9fGuc8iXz9wJrdCrkz50"
bot = Bot(token=TOKEN)

def bot_play_text(bot, event):
    if event.data["text"] == "/start":
        bot.send_text(chat_id=event.from_chat, text="Привет! Я бот для игры в угадай число. Начнём?",
                      inline_keyboard_markup="{}".format(json.dumps([[
                                                                    {"text":"Начать", "callbackData":"call_btn_id_1", "style":"attention"}]])))

def num_play(bot, event):
    if event.data["text"] == ran_num:
        bot.send_text(chat_id=event.from_chat, text="Да, вы справились")
    elif event.data["text"] > ran_num:
        bot.send_text(chat_id=event.from_chat, text="Загаданное число меньше.")
    elif event.data["text"] < ran_num:
        bot.send_text(chat_id=event.from_chat, text="Загаданное число больше.")

def bot_play(bot, event):
    if event.data["callbackData"] == "call_btn_id_1":
        bot.send_text(chat_id=event.from_chat, text="Я загадал число от 1 до 99, количество попыток: неограниченно.")
        bot.send_text(chat_id=event.from_chat, text="Ваше предположение?")

bot.dispatcher.add_handler(MessageHandler(callback=bot_play_text))
bot.dispatcher.add_handler(MessageHandler(callback=num_play))
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=bot_play))
bot.start_polling()
bot.idle()




















































#'5779612331:AAHX8l4VPBE9MQb9fGuc8iXz9wJrdCrkz50'