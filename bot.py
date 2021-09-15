import telebot
from telebot import types

name = ''
surname = ''
age = 0

bot = telebot.TeleBot("Введите ваш токен на место этого сообщения!")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуй! Я бот-помошник команды ...! Добро пожаловать! Выбери интересующий тебя вопрос.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == 'Привет':
		bot.reply_to(message, "Привет, партнер!")
	elif message.text == 'Hi':
		bot.reply_to(message, "Hi, partner!")
	elif message.text == '/reg':
		bot.send_message(message.from_user.id, "Давай знакомиться! Как тебя зовут?")
		bot.register_next_step_handler(message, reg_name)
# bot.reply_to(message, message.text)

def reg_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
	bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
	global surname
	surname = message.text
	bot.send_message(message.from_user.id, "Сколько тебе лет?")
	bot.register_next_step_handler(message, reg_age)

def reg_age(message):
	global age
	# age = message.text
	while age == 0:
		try:
			age = int(message.text)
		except Exception:
			bot.send_message(message.from_user.id, "Введите ваш возраст цифрами!")

	keyboard = types.InlineKeyboardMarkup()
	key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
	keyboard.add(key_yes)
	key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
	keyboard.add(key_no)
	question = ("Тебя " + str(age) + ' лет? И тебя зовут: ' + name + ' ' + surname + '?')
	bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "yes":
		bot.send_message(call.message.chat.id, 'Приятно познакомиться! Запишу данные в БД!')
	elif call.data == "no":
		bot.send_message(call.message.chat.id, 'Давай введем данные еще раз!')
		bot.send_message(call.message.chat.id, "Давай знакомиться! Как тебя зовут?")
		bot.register_next_step_handler(call.message, reg_name)

bot.polling()