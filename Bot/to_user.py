from parsing import Parser


class User_talk(object):
    """Class for requires processing"""

    def __init__(self):
        """Init instance."""

        self.parser = Parser()
        self.required_regions = None
        self.required_towns = None
        self.choosed_region = None
        self.choosed_town = None

    def place_to_link(self, places, required_place):
        """Returns place link.

        Argumetns:
            places(list): possible places to choose;
            required_place(string): choosed places by user.
        """

        for place in places:
            if (required_place.upper() == list(place.keys())[0].upper()):
                return place[list(place.keys())[0]]
            elif required_place.upper() in list(
                    place.keys())[0].upper()[:10] and len(required_place) > 2:
                return place[list(place.keys())[0]]
        return 'There is no such a place!'

    def letter_to_regions(self, region_letter):
        """Put regions, that are possible to choose,
           which starts with this first letter, into required_regions.

        Argumetns:
            region_letter(string): first letter of required region.
        """

        all_regions = self.parser.parse_places(
            self.parser.get_html(self.parser.URL))
        self.required_regions = all_regions[region_letter]

    def region_to_towns(self, choosed_region, town_letter):
        """Puts town, that is possible to choose, into self.required_town.

        Argumetns:
            choosed_region(string): choosed region by user;
            town_letter(string): first letter of required town.
        """

        region_url = self.place_to_link(self.required_regions,
                                        self.choosed_region)
        all_towns = self.parser.parse_places(self.parser.get_html(region_url))

        self.required_towns = all_towns[town_letter]

    def date_to_weather(self):
        """Returns dates, that are possible to choose."""

        town_url = self.place_to_link(self.required_towns, self.choosed_town)
        return self.parser.possible_dates(self.parser.get_html(town_url))

    def town_to_weather(self, date):
        town_url = self.place_to_link(self.required_towns, self.choosed_town)
        return self.parser.parse_weather(date, self.parser.get_html(town_url))
