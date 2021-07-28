from player_controller import player_controller
import re
from tournament_controller import tournament_controller
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
                            tournament = tournament_controller.create_tournament()
                            tournament_controller.add_players_to_tournament(tournament)
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
                                    TournamentView.display_in_progress_tournament(
                                        tournament_nb, tournament, next_round
                                    )
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
                            entry = int(entry)
                            if entry == 0:  # 1.2.0 Retour au menu précédent
                                run_tournament = False
                                continue
                            else:   # 1.2.1 Jouer un round du tournoi choisi
                                tournament = tournament_manager.unserialize_tournament(tournaments_list[entry - 1])
                                TournamentView.selected_tournament(tournament.name)
                                while not tournament.isover:
                                    tournament_controller.play_round(tournament)
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
                                    tournament_controller.change_tournament_data(tournament)
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
                                player = player_controller.create_player()
                                player_manager.save_player()
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
                                        player_controller.change_first_name(selected_player)
                                    elif entry == 2:  # Nom
                                        player_controller.change_last_name(selected_player)
                                    elif entry == 3:  # Rang
                                        player_controller.change_rank(selected_player)
                                    elif entry == 4:  # Date
                                        player_controller.change_birthdate(selected_player)
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
