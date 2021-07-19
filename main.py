import re
import constants 
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from tournament_manager import tournament_manager
from player_manager import player_manager
from views.main_view import MainView

class Main:
    def run_program(self):
        run = True
        while run:
            tournament_manager.load_from_json()
            player_manager.load_from_json()
            MainView.main()
            entry_main_menu = ""
            entry_list = ("1", "2", "3")
            while entry_main_menu not in entry_list:
                entry_main_menu = MainView.main_menu()
                if entry_main_menu not in entry_list:
                    MainView.correct_value(entry_list)
            entry_main_menu = int(entry_main_menu)
            if entry_main_menu == 1:  # 1 Gestion des tournois
                tournaments_menu = True
                while tournaments_menu:
                    TournamentView.tournament_management()
                    entry_t_management = ""
                    entry_list = ("0", "1", "2", "3")
                    while entry_t_management not in entry_list:
                        entry_t_management = TournamentView.tournament_management_menu()
                        if entry_t_management not in entry_list:
                            MainView.correct_value(entry_list)
                    entry_t_management = int(entry_t_management)
                    if entry_t_management == 0:  # 1.0 Menu précédent
                        tournaments_menu = False
                    elif entry_t_management == 1:  # 1.1 Créer un nouveau tournoi
                        new_tournament = True
                        while new_tournament:
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
                                name, location, date, time_control, description, int(number_of_players), int(number_of_rounds)
                                ]
                            tournament = tournament_manager.new_tournament(*tournament_data)
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
                                                    MainView.error(constants.PLAYER_RANK_ERROR)
                                            if not rank_OK:
                                                MainView.error(constants.PLAYER_RANK_ERROR)
                                    if not rank:
                                        rank = 3000
                                    player_data = [first_name, last_name, birthdate, gender, int(rank)]
                                    player = player_manager.new_player(*player_data)
                                    players_ID.append(player.ID)
                            tournament.players = players_ID
                            tournament_manager.save_tournament(tournament)
                            new_tournament = False
                    elif entry_t_management == 2:  # 1.2 Choix d'un tournoi
                        run_tournament = True
                        while run_tournament:
                            tournament_nb = 1
                            tournaments_list = []
                            for tournament in tournament_manager.tournaments:
                                if tournament["state"] == "In progress":
                                    if tournament["rounds"] == {}:
                                        next_round_nb = 1
                                    else:
                                        next_round_nb = int(list(tournament["rounds"].keys())[-1].replace("round", ""))
                                        next_round_nb += 1
                                    next_round = "Round {}".format(str(next_round_nb))
                                    tournaments_list.append(tournament["ID"])
                                    if tournament_nb == 1:
                                        TournamentView.in_progress_tournaments_title()
                                    TournamentView.display_in_progress_tournament(tournament_nb, tournament, next_round)
                                    tournament_nb += 1
                            entry = ""
                            entry_OK = False
                            while not entry_OK:
                                entry = TournamentView.select_tournament()
                                if re.match(constants.REGEX_TOURNAMENT_NUMBER, entry):
                                    if int(entry) <= tournament_nb:
                                        entry_OK = True
                                if not entry_OK:
                                    MainView.ID_error(tournament_nb)
                            if entry == 0:  # 1.2.0 Retour au menu précédent
                                run_tournament = False
                                continue
                            else:   # 1.2.1 Jouer un round du tournoi choisi
                                tournament = tournament_manager.unserialize_tournament(tournaments_list[entry - 1])
                                TournamentView.selected_tournament(tournament.name)
                                while not tournament.isover:
                                    round_number = len(tournament.rounds) + 1
                                    round = tournament.create_round(round_number)
                                    scores = []
                                    TournamentView.display_round(tournament.name, round_number)
                                    for match in round.matchs:
                                        TournamentView.match()
                                        score = ""
                                        score_list = ("0", "1", "2")
                                        while score not in score_list:
                                            score = TournamentView.play_match(round.matchs, match)
                                            if score not in score_list:
                                                MainView.correct_value(score_list)
                                        scores.append(score)
                                    tournament.set_scores(scores)
                                    if not tournament.isover:
                                        entry = ""
                                        entry_list = ("0", "1", "2")
                                        while entry not in entry_list:
                                            entry = TournamentView.play_next_round()
                                            if entry not in entry_list:
                                                MainView.correct_value(entry_list)
                                        entry = int(entry)
                                        if entry == 0:
                                            tournament_manager.save_tournament(tournament)
                                            break
                                        elif entry == 1:
                                            tournament_manager.save_tournament(tournament)
                                            continue
                                        elif entry == 2:
                                            break
                                    else:
                                        tournament_manager.save_tournament(tournament)
                                run_tournament = False
                    elif entry_t_management == 3:  # 1.3 Quitter
                        tournaments_menu = False
                        run = False
            elif entry_main_menu == 2:  # 2 Archives
                records_menu = True
                while records_menu:
                    entry = ""
                    entry_list = ("0", "1", "2", "3")
                    while entry not in entry_list:
                        entry = MainView.display_menu()
                        if entry not in entry_list:
                            MainView.correct_value(entry_list)
                    entry = int(entry)
                    if entry == 0:  # 2.0 Menu précédent
                        records_menu = False
                        break
                    elif entry == 1:  # 2.1 Voir les tournois
                        tournaments_display_menu = True
                        while tournaments_display_menu:
                            by_date = False
                            entry = ""
                            entry_list = ("0", "1", "2", "3")
                            while entry not in entry_list:
                                entry = TournamentView.display_tournament_menu()
                                if entry not in entry_list:
                                    MainView.correct_value(entry_list)
                            entry = int(entry)
                            if entry == 0:  # 2.1.0 Menu Précédent
                                tournaments_display_menu = False
                                break
                            elif entry == 1:  # 2.1.1 Tri des tournois par date
                                by_date = True
                            elif entry == 2:  # 2.1.2 Tri des tournois par nom
                                by_date = False
                            elif entry == 3:  # 2.1.0 Menu Précédent
                                tournaments_display_menu = False
                                records_menu = False
                                run = False
                                break
                            tournament_manager.tournaments = tournament_manager.sort_tournaments(by_date)
                            tournament_nb = 1
                            if entry == 1 or 2:  # 2.1.1 / 2.1.2 Affichage des tournois
                                for tournament in tournament_manager.tournaments:
                                    TournamentView.display_tournament(tournament_nb, tournament)
                                    tournament_nb += 1
                                higher_nb = tournament_nb
                                nb_OK = False
                                while not nb_OK:
                                    entry = TournamentView.tournament_choice_menu()
                                    if re.match(constants.REGEX_TOURNAMENT_NUMBER, entry):
                                        if int(entry) <= higher_nb:
                                            nb_OK = True
                                        else:
                                            MainView.ID_error(higher_nb)
                                    else:
                                        MainView.ID_error(higher_nb)
                            entry = int(entry)
                            if entry == 0:  # 2.1.0 Menu Précédent
                                continue
                            else:  # 2.1.X Affichage du tournoi sélectionné
                                tournament = tournament_manager.tournaments[entry-1]
                                TournamentView.selected_tournament(tournament["name"])
                                entry = ""
                                entry_list = ("0", "1", "2", "3")
                                while entry not in entry_list:
                                    entry = TournamentView.selected_tournament_menu()
                                    if entry not in entry_list:
                                        MainView.correct_value(entry_list)
                                entry = int(entry)
                                if entry == 0:  # 2.1.X.0 Menu précédent
                                    tournaments_display_menu = False
                                    break
                                elif entry == 1:  # 2.1.X.1 Affichage tournoi complet
                                    TournamentView.display_full_tournament(tournament)
                                elif entry == 2:  # 2.1.X.2 Affichage joueurs du tournoi
                                    TournamentView.display_tournament_players(tournament)
                                elif entry == 3:  # 2.1.X.3 Menu modification du tournoi
                                    entry = ""
                                    entry_list = ("0", "1", "2", "3")
                                    while entry not in entry_list:
                                        entry = TournamentView.tournament_modification_menu()
                                        if entry not in entry_list:
                                            MainView.correct_value(entry_list)
                                    entry = int(entry)
                                    if entry == 0:  # 2.1.X.3.0 Menu précédent
                                        continue
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
                                            continue
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
                                            continue
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
                                            continue
                                        if entry == 1:
                                            tournament["description"] = new_description
                                            MainView.data_changed("Description")
                    elif entry == 2:  # 2.2 Voir les joueurs
                        players_display_menu = True
                        while players_display_menu:
                            by_rank = False
                            entry = ""
                            entry_list = ("0", "1", "2", "3", "4")
                            while entry not in entry_list:
                                entry = PlayerView.display_player_menu()
                                if entry not in entry_list:
                                    MainView.correct_value(entry_list)
                            entry = int(entry)
                            if entry == 0:  # 2.2.0 Menu précédent
                                players_display_menu = False
                                break
                            elif entry == 1:  # 2.2.1 Afficher joueurs par rang
                                by_rank = True
                            elif entry == 2:  # 2.2.2 Afficher joueurs par nom
                                by_rank = False
                            elif entry == 3:  # 2.2.3 Créer un nouveau joueur
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
                                                MainView.error(constants.PLAYER_RANK_ERROR)
                                        if not rank_OK:
                                            MainView.error(constants.PLAYER_RANK_ERROR)
                                if not rank:
                                    rank = 3000
                                player_data = [first_name, last_name, birthdate, gender, int(rank)]
                                player = player_manager.new_player(*player_data)
                                continue
                            if entry == 4:  # 2.2.4 Quitter le programme
                                players_display_menu = False
                                records_menu = False
                                run = False
                                break
                            higher_ID = 0
                            if entry == 1 or 2:  # 2.2.1 / 2.2.2 Affichage des joueurs
                                player_manager.players = player_manager.sort_players(by_rank)
                                for player in player_manager.players:
                                    PlayerView.display_player_by(player, by_rank)
                                    if player["ID"] > higher_ID:
                                        higher_ID = player["ID"]
                            ID_OK = False
                            while not ID_OK:
                                entry = PlayerView.player_choice_menu()
                                if re.match(constants.REGEX_PLAYER_ID, entry):
                                    entry = int(entry)
                                    if entry <= higher_ID:
                                        ID_OK = True
                                    else:
                                        MainView.ID_error(higher_ID)
                                else:
                                    MainView.ID_error(higher_ID)
                            if entry == 0:  # 2.2.0 Menu précédent
                                continue
                            else:
                                selected_player = {}
                                for player in player_manager.players:
                                    if player["ID"] == entry:
                                        PlayerView.display_full_player(player)
                                        selected_player = player
                                entry = ""
                                entry_list = ("0", "1")
                                while entry not in entry_list:
                                    entry = PlayerView.player_modification()
                                    if entry not in entry_list:
                                        MainView.correct_value(entry_list)
                                entry = int(entry)
                                if entry == 0:  # 2.2.x.0 Menu précédent
                                    players_display_menu = False
                                    break
                                if entry == 1:  # 2.2.x.1 Modifier joueur
                                    entry = ""
                                    entry_list = ("0", "1", "2", "3", "4")
                                    while entry not in entry_list:
                                        entry = PlayerView.player_modification_menu()
                                        if entry not in entry_list:
                                            MainView.correct_value(entry_list)
                                    entry = int(entry)
                                    if entry == 0:
                                        continue
                                    elif entry == 1:  # Prénom
                                        new_first_name =  ""
                                        while not re.match(constants.REGEX_FIRST_NAME, new_first_name):
                                            new_first_name = PlayerView.player_first_name()
                                            if not re.match(constants.REGEX_FIRST_NAME, new_first_name):
                                                MainView.error(constants.PLAYER_FIRST_NAME_ERROR)
                                                PlayerView.player_first_name_modification(selected_player)
                                        PlayerView.player_first_name_confirmation(selected_player, new_first_name)
                                        entry = ""
                                        entry_list = ("0", "1")
                                        while entry not in entry_list:
                                            entry = MainView.confirmation()
                                            if entry not in entry_list:
                                                MainView.correct_value(entry_list)
                                        entry = int(entry)
                                        if entry == 0:
                                            continue
                                        elif entry == 1:
                                            selected_player["first_name"] = new_first_name
                                            MainView.data_changed("Prénom")
                                    elif entry == 2:  # Nom
                                        new_last_name =  ""
                                        while not re.match(constants.REGEX_LAST_NAME, new_last_name):
                                            new_last_name = PlayerView.player_last_name()
                                            if not re.match(constants.REGEX_LAST_NAME, new_last_name):
                                                MainView.error(constants.PLAYER_LAST_NAME_ERROR)
                                                PlayerView.player_last_name_modification(selected_player)
                                        PlayerView.player_last_name_confirmation(selected_player, new_last_name)
                                        entry = ""
                                        entry_list = ("0", "1")
                                        while entry not in entry_list:
                                            entry = MainView.confirmation()
                                            if entry not in entry_list:
                                                MainView.correct_value(entry_list)
                                        entry = int(entry)
                                        if entry == 0:
                                            continue
                                        elif entry == 1:
                                            selected_player["last_name"] = new_last_name
                                            MainView.data_changed("Nom de famille")
                                    elif entry == 3:  # Rang
                                        new_rank =  ""
                                        while not re.match(constants.REGEX_RANK, new_rank):
                                            new_rank = PlayerView.rank()
                                            if not re.match(constants.REGEX_RANK, new_rank):
                                                MainView.error(constants.RANK_ERROR)
                                                PlayerView.rank_modification(selected_player)
                                        PlayerView.player_rank_confirmation(selected_player, new_rank)
                                        entry = ""
                                        entry_list = ("0", "1")
                                        while entry not in entry_list:
                                            entry = MainView.confirmation()
                                            if entry not in entry_list:
                                                MainView.correct_value(entry_list)
                                        entry = int(entry)
                                        if entry == 0:
                                            continue
                                        elif entry == 1:
                                            selected_player["rank"] = new_rank
                                            MainView.data_changed("Rang")
                                    elif entry == 4:  # Date
                                        new_birthdate =  ""
                                        while not re.match(constants.REGEX_DATE, new_birthdate):
                                            new_birthdate = PlayerView.birthdate()
                                            if not re.match(constants.REGEX_DATE, new_birthdate):
                                                MainView.error(constants.DATE_ERROR)
                                                PlayerView.birthdate_modification(selected_player)
                                        PlayerView.player_birthdate_confirmation(selected_player, new_birthdate)
                                        entry = ""
                                        entry_list = ("0", "1")
                                        while entry not in entry_list:
                                            entry = MainView.confirmation()
                                            if entry not in entry_list:
                                                MainView.correct_value(entry_list)
                                        entry = int(entry)
                                        if entry == 0:
                                            continue
                                        elif entry == 1:
                                            selected_player["birthdate"] = new_birthdate
                                            MainView.data_changed("Date de naissance")
                                player_manager.save_player()
                    elif entry == 3:  # 2.3 Menu précédent
                        records_menu = False
                        run = False
                        break
            elif entry_main_menu == 3:  # 3 Quitter
                run = False
                MainView.quit()


if __name__ == "__main__":
    main = Main()
    main.run_program()
