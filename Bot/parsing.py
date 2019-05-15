import urllib.request as req
from bs4 import BeautifulSoup


class Parser(object):
    """Class for parsing site with weather."""
    def __init__(self):
        """Init instance."""

        self.URL = 'https://yandex.ru/pogoda/region/225'
        self.PREFIX = 'https://yandex.ru'

    def get_html(self, url):
        """Returns html script.

        Argumetns:
            url(string): url.
        """

        response = req.urlopen(url)
        return response.read()

    def place_to_links(self, alpha_list, alpha):
        """Fills alpha_place list.

        Argumetns:
            alpha_list(list): list, containing dict(town to url);
            alpha: part of html code, which contains places,
                   that starts with "alpha" letter.
        """

        cstr = 'link link_theme_normal place-list__item-name i-bem'
        town_link_part = alpha.find_all('a', class_=cstr)

        for elem in town_link_part:
            town = elem.text
            link = self.PREFIX + elem['href']
            alpha_list.append({town: link})

    def parse_places(self, html):
        """Returns dict(letter to list(dict(place to url)))

        Argumetns:
            html(string): html script.
        """

        all_cities = dict()

        soup = BeautifulSoup(html)
        main_page = soup.find('div', class_='content')
        alpha_header = main_page.find_all('div', class_='place-list')

        for alpha in alpha_header:
            cstr = 'title title_level_2 place-list__letter'
            letter = alpha.find('h2', class_=cstr).text

            if letter not in all_cities.keys():
                all_cities[letter] = list()

            self.place_to_links(all_cities[letter], alpha)

        return all_cities

    def possible_dates(self, weather_html):
        """Returns date, that are possible to choose.

        Argumetns:
            weather_html(string);
        """

        data = dict()
        soup = BeautifulSoup(weather_html)

        main_page = soup.find('div', class_='forecast-briefly__days')

        template_columns = main_page.find_all('a')

        dates = list()
        for data_part in template_columns:
            cstr = 'time forecast-briefly__date'
            dates.append(data_part.find('time', class_=cstr).text)

        return dates

    def parse_weather(self, date, weather_html):
        """Returns all information about choosed date.

        Argumetns:
            date(string): choosed date;
            weather_html: html of weather part.
        """

        data = dict()
        soup = BeautifulSoup(weather_html)

        main_page = soup.find('div', class_='forecast-briefly__days')

        weather_columns = main_page.find_all('a')

        dates = self.possible_dates(weather_html)
        dates_counter = 0
        for data_part in weather_columns:
            cstr = 'temp forecast-briefly__temp forecast-briefly__temp_day'
            day = data_part.find('div', class_=cstr)

            data[dates[dates_counter]] = [
                {'day': day.find('span', class_='temp__value').text}]

            cstr = 'temp forecast-briefly__temp forecast-briefly__temp_night'
            night = data_part.find('div', class_=cstr)
            data[dates[dates_counter]].append(
                {'night': night.find('span', class_='temp__value').text})

            weather_condition = data_part.find(
                'div', class_='forecast-briefly__condition')
            data[dates[dates_counter]].append(
                {'condition': weather_condition.text})
            dates_counter += 1

        if date in dates:
            return data[date]
