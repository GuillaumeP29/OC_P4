import re
import constants
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from tournament_manager import tournament_manager
from player_manager import player_manager
from views.main_view import MainView
from player_controller import player_controller


class TournamentController:
    def create_tournament(self):
        TournamentView.new_tournament()
        name = ""
        while not re.match(constants.REGEX_TOURNAMENT_NAME, name):
            name = TournamentView.tournament_name()
            if not re.match(constants.REGEX_TOURNAMENT_NAME, name):
                MainView.error(constants.TOURNAMENT_NAME_ERROR)
        location = ""
        while not re.match(constants.REGEX_LOCATION, location):
            location = TournamentView.tournament_location()
            if not re.match(constants.REGEX_LOCATION, location):
                MainView.error(constants.TOURNAMENT_LOCATION_ERROR)
        date = ""
        while not re.match(constants.REGEX_DATE, date):
            date = TournamentView.tournament_date()
            if not re.match(constants.REGEX_DATE, date):
                MainView.error(constants.DATE_ERROR)
        time_control = ""
        entry_list = ("1", "2", "3")
        while time_control not in entry_list:
            time_control = TournamentView.time_control()
            if time_control not in entry_list:
                MainView.correct_value(entry_list)
        if time_control == "1":
            time_control = "Bullet"
        elif time_control == "2":
            time_control = "Blitz"
        elif time_control == "3":
            time_control = "Coup rapide"
        description = ""
        while not re.match(constants.REGEX_DESCRIPTION, description):
            description = TournamentView.tournament_description()
            if not re.match(constants.REGEX_DESCRIPTION, description):
                MainView.error(constants.TOURNAMENT_DESCRIPTION_ERROR)
        number_of_players = ""
        while not re.match(constants.REGEX_NUMBER_OF_PLAYERS, number_of_players):
            number_of_players = TournamentView.number_of_players()
            if not re.match(constants.REGEX_NUMBER_OF_PLAYERS, number_of_players):
                MainView.error(constants.NUMBER_OF_PLAYERS_ERROR)
        number_of_rounds = ""
        while not re.match(constants.REGEX_NUMBER_OF_ROUNDS, number_of_rounds):
            number_of_rounds = TournamentView.number_of_rounds()
            if not re.match(constants.REGEX_NUMBER_OF_ROUNDS, number_of_rounds):
                MainView.error(constants.NUMBER_OF_ROUNDS_ERROR)
        TournamentView.tournament_players(name)
        tournament_data = [
            name, location, date, time_control, description, int(number_of_players),
            int(number_of_rounds)
            ]
        tournament = tournament_manager.new_tournament(*tournament_data)
        return tournament

    def add_players_to_tournament(self, tournament: type):
        players_ID = []
        for player in range(tournament.number_of_players):
            entry = ""
            entry_list = ("1", "2")
            while entry not in entry_list:
                entry = PlayerView.way_to_add_player(player)
                if entry not in entry_list:
                    MainView.correct_value(entry_list)
            entry = int(entry)
            if entry == 1:  # 1.1.1 Ajout d'un joueur existant
                higher_ID = 0
                for player in player_manager.players:
                    if player["ID"] > higher_ID:
                        higher_ID = player["ID"]
                    PlayerView.display_player(player)
                if players_ID != []:
                    PlayerView.selected_player(players_ID)
                ID_OK = False
                while not ID_OK:
                    player_ID = PlayerView.select_player()
                    if re.match(constants.REGEX_PLAYER_ID, player_ID):
                        if int(player_ID) <= higher_ID:
                            if int(player_ID) not in players_ID:
                                ID_OK = True
                            else:
                                PlayerView.already_selected_player(player_ID)
                        else:
                            MainView.ID_error(higher_ID)
                    else:
                        MainView.ID_error(higher_ID)
                players_ID.append(int(player_ID))
            if entry == 2:  # 1.1.2 Création et ajout d'un nouveau joueur
                player = player_controller.create_player()
                players_ID.append(player.ID)
        tournament.players = players_ID

    def change_tournament_data(self, tournament: type):
        entry = ""
        entry_list = ("0", "1", "2", "3")
        while entry not in entry_list:
            entry = TournamentView.tournament_modification_menu()
            if entry not in entry_list:
                MainView.correct_value(entry_list)
        entry = int(entry)
        if entry == 0:  # 2.1.X.3.0 Menu précédent
            return None
        elif entry == 1:  # 2.1.X.3.1 Modification du nom du tournoi
            TournamentView.tournament_name_modification(tournament)
            new_name = ""
            while not re.match(constants.REGEX_TOURNAMENT_NAME, new_name):
                new_name = TournamentView.tournament_name()
                if not re.match(constants.REGEX_TOURNAMENT_NAME, new_name):
                    MainView.error(constants.TOURNAMENT_NAME_ERROR)
            TournamentView.tournament_name_confirmation(tournament, new_name)
            entry = ""
            entry_list = ("0", "1")
            while entry not in entry_list:
                entry = MainView.confirmation()
                if entry not in entry_list:
                    MainView.correct_value(entry_list)
            entry = int(entry)
            if entry == 0:  # Annuler modif.
                return None
            if entry == 1:  # Confirmer modif.
                tournament["name"] = new_name
                MainView.data_changed("Nom")
        elif entry == 2:  # 2.1.X.3.2 Modification de la date du tournoi
            TournamentView.tournament_date_modification(tournament)
            new_date = ""
            while not re.match(constants.REGEX_DATE, new_date):
                new_date = TournamentView.tournament_date()
                if not re.match(constants.REGEX_DATE, new_date):
                    MainView.error(constants.DATE_ERROR)
            TournamentView.tournament_date_confirmation(tournament, new_date)
            entry = ""
            entry_list = ("0", "1")
            while entry not in entry_list:
                entry = MainView.confirmation()
                if entry not in entry_list:
                    MainView.correct_value(entry_list)
            entry = int(entry)
            if entry == 0:
                return None
            if entry == 1:
                tournament["date"] = new_date
                MainView.data_changed("Date")
        elif entry == 3:  # 2.1.X.3.3 Modification de la description du tournoi
            TournamentView.tournament_description_modification(tournament)
            new_description = ""
            while not re.match(constants.REGEX_DESCRIPTION, new_description):
                new_description = TournamentView.tournament_description()
                if not re.match(constants.REGEX_DESCRIPTION, new_description):
                    MainView.error(constants.TOURNAMENT_DESCRIPTION_ERROR)
            TournamentView.tournament_description_confirmation(tournament, new_description)
            entry = ""
            entry_list = ("0", "1")
            while entry not in entry_list:
                entry = MainView.confirmation()
                if entry not in entry_list:
                    MainView.correct_value(entry_list)
            entry = int(entry)
            if entry == 0:
                return None
            if entry == 1:
                tournament["description"] = new_description
                MainView.data_changed("Description")

    def play_round(self, tournament: type):
        tournament = tournament
        round_number = len(tournament.rounds) + 1
        round = tournament.create_round(round_number)
        scores = []
        TournamentView.display_round(tournament.name, round_number)
        for match in round.matchs:
            TournamentView.match(round.matchs, match)
            score = ""
            score_list = ("0", "1", "2")
            while score not in score_list:
                score = TournamentView.play_match(round.matchs, match)
                if score not in score_list:
                    MainView.correct_value(score_list)
            scores.append(int(score))
        tournament.set_scores(scores)


tournament_controller = TournamentController()
