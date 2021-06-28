from match import Match


class Round:

    def __init__(self, round_number: int, number_of_players: int, matchs: dict = None):
        errors = []
        try:
            self.round_number = round_number
        except AttributeError as e:
            errors.append(("round_number", str(e)))
        try:
            self.number_of_players = number_of_players
        except AttributeError as e:
            errors.append(("number_of_players", str(e)))
        try:
            self.number_of_matchs = int(number_of_players / 2)
        except AttributeError as e:
            errors.append(("number_of_matchs", str(e)))
        try:
            self.matchs = matchs
        except AttributeError as e:
            errors.append(("matchs", str(e)))
        try:
            self.name = round_number
        except AttributeError as e:
            errors.append(("name", str(e)))
        try:
            self.ID_tuple = []
        except AttributeError as e:
            errors.append(("ID_tuple", str(e)))
        if errors:
            raise Exception(errors)

    @property
    def round_number(self) -> int:
        return self.__round_number

    @round_number.setter
    def round_number(self, value: int):
        if (isinstance(value, int) and value > 0):
            self.__round_number = value
        else:
            raise AttributeError("Le numéro de tour doit être un nombre entier positif")

    @property
    def number_of_players(self) -> int:
        return self.__number_of_players

    @number_of_players.setter
    def number_of_players(self, value: int):
        if (isinstance(value, int) and value > 0):
            self.__number_of_players = value
        else:
            raise AttributeError("Le nombre de joueurs doit être un nombre entier positif")

    @property
    def number_of_matchs(self) -> int:
        return self.__number_of_matchs

    @number_of_matchs.setter
    def number_of_matchs(self, value: int):
        if (isinstance(value, int) and value > 0):
            self.__number_of_matchs = value
        else:
            raise AttributeError("Le nombre de matchs du tour doit être un nombre entier positif")

    @property
    def matchs(self) -> dict:
        return self.__matchs

    @matchs.setter
    def matchs(self, value: dict):
        if value is None:
            self.__matchs = {}
        elif isinstance(value, dict):
            self.__matchs = {}
            for match in value:
                players_values = []
                for player in value[match]:
                    players_values.append(value[match][player]["ID"])
                for player in value[match]:
                    players_values.append(value[match][player]["score"])
                m = Match(*players_values)
                self.__matchs[match] = m
        elif isinstance(value, list):
            self.__matchs = {}
            match_number = 1
            for match in value:
                match_name = ("match{}".format(match_number))
                self.__matchs[match_name] = match
                match_number += 1
        else:
            raise AttributeError("Le nombre de matchs du tour doit être un nombre entier positif")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: int):
        if (isinstance(value, int)):
            self.__name = "round{}".format(str(value))
        else:
            raise AttributeError("Le numéro de tour doit être un nombre entier positif")
