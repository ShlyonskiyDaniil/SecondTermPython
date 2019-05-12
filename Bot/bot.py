from to_user import User_talk, place_to_link
import telebot 

TOKEN = "800215378:AAGi8Ro-VDRBpvsviZL8Bkviu64ic3W6bwM"
telebot.apihelper.proxy = {'https':'socks5://144.217.163.138'}
STOP_DATE = True
STOP_REGION = True

bot = telebot.TeleBot(TOKEN)

ut = User_talk()

def keyboard():
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button = 'Погода.'
        markup.add(button)
        return markup

def make_places_button(message, ut, question, place):
        place_letter = message.text.upper()
        if place == 'region':
                get_places = ut.letter_to_regions(place_letter)
        elif place == 'town':
                ut.region_to_towns(ut.choosed_region, place_letter)

        keyboard = telebot.types.InlineKeyboardMarkup()

        place_keys = list()
        required_places = getattr(ut, 'required_' + place + 's')
        for place in required_places:
                place_key = telebot.types.InlineKeyboardButton(text=list(place.keys())[0], callback_data=list(place.keys())[0][:3]); 
                place_keys.append(place_key)
                
        keyboard.add(*place_keys)
        bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def bot_start(message):
        print('bot_start')
        bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=keyboard())

@bot.message_handler(content_types=['text'])
def start(message):
        global STOP_DATE, STOP_REGION
        print('start')
        if message.text == 'Погода.':
                STOP_DATE = True
                STOP_REGION= True
                bot.send_message(message.from_user.id, 'Введите первую букву вашего региона: ', reply_markup=keyboard())
                bot.register_next_step_handler(message, get_region)
        elif message.text == '/help':
                bot.send_message(message.from_user.id, 'Хотите узнать погоду?\nВведите слово "Погода."', reply_markup=keyboard())
        else:
                bot.send_message(message.from_user.id, 'Я Вас не понимаю, напишите, пожалуйста, "/help".', reply_markup=keyboard())

def get_region(message):
        print('get_region')
        question = 'Выберите Ваш регион: '
        make_places_button(message, ut, question, 'region')

@bot.callback_query_handler(func=lambda call: STOP_REGION)
def get_town_letter(call):
        print('get_town_letter')
        global STOP_REGION

        for elem in ut.required_regions:
                tmp = list(elem.keys())[0]
                if tmp.startswith(call.data):
                        ut.choosed_region = tmp
                        break

        bot.send_message(call.message.chat.id, "Введите название Вашего города.")
        STOP_REGION = False
        bot.register_next_step_handler(call.message, suggest_date)

def suggest_date(message):
        print('suggest_date')
        ut.choosed_town = message.text
        ut.region_to_towns(ut.choosed_region, ut.choosed_town.upper()[0])
        # print('suggest_date')
        # print(ut.choosed_town)
        # print(place_to_link(ut.required_regions, ut.choosed_region))
        if place_to_link(ut.required_towns, ut.choosed_town) == 'There is no such a place!':
                print("I WAS HERE")
                question = 'Извините, у меня не такого города!\nВведите название Вашего города.'
                bot.send_message(message.chat.id, question)
                bot.register_next_step_handler(message, suggest_date)
        else:
                keyboard = telebot.types.InlineKeyboardMarkup()

                date_keys = list()
                for elem in ut.date_to_weather():
                        date_key = telebot.types.InlineKeyboardButton(text=elem, callback_data=elem[:4]); 
                        date_keys.append(date_key)

                keyboard.add(*date_keys)

                question = 'Выберите дату!'
                bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def get_weather(call):
        print('get_weather')
        date = str()
        for elem in ut.date_to_weather():
                if elem.startswith(call.data):
                        date = elem
                        break
        day = ut.town_to_weather(date)

        result = date + '\n\n'
        print('VERY IMPORTANT:')
        print(day)
        for elem in day:
                word = list(elem.keys())[0]
                result += '{}: {}\n'.format(word, elem[word])
        bot.send_message(call.message.chat.id, result, reply_markup=keyboard())

bot.polling()