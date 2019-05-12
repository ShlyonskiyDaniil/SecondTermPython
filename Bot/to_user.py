from parsing import Parser, get_html


def in_required(choosed, required):
        for item in required:
            if (choosed.upper() == list(item)[0].upper() or
                 choosed.upper() in list(item)[0].upper()[:10]):
                return True

def place_to_link(places, required_place):
    print(f'places is {places}')
    print('#' * 20)
    print(f'required is {required_place}')
    for place in places:
        if (required_place.upper() == list(place.keys())[0].upper()):
            print('equal')
            print(list(place.keys())[0])
            return place[list(place.keys())[0]]
        elif required_place.upper() in list(place.keys())[0].upper()[:10] and len(required_place) > 2:
            print('in')
            print(list(place.keys())[0])
            return place[list(place.keys())[0]]
    return 'There is no such a place!'

# #  Я хочу:
# Получить букву - выдать регионы.
# Получить название региона, получить первую букву города - выдать города.
# Получить название города - выдать weather pattern. 
class User_talk(object):
    def __init__(self):
        self.parser = Parser()
        self.required_regions = None
        self.required_towns = None
        self.choosed_region = None
        self.choosed_town = None

    def letter_to_regions(self, region_letter):
        all_regions = self.parser.parse_places(get_html(self.parser.URL))
        self.required_regions = all_regions[region_letter]

        for key in self.required_regions:
            print(list(key.keys())[0])


    def region_to_towns(self, choosed_region, town_letter):
        region_url = str()

        while not in_required(self.choosed_region, self.required_regions):
            self.choosed_region = input('Choose your region: ')
            if self.choosed_region == 'exit':
                break

        region_url = place_to_link(self.required_regions, self.choosed_region)
        all_towns = self.parser.parse_places(get_html(region_url))

        self.required_towns = all_towns[town_letter]
        # print(required_towns)

        for key in self.required_towns:
            print(key.keys())
        
    def date_to_weather(self):
        town_url = place_to_link(self.required_towns, self.choosed_town)
        return self.parser.possible_dates(get_html(town_url))

    def town_to_weather(self, date):
        town_url = str()

        while not in_required(self.choosed_town, self.required_towns):
            self.choosed_town = input('Choose your town: ')
            if self.choosed_town == 'exit':
                break

        town_url = place_to_link(self.required_towns, self.choosed_town)
        return self.parser.parse_weather(date, get_html(town_url))



# ut = User_talk()

# region_letter = input('Write the first letter of you region: ')
# ut.letter_to_regions(region_letter)

# choosed_region = input('Choose your region: ')
# town_letter = input('Write the first letter of your town: ')
# ut.region_to_towns(choosed_region, town_letter)

# choosed_town= input('Choose your town: ')
# ut.town_to_weather(choosed_town)
