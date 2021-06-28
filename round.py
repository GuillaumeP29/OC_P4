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
        try:
            self.isover = False
        except AttributeError as e:
            errors.appends(("isover", str(e)))
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

    @property
    def isover(self) -> bool:
        return self.__isover

    @isover.setter
    def isover(self, value: bool):
        if isinstance(value, bool):
            self.__isover = value

    def sort_players(self, list_to_sort: list):
        sorted_list = sorted(list_to_sort, key=lambda item: (-item.get("score"), item.get("rank")))
        return sorted_list

    def first_round_matchs(self, matchs_combinations: list[int, int]):
        """Set matchs for first round"""
        first_player = 0
        second_player = self.number_of_matchs
        matchs = []
        for m in range(self.number_of_matchs):
            matchs.append(Match(self.ID_tuple[first_player], self.ID_tuple[second_player]))
            if (self.ID_tuple[first_player], self.ID_tuple[second_player]) in matchs_combinations:
                matchs_combinations.remove((self.ID_tuple[first_player], self.ID_tuple[second_player]))
            else:
                matchs_combinations.remove((self.ID_tuple[second_player], self.ID_tuple[first_player]))
            first_player += 1
            second_player += 1
        return matchs, matchs_combinations

    def other_rounds_matchs(self, matchs_combinations: list[int, int]):
        """Set matchs for non first round"""
        first_player = 0
        second_player = 1
        deleted_combi_list = []
        matchs = []
        try_nb = 1
        ID_list = list(self.ID_tuple)
        while len(ID_list) >= 2:
            print("essai n° : ", try_nb)
            try:
                while len(ID_list) >= 2:  # tant qu'il y a des joueurs dans la liste
                    combi1 = (ID_list[first_player], ID_list[second_player])
                    combi2 = (ID_list[second_player], ID_list[first_player])
                    if combi1 in matchs_combinations:  # si les deux joueurs n'ont jamais combattu
                        matchs.append(Match(ID_list[first_player], ID_list[second_player]))  # On crée le match
                        ID_list.remove(ID_list[second_player])  # On enlève les joueurs de la liste
                        ID_list.remove(ID_list[first_player])  # Remplacer par des pop
                        deleted_combi_list.append(combi1)
                        matchs_combinations.remove(combi1)
                        second_player = 1
                    elif combi2 in matchs_combinations:
                        matchs.append(Match(ID_list[first_player], ID_list[second_player]))
                        del ID_list[second_player]
                        del ID_list[first_player]
                        deleted_combi_list.append(combi1)
                        matchs_combinations.remove(combi2)
                        second_player = 1
                    else:
                        second_player += 1
            except:
                try_nb += 1
                second_player = try_nb
                ID_list = list(self.ID_tuple)
                matchs = []
                for combi in deleted_combi_list:
                    matchs_combinations.append(combi)
                deleted_combi_list = []
        return matchs, matchs_combinations

    def create_matchs(self, players: list, matchs_combinations: list[int, int]):
        """Create the matchs of the rounds from the current ranking of the tournaments"""
        ID_list = []
        for ID in players:
            ID_list.append(ID["ID"])
        self.ID_tuple = tuple(ID_list)
        if self.round_number == 1:
            matchs = self.first_round_matchs(matchs_combinations)
        else:
            matchs = self.other_rounds_matchs(matchs_combinations)
        self.matchs = matchs[0]
        return matchs[1]

    def set_scores(self, scores: list):
        score_nb = 0
        round_scores = []
        for m in self.matchs:
            match = self.matchs[m]
            match.set_result(scores[score_nb])
            player_dict1 = {}
            player_dict2 = {}
            player_dict1["ID"] = match.player1
            player_dict1["score"] = match.result1
            player_dict2["ID"] = match.player2
            player_dict2["score"] = match.result2
            round_scores.append(player_dict1)
            round_scores.append(player_dict2)
            score_nb += 1
        self.isover = True
        return round_scores

    def serialize(self):
        matchs_dict = {}
        for match in self.matchs:
            matchs_dict[match] = self.matchs[match].serialize()
        return matchs_dict


if __name__ == "__main__":
    pass
