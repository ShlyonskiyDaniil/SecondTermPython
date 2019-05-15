from to_user import User_talk
import functools
import telebot 


def add_method(cls):
    def decorator(func):
        @functools.wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        return func
    return decorator

TOKEN = "800215378:AAGi8Ro-VDRBpvsviZL8Bkviu64ic3W6bwM"
# telebot.apihelper.proxy = {'https':'socks5://132.148.143.136:2029'}
STOP_DATE = True
STOP_REGION = True
bot = telebot.TeleBot(TOKEN)
ut = User_talk()

@add_method(bot)
def keyboard():
        """Make button with "Погода" text."""
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button = 'Погода.'
        markup.add(button)
        return markup

@add_method(bot)
@bot.message_handler(commands=['start'])
def bot_start(message):
        """Processes start of work with bot.
        
        Attributes:
                message: message from user.
        """
        message_to_user = 'Добро пожаловать!'
        bot.send_message(message.chat.id, message_to_user, reply_markup=keyboard())

@add_method(bot)
@bot.message_handler(content_types=['text'])
def start(message):
        """Processes user message untill finding weather.
        
        Attributes:
                message: message from user.
        """
        global STOP_DATE, STOP_REGION
        if message.text == 'Погода.':
                STOP_DATE = True
                STOP_REGION= True
                message_to_user = 'Введите первую букву вашего региона: '
                bot.send_message(message.from_user.id, message_to_user, reply_markup=keyboard())
                bot.register_next_step_handler(message, get_region)
        elif message.text == '/help':
                message_to_user = 'Хотите узнать погоду?\nВведите слово "Погода."'
                bot.send_message(message.from_user.id, message_to_user, reply_markup=keyboard())

        else:
                message_to_user = 'Я Вас не понимаю, напишите, пожалуйста, "/help".'
                bot.send_message(message.from_user.id, message_to_user, reply_markup=keyboard())

@add_method(bot)
def get_region(message):
        """Fills UserTalk.letter_to_region.
           Returns table with regions, that are possible to choose.
        
        Attributes:
                message: message from user with region first letter.
        """
        region_letter = message.text.upper()

        ut.letter_to_regions(region_letter)
        keyboard = telebot.types.InlineKeyboardMarkup()

        region_keys = list()
        for reqion in ut.required_regions:
                region_key = telebot.types.InlineKeyboardButton(text=list(reqion.keys())[0], callback_data=list(reqion.keys())[0][:3]); 
                region_keys.append(region_key)
                
        keyboard.add(*region_keys)
        message_to_user = 'Выберите Ваш регион:'
        bot.send_message(message.chat.id, text=message_to_user, reply_markup=keyboard)

@add_method(bot)
@bot.callback_query_handler(func=lambda call: STOP_REGION)
def get_town_letter(call):
        """Fills UserTalk.choosed_region. Asks for town.
        
        Attributes:
                call: information gotten after previous function table.
        """
        global STOP_REGION

        for elem in ut.required_regions:
                tmp = list(elem.keys())[0]
                if tmp.startswith(call.data):
                        ut.choosed_region = tmp
                        break

        message_to_user = 'Введите название Вашего города.'
        bot.send_message(call.message.chat.id, message_to_user)
        STOP_REGION = False
        bot.register_next_step_handler(call.message, suggest_date)

@add_method(bot)
def suggest_date(message):
        """Processes gotten in message town.
           Returns:
                1) Table of dates, that are possible to choose.
                2) Ask for town rechoosing, in case of gotten town absence.

        Arguments:
                message: message from user with choosed town.
        """
        ut.choosed_town = message.text
        ut.region_to_towns(ut.choosed_region, ut.choosed_town.upper()[0])
        if ut.place_to_link(ut.required_towns, ut.choosed_town) == 'There is no such a place!':
                message_to_user = 'Извините, у меня не такого города!\nВведите название Вашего города.'
                bot.send_message(message.chat.id, message_to_user)
                bot.register_next_step_handler(message, suggest_date)
        else:
                keyboard = telebot.types.InlineKeyboardMarkup()

                date_keys = list()
                for elem in ut.date_to_weather():
                        date_key = telebot.types.InlineKeyboardButton(text=elem, callback_data=elem[:4]); 
                        date_keys.append(date_key)

                keyboard.add(*date_keys)

                message_to_user = 'Выберите дату!'
                bot.send_message(message.chat.id, text=message_to_user, reply_markup=keyboard)

@add_method(bot)
@bot.callback_query_handler(func=lambda call: True)
def get_weather(call):
        """Processes choosed_date.
           Returns all information about that day weather.
        
        Arguments:
                call: information from user with choosed date.
        """
        date = str()
        for elem in ut.date_to_weather():
                if elem.startswith(call.data):
                        date = elem
                        break
        day = ut.town_to_weather(date)

        result = date + '\n\n'
        for elem in day:
                word = list(elem.keys())[0]
                result += '{}: {}\n'.format(word, elem[word])
        bot.send_message(call.message.chat.id, result, reply_markup=keyboard())

bot.polling(none_stop=True)