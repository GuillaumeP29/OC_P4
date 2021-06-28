import datetime
import re
import enum
from typing import Union
from itertools import combinations
from player_manager import player_manager
from round import Round


class Tournament:

    class TimeControl(enum.Enum):
        Bullet = "Bullet"
        Blitz = "Blitz"
        Coup_rapide = "Coup rapide"

    def __init__(
        self, name: str, location: str, date: str, time_control: str, description: str,
        number_of_players: int, number_of_rounds: int = 4, ID: int = None, players: list = None, rounds: dict = None
    ):
            self.name = name
            self.location = location
            self.date = date
            self.time_control = time_control
            self.description = description
            self.number_of_players = number_of_players
            self.number_of_rounds = number_of_rounds
            self.ID = ID
            self.matchs_combinations = []
            self.players = players
            self.rounds = rounds

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if (isinstance(value, str) and re.match(r'^[0-9a-zA-Z- àéèçîôâûùäëïüö]{2,100}$', value)):
            self.__name = value
        else:
            raise AttributeError("Veuillez rentrer une chaîne de caractères")

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        if (isinstance(value, str) and re.match(r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,50}$', value)):
            self.__location = value
        else:
            raise AttributeError("Veuillez rentrer une chaîne de caractères")

    @property
    def date(self) -> Union[str, datetime.date]:
        return self.__date

    @date.setter
    def date(self, value: Union[str, datetime.date]):
        if isinstance(value, str):
            try:
                self.__date = datetime.date.fromisoformat(value)
            except AttributeError as e:
                raise AttributeError(str(e))
        elif isinstance(value, datetime.date):
            self.__date = value
        else:
            raise AttributeError("Veuillez entrer une date selon le format suivant : AAAA-MM-JJ : ")

    @property
    def time_control(self) -> TimeControl:
        return self.__time_control

    @time_control.setter
    def time_control(self, value: Union[str, TimeControl]):
        if (value == "Bullet" or value == "Blitz" or value == "Coup rapide"):
            self.__time_control = value
        else:
            raise AttributeError("Veuillez entrer une des trois valeurs suivantes : Bullet, Blitz ou Coup rapide")

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if (isinstance(value, str) and re.match(r'^[0-9a-zA-Z- àéèçîôâûùäëïüö]{2,250}$', value)):
            self.__description = value
        else:
            raise AttributeError("Veuillez rentrer une chaîne de caractères")

    @property
    def number_of_players(self) -> int:
        return self.__number_of_players

    @number_of_players.setter
    def number_of_players(self, value: int):
        if isinstance(value, int):
            if value > 0:
                self.__number_of_players = value
            else:
                raise AttributeError("Le nombre de joueurs ne doit pas être un entier négatif")
        else:
            raise AttributeError("Le nombre de joueurs devrait être un nombre entier supérieur à 0")

    @property
    def number_of_rounds(self) -> int:
        return self.__number_of_rounds

    @number_of_rounds.setter
    def number_of_rounds(self, value: int):
        if isinstance(value, int):
            if value > 0:
                self.__number_of_rounds = value
            else:
                raise AttributeError("Le nombre de tours ne doit pas être un entier négatif")
        else:
            raise AttributeError("Le nombre de tours devrait être un nombre entier supérieur à 0")

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, value: str):
        if value is None:
            name = self.name.replace(" ", "")
            value = "{}/{}/{}".format(name, self.location, self.date)
            self.__ID = value
        elif isinstance(value, str):
            self.__ID = value
        else:
            raise AttributeError("L'identifiant devrait être une chaîne de caractères")

    @property
    def players(self) -> list:
        return self.__players

    @players.setter
    def players(self, value: list):
        if not value:
            value = []  # mettre le self.__players = value à la fin
        elif isinstance(value, list):
            if isinstance(value[0], dict):  # rajouter un for pour vérifier chaque valeur et pas seulement la [0]
                players = []
                for player in value:
                    players.append(player)
                value = players
            else:
                players = []
                for ID in value:
                    players.append(player_manager.load_player(ID))
                value = players
        else:
            raise AttributeError("La liste de joueurs du tournois doit être une liste de dictionnaire")
        self.__players = value
        if self.matchs_combinations == []:
            self.matchs_combinations = self.players

    @property
    def rounds(self) -> dict:
        return self.__rounds

    @rounds.setter
    def rounds(self, value: dict):
        self.__rounds = {}
        if value is None:
            value = {}
            self.__rounds = value
        elif isinstance(value, dict):
            self.__rounds = {}
            round_number = 1
            for rd in value:
                round = Round(round_number, self.number_of_players, value[rd])
                self.__rounds[rd] = round
                round_number += 1
        else:
            raise AttributeError("La liste de joueurs du tournois doit être sous forme de dictionnaire")

    @property
    def scores(self) -> dict:
        return self.__scores

    @scores.setter
    def scores(self, value: dict):
        if value is None:
            value = {}
            self.__scores = value
        elif isinstance(value, dict):
            self.__scores = value
        else:
            raise AttributeError("La liste de joueurs du tournois doit être sous forme de dictionnaire")

    @property
    def matchs_combinations(self) -> list:
        return self.__matchs_combinations

    @matchs_combinations.setter
    def matchs_combinations(self, value: list):
        if isinstance(value, list):
            if value == []:
                self.__matchs_combinations = value
            elif value == self.players:
                ID_list = []
                for player in self.players:
                    ID_list.append(player["ID"])
                self.__matchs_combinations = list(combinations(ID_list, 2))
            else:
                self.__matchs_combinations = value
        else:
            raise AttributeError("Les combinaisons du matchs doivent être envoyées dans une liste")

    def create_round(self, round_number: int):
        pass

    def set_scores(self, scores: list):
        pass

    def serialize(self) -> dict:
        return {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "time control": self.time_control,
                "description": self.description,
                "number_of_players": self.number_of_players,
                "number_of_rounds": self.number_of_rounds,
                "ID": self.ID,
                "players": self.players,
                "rounds": self.rounds
        }