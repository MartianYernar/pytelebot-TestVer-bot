import telebot 
import config 
import random 

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'Back'])
def welcome(message):
	
	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	item1 = types.KeyboardButton("🎲 Random number")
	item2 = types.KeyboardButton("😌 How are you?")
	item3 = types.KeyboardButton("🪙 Coin")
	item4 = types.KeyboardButton("🎞️ Last films")
	item5 = types.KeyboardButton("📞 Phone number request", request_contact=True)
	item6 = types.KeyboardButton("🌎 Location request", request_location=True)
	item7 = types.KeyboardButton("📱 Phone wallpaper")
	item8 = types.KeyboardButton("🎸 Some music")
	markup.add(item1, item2, item5)
	markup.add(item3, item4, item6)
	markup.add(item7, item8)


	bot.send_message(message.chat.id, "Welcome {0.first_name}, i am going to be your assistant today \n by the way i am from Yernar!?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['location'])
def check_location(message):
	bot.send_message(message.chat.id, message)

@bot.message_handler(content_types=['contact'])
def check_contact(message):
	if message.text == '📞 Phone number request':
		bot.send_message(message.chat.id, message.contact.number_phone)

@bot.message_handler(content_types=['text'])
def lalala(message):

	if message.chat.type == 'private':

	#format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

		if message.text == '🎲 Random number':
			bot.send_message(message.chat.id, str(random.randint(0, 100)))
		elif message.text == '🪙 Coin':
			keyboard = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton(text="head", callback_data="head")
			item2 = types.InlineKeyboardButton(text="tail", callback_data="tail")
			keyboard.add(item1, item2)
			bot.send_message(message.chat.id, "This function may help you to solve certain problem, you can use it for your own goals☯️ \n SO before please choose one of them 'head' or 'tail'🐢", reply_markup=keyboard)
		elif message.text == 'head':
			res = random.randint(0, 1)
			if res == 0:
				bot.send_message(message.chat.id, "Yeah you are correct, Its head 😎")
			elif res == 1:
				bot.send_message(message.chat.id, "NUuhh try again, Its tail 😑")
		elif message.text == 'tail':
			res = random.randint(0, 1)
			if res == 0:
				bot.send_message(message.chat.id, "NUuh try again, its head😑")
			elif res == 1:
				bot.send_message(message.chat.id, "YEah you are correct, Its tail 🤑")
		elif message.text == '🎞️ Last films':
			keyboard = types.InlineKeyboardMarkup(row_width=2)
			url = types.InlineKeyboardButton(text="T I C K E T O N", url="https://ticketon.kz/cinema")
			keyboard.add(url)
			
			bot.send_message(message.chat.id, "Below is the link to the site, where you can find the list of last films🍿", reply_markup=keyboard)
		elif message.text == '🎸 Some music':
			file3 = open('Dead tape.mp3', 'rb')
			bot.send_audio(message.chat.id, file3, 'Dead..')
		elif message.text == "📱 Phone wallpaper":
			file = open('wll1.jpg', 'rb')
			file2 = open('wll2.jpg', 'rb')
			file3 = open('wll3.jpg', 'rb')
			file4 = open('wll4.jpg', 'rb')
			bot.send_photo(message.chat.id, file, 'first one')
			bot.send_photo(message.chat.id, file2, 'second one')
			bot.send_photo(message.chat.id, file3, 'third one')
			bot.send_photo(message.chat.id, file4, 'fourth one')
		elif message.text == '😌 How are you?':
			#keyboard after how are you message
			markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("Great, allright!!🦍")
			item2 = types.KeyboardButton("Actually, bad(🥺🐒")
			item3 = types.KeyboardButton("/Back")
			markup1.row(item1, item2, item3)
		
			
			bot.send_message(message.chat.id, 'Fine, and how do you do?', reply_markup=markup1)
		
		elif message.text == 'Great, allright!!🦍':
			keyboard = types.InlineKeyboardMarkup()
			url = types.InlineKeyboardButton(text="C H I L L  S O N G S", url="https://youtu.be/TaINndH-bZ0")
			keyboard.add(url)

			bot.send_message(message.chat.id, "Super, leshhh gooo🐵🙊🙉 \n Below you can find the chill songs", reply_markup=keyboard)

		elif message.text == 'Actually, bad(🥺🐒':
			keyboard = types.InlineKeyboardMarkup()
			url = types.InlineKeyboardButton(text="R E L A X A T I O N  M U S I C", url="https://youtu.be/_5QPFQ-1XKY")
			keyboard.add(url)
			
			bot.send_message(message.chat.id, "Ohh, you should relax it will be helpful for you))🙈", reply_markup=keyboard)
		

		else:	
			bot.send_message(message.chat.id, 'idk what to type🙃')

@bot.callback_query_handler(func=lambda callback: callback.data)
def inline_query(callback):
	if callback.data == 'head':
		res = random.randint(0, 1)
		if res == 0:
			bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Yeah you are correct, Its head 😎")
		elif res == 1:
			bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="NUuhh try again, Its tail 😑")
	elif callback.data == 'tail':
		res = random.randint(0, 1)
		if res == 0:
			bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="NUuhh try again, Its head 😑")
		elif res == 1:
			bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Yeah you are correct, Its tail🐢")


#run
bot.polling(none_stop=True)


