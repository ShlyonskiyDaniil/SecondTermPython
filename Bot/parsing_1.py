import urllib.request as req
from bs4 import BeautifulSoup

def add_method(cls):
    def decorator(func):
        @wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        return func
    return decorator

def get_html(url):
        response = req.urlopen(url)
        return response.read()


class Parser(object):
    def __init__(self):
        self.URL = 'https://yandex.ru/pogoda/region/225'
        self.PREFIX = 'https://yandex.ru'

    def towns_to_links(self, alpha_list, alpha):
        town_link_part = alpha.find_all('a', class_="link link_theme_normal place-list__item-name i-bem")
        for elem in town_link_part:
            town = elem.text
            link = self.PREFIX + elem['href']
            alpha_list.append({town: link})

    def parse_places(self, html):
        all_cities = dict()

        soup = BeautifulSoup(html)
        main_page = soup.find('div', class_='content')
        alpha_header = main_page.find_all('div', class_='place-list')

        for alpha in alpha_header:
            letter = alpha.find('h2', class_='title title_level_2 place-list__letter').text
            if letter not in all_cities.keys():
                all_cities[letter] = list()
            
            self.towns_to_links(all_cities[letter], alpha)

        return all_cities

    def possible_dates(self, weather_html):
        data = dict()
        soup = BeautifulSoup(weather_html)

        main_page = soup.find('div', class_='forecast-briefly__days')

        template_columns = main_page.find_all('a')

        dates = list()
        for data_part in template_columns:
            dates.append(data_part.find('time', class_='time forecast-briefly__date').text)
        
        return dates

    def parse_weather(self, date, weather_html):
        data = dict()
        soup = BeautifulSoup(weather_html)

        main_page = soup.find('div', class_='forecast-briefly__days')

        weather_columns = main_page.find_all('a')

        dates = self.possible_dates(weather_html)
        dates_counter = 0
        for data_part in weather_columns:
            day = data_part.find('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day')
            data[dates[dates_counter]] = [{'day': day.find('span', class_='temp__value').text}]

            night = data_part.find('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night')
            data[dates[dates_counter]].append({'night': night.find('span', class_='temp__value').text})

            weather_condition = data_part.find('div', class_='forecast-briefly__condition')
            data[dates[dates_counter]].append({'condition': weather_condition.text})
            dates_counter += 1

        if date in dates:
            return data[date]
        else:
            return data
