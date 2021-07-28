import re
import constants
from views.player_view import PlayerView
from player_manager import player_manager
from views.main_view import MainView


class PlayerController:
    def create_player(self):
        first_name = ""
        while not re.match(constants.REGEX_FIRST_NAME, first_name):
            first_name = PlayerView.player_first_name()
            if not re.match(constants.REGEX_FIRST_NAME, first_name):
                MainView.error(constants.PLAYER_FIRST_NAME_ERROR)
        last_name = ""
        while not re.match(constants.REGEX_LAST_NAME, last_name):
            last_name = PlayerView.player_last_name()
            if not re.match(constants.REGEX_LAST_NAME, last_name):
                MainView.error(constants.PLAYER_LAST_NAME_ERROR)
        birthdate = ""
        while not re.match(constants.REGEX_DATE, birthdate):
            birthdate = PlayerView.birthdate()
            if not re.match(constants.REGEX_DATE, birthdate):
                MainView.error(constants.DATE_ERROR)
        gender = ""
        gender_list = ("M", "F")
        while gender not in gender_list:
            gender = PlayerView.gender()
            if gender not in gender_list:
                MainView.correct_value(gender_list)
        pronoun = ""
        termination = ""
        if gender == "M":
            pronoun = "il"
        elif gender == "F":
            pronoun = "elle"
            termination = "e"
        ranked = ""
        ranked_list = ("1", "2")
        while ranked not in ranked_list:
            ranked = PlayerView.ranked(first_name, pronoun, termination)
            if ranked not in ranked_list:
                MainView.correct_value(ranked_list)
        rank = None
        if int(ranked) == 1:
            rank_OK = False
            while not rank_OK:
                rank = PlayerView.rank()
                if re.match(constants.REGEX_RANK, rank):
                    if 0 < int(rank) <= 3000:
                        rank_OK = True
                    else:
                        MainView.error(constants.RANK_ERROR)
                if not rank_OK:
                    MainView.error(constants.RANK_ERROR)
        if not rank:
            rank = 3000
        player_data = [first_name, last_name, birthdate, gender, int(rank)]
        player = player_manager.new_player(*player_data)
        return player

    def change_first_name(self, player: dict):
        new_first_name = ""
        while not re.match(constants.REGEX_FIRST_NAME, new_first_name):
            new_first_name = PlayerView.player_first_name()
            if not re.match(constants.REGEX_FIRST_NAME, new_first_name):
                MainView.error(constants.PLAYER_FIRST_NAME_ERROR)
                PlayerView.player_first_name_modification(player)
        PlayerView.player_first_name_confirmation(player, new_first_name)
        entry = ""
        entry_list = ("0", "1")
        while entry not in entry_list:
            entry = MainView.confirmation()
            if entry not in entry_list:
                MainView.correct_value(entry_list)
        entry = int(entry)
        if entry == 0:
            MainView.cancel_data_change()
        elif entry == 1:
            player["first_name"] = new_first_name
            MainView.data_changed("Prénom")

    def change_last_name(self, player: dict):
        new_last_name = ""
        while not re.match(constants.REGEX_LAST_NAME, new_last_name):
            new_last_name = PlayerView.player_last_name()
            if not re.match(constants.REGEX_LAST_NAME, new_last_name):
                MainView.error(constants.PLAYER_LAST_NAME_ERROR)
                PlayerView.player_last_name_modification(player)
        PlayerView.player_last_name_confirmation(player, new_last_name)
        entry = ""
        entry_list = ("0", "1")
        while entry not in entry_list:
            entry = MainView.confirmation()
            if entry not in entry_list:
                MainView.correct_value(entry_list)
        entry = int(entry)
        if entry == 0:
            MainView.cancel_data_change()
        elif entry == 1:
            player["last_name"] = new_last_name
            MainView.data_changed("Nom de famille")

    def change_rank(self, player: dict):
        new_rank = ""
        while not re.match(constants.REGEX_RANK, new_rank):
            new_rank = PlayerView.rank()
            if not re.match(constants.REGEX_RANK, new_rank):
                MainView.error(constants.RANK_ERROR)
                PlayerView.rank_modification(player)
        PlayerView.rank_confirmation(player, new_rank)
        entry = ""
        entry_list = ("0", "1")
        while entry not in entry_list:
            entry = MainView.confirmation()
            if entry not in entry_list:
                MainView.correct_value(entry_list)
        entry = int(entry)
        if entry == 0:
            MainView.cancel_data_change()
        elif entry == 1:
            player["rank"] = new_rank
            MainView.data_changed("Rang")

    def change_birthdate(self, player: dict):
        new_birthdate = ""
        while not re.match(constants.REGEX_DATE, new_birthdate):
            new_birthdate = PlayerView.birthdate()
            if not re.match(constants.REGEX_DATE, new_birthdate):
                MainView.error(constants.DATE_ERROR)
                PlayerView.player_birthdate_modification(player)
        PlayerView.player_birthdate_confirmation(player, new_birthdate)
        entry = ""
        entry_list = ("0", "1")
        while entry not in entry_list:
            entry = MainView.confirmation()
            if entry not in entry_list:
                MainView.correct_value(entry_list)
        entry = int(entry)
        if entry == 0:
            MainView.cancel_data_change()
        elif entry == 1:
            player["birthdate"] = new_birthdate
            MainView.data_changed("Date de naissance")


player_controller = PlayerController()
