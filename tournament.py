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
        self, name: str, location: str, date: str, time_control: Union[TimeControl, str], description: str,
        number_of_players: int, number_of_rounds: int = 4, ID: int = None, players: list = None, rounds: dict = None,
        isover: bool = False
    ):
        errors = []
        try:
            self.name = name
        except AttributeError as e:
            errors.append(("name", str(e)))
        try:
            self.location = location
        except AttributeError as e:
            errors.append(("location", str(e)))
        try:
            self.date = date
        except AttributeError as e:
            errors.append(("date", str(e)))
        try:
            self.time_control = time_control
        except AttributeError as e:
            errors.append(("time_control", str(e)))
        try:
            self.description = description
        except AttributeError as e:
            errors.append(("description", str(e)))
        try:
            self.number_of_players = number_of_players
        except AttributeError as e:
            errors.append(("number_of_players", str(e)))
        try:
            self.number_of_rounds = number_of_rounds
        except AttributeError as e:
            errors.append(("number_of_rounds", str(e)))
        try:
            self.ID = ID
        except AttributeError as e:
            errors.append(("ID", str(e)))
        try:
            self.matchs_combinations = []
        except AttributeError as e:
            errors.append(("matchs_combinations", str(e)))
        try:
            self.rounds = rounds
        except AttributeError as e:
            errors.append(("rounds", str(e)))
        try:
            self.players = players
        except AttributeError as e:
            errors.append(("players", str(e)))
        try:
            self.isover = isover
        except AttributeError as e:
            errors.append(("isover", str(e)))
        if errors:
            raise Exception(errors)

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
            value = []
        elif isinstance(value, list):
            if isinstance(value[0], dict):
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
                if self.rounds is not None:
                    rounds_dict = {}
                    for round in self.rounds:
                        rounds_dict[round] = self.rounds[round].serialize()
                    rounds_list = list(rounds_dict.values())
                    for round in rounds_list:
                        matchs_list = list(round["matchs"].values())
                        for match in matchs_list:
                            player1 = match["player 1"]["ID"]
                            player2 = match["player 2"]["ID"]
                            combi1 = (player1, player2)
                            combi2 = (player2, player1)
                            if combi1 in self.matchs_combinations:
                                self.__matchs_combinations.remove(combi1)
                            else:
                                self.__matchs_combinations.remove(combi2)
            else:
                self.__matchs_combinations = value
        else:
            raise AttributeError("Les combinaisons du matchs doivent être envoyées dans une liste")

    @property
    def isover(self) -> bool:
        return self.__isover

    @isover.setter
    def isover(self, value: bool):
        if isinstance(value, bool):
            value = value
        elif isinstance(value, str):
            if value == "In progress":
                value = False
            elif value == "Complete":
                value = True
            else:
                raise AttributeError("L'état du tournoi doit être 'In progress' ou 'complete'")
        else:
            raise AttributeError("l'attribut 'isover' doit recevoir un booléen ou un string")
        self.__isover = value

    def create_round(self, round_number: int):
        round = Round(round_number, self.number_of_players)
        round_name = "round{}".format(str(round_number))
        self.rounds[round_name] = round
        self.players = round.sort_players(self.players)
        self.matchs_combinations = round.create_matchs(self.players, self.matchs_combinations)
        return round

    def set_scores(self, scores: list):
        rounds_list = list(self.rounds.values())
        round_scores = rounds_list[-1].set_scores(scores)
        for score in round_scores:
            for player in self.players:
                if score["ID"] == player["ID"]:
                    player["score"] += score["score"]
        if len(self.rounds) == self.number_of_rounds and rounds_list[-1].isover:
            self.isover = True

    def serialize(self) -> dict:
        rounds_dict = {}
        last_round = ""
        for round in self.rounds:
            rounds_dict[round] = self.rounds[round].serialize()
            last_round = round
        if last_round != "":
            self.players = self.rounds[last_round].sort_players(self.players)
        state = ""
        if self.isover:
            state = "Complete"
        else:
            state = "In progress"
        return {
                "name": self.name,
                "location": self.location,
                "date": self.date.isoformat(),
                "time control": self.time_control,
                "description": self.description,
                "number_of_players": self.number_of_players,
                "number_of_rounds": self.number_of_rounds,
                "ID": self.ID,
                "players": self.players,
                "rounds": rounds_dict,
                "state": state
        }


if __name__ == "__main__":
    tournament = Tournament("Nom du tournois", "Lieu", "2021-05-06", "Bullet", "Petit tournois de test", "8")
    player_number = 1
    for p in range(tournament.number_of_players):
        player_name = "Player{}".format(player_number)
        first_name = input("Quel est le prénom du joueur {} ? ".format(player_number))
        last_name = input("Quel est son nom ? ")
        birthdate = input("Quelle est sa date de naissance (AAAA-MM-JJ) ")
        gender = input("Quel est son sexe ? (M ou F) ")
        rank = "3000"
        players = [first_name, last_name, birthdate, gender, rank]
        player = player_manager.create(players)
        tournament.players[player.ID] = [0.0, player.rank]
        print("{} créé ! ".format(player_name))
        player_number += 1
    round_number = 1
    print(tournament.players)
    for r in range(tournament.number_of_rounds):
        tournament.players = player_manager.sort_players(tournament.players)
        print(tournament.players)
        round = tournament.create_round(round_number, tournament.players)
        tournament.rounds.append(round)
        round_number += 1
