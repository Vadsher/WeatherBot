#  Simple Telegram Bot
# --------------------------------------------- #
# Program by Vadim S.							#
#												#
#												#
# Version	Date		Info					#
# 1.0.0		06.06.2022	Initial vesrion			#
#												#
#												#
# --------------------------------------------- #

import telebot
from pyowm.owm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ua'

owm = OWM('e954cef3febcc4afdda0570b8d95e785')
mgr = owm.weather_manager()
bot = telebot.TeleBot("5402772676:AAGS2X3Eyr3hEO7gbX-UgJyrIWrrp7YKkmk", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing? Enter a city name to get some weather details. \n\nСлава Україні! Введи назву міста, щоб отримати інформацію про погоду.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "I can search for current weather the city you specified and get some details")

@bot.message_handler(content_types=['text'])
def send_message(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	t = w.temperature('celsius')['temp']

	answer = "В місті " + message.text + " зараз " + w.detailed_status + ".\n"
	answer += "Температура за бортом становить приблизно " + str(t) + "°С.\n\n"
	answer += "Доречі, моя порада, \n"

	if t < 0:
		answer += "сьогодні буде холодно, швидко повернувлся і вдягнув шапку!"
	if t < 10:
		answer += "щось сьогодні холодно, одягнись тепліше!"
	elif t < 18:
		answer += "на вулиці прохолодно, куртка не завадить."
	else:
		answer += "літо на дворі, одягай що хочеш!"

	bot.send_message(message.chat.id, answer)






bot.infinity_polling()