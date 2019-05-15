from parsing import Parser, get_html

def in_required(choosed, required):
        for item in required:
            if (choosed.upper() == list(item)[0].upper() or
                 choosed.upper() in list(item)[0].upper()[:10]):
                return True

def place_to_link(places, required_place):
    for place in places:
        if (required_place.upper() == list(place.keys())[0].upper()):
            return place[list(place.keys())[0]]
        elif required_place.upper() in list(place.keys())[0].upper()[:10] and len(required_place) > 2:
            return place[list(place.keys())[0]]
    return 'There is no such a place!'

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

    def region_to_towns(self, choosed_region, town_letter):
        region_url = str()

        region_url = place_to_link(self.required_regions, self.choosed_region)
        all_towns = self.parser.parse_places(get_html(region_url))

        self.required_towns = all_towns[town_letter

    def date_to_weather(self):
        town_url = place_to_link(self.required_towns, self.choosed_town)
        return self.parser.possible_dates(get_html(town_url))

    def town_to_weather(self, date):
        town_url = str()

        town_url = place_to_link(self.required_towns, self.choosed_town)
        return self.parser.parse_weather(date, get_html(town_url))

