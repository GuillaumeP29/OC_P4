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
            entry_main = MainView.main()
            if entry_main == 1:  # 1 Gestion des tournois
                tournaments_menu = True
                while tournaments_menu:
                    entry_t_management = TournamentView.tournament_management_menu()
                    if entry_t_management == 0:  # 1.0 Menu précédent
                        tournaments_menu = False
                    elif entry_t_management == 1:  # 1.1 Créer un nouveau tournoi
                        new_tournament = True
                        while new_tournament:
                            tournament_data = TournamentView.new_tournament_data()
                            tournament = tournament_manager.new_tournament(*tournament_data)
                            players_ID = []
                            for player in range(tournament.number_of_players):
                                entry = PlayerView.way_to_add_player(player)
                                if entry == 1:  # 1.1.1 Ajout d'un joueur existant
                                    higher_ID = 0
                                    for player in player_manager.players:
                                        if player["ID"] > higher_ID:
                                            higher_ID = player["ID"]
                                        PlayerView.display_player(player)
                                    player_ID = PlayerView.select_player(players_ID, higher_ID)
                                    players_ID.append(player_ID)
                                if entry == 2:  # 1.1.2 Création et ajout d'un nouveau joueur
                                    player_data = PlayerView.new_player()
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
                                    TournamentView.display_in_progress_tournament(tournament_nb, tournament, next_round)
                                    tournament_nb += 1
                            entry = TournamentView.select_tournament(tournament_nb)
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
                                        score = TournamentView.play_match(round.matchs, match)
                                        scores.append(score)
                                    tournament.set_scores(scores)
                                    if not tournament.isover:
                                        entry = TournamentView.play_next_round()
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
            elif entry_main == 2:  # 2 Archives
                records_menu = True
                while records_menu:
                    entry = MainView.display_menu()
                    if entry == 0:  # 2.0 Menu précédent
                        records_menu = False
                        break
                    elif entry == 1:  # 2.1 Voir les tournois
                        tournaments_display_menu = True
                        while tournaments_display_menu:
                            by_date = False
                            entry = TournamentView.display_tournament_menu()
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
                                entry = TournamentView.tournament_choice_menu(higher_nb)
                            if entry == 0:  # 2.1.0 Menu Précédent
                                continue
                            else:  # 2.1.X Affichage du tournoi sélectionné
                                tournament = tournament_manager.tournaments[entry-1]
                                TournamentView.selected_tournament(tournament["name"])
                                entry = TournamentView.selected_tournament_menu()
                                if entry == 0:  # 2.1.X.0 Menu précédent
                                    tournaments_display_menu = False
                                    break
                                elif entry == 1:  # 2.1.X.1 Affichage tournoi complet
                                    TournamentView.display_full_tournament(tournament)
                                elif entry == 2:  # 2.1.X.2 Affichage joueurs du tournoi
                                    TournamentView.display_tournament_players(tournament)
                                elif entry == 3:  # 2.1.X.3 Menu modification du tournoi
                                    entry = TournamentView.tournament_modification_menu()
                                    if entry == 0:  # 2.1.X.3.0 Menu précédent
                                        continue
                                    elif entry == 1:  # 2.1.X.3.1 Modification du nom du tournoi
                                        new_name = TournamentView.tournament_name_modification(tournament)
                                        entry = MainView.confirmation()
                                        if entry == 0:  # Annuler modif.
                                            continue
                                        if entry == 1:  # Confirmer modif.
                                            tournament["name"] = new_name
                                            MainView.data_changed("Nom")
                                    elif entry == 2:
                                        new_date = TournamentView.tournament_date_modification(tournament)
                                        entry = MainView.confirmation()
                                        if entry == 0:
                                            continue
                                        if entry == 1:
                                            tournament["date"] = new_date
                                            MainView.data_changed("Date")
                                    elif entry == 3:
                                        new_description = TournamentView.tournament_description_modification(tournament)
                                        entry = MainView.confirmation()
                                        if entry == 0:
                                            continue
                                        if entry == 1:
                                            tournament["description"] = new_description
                                            MainView.data_changed("Description")
                    elif entry == 2:  # 2.2 Voir les joueurs
                        players_display_menu = True
                        while players_display_menu:
                            by_rank = False
                            entry = PlayerView.display_player_menu()
                            if entry == 0:  # 2.2.0 Menu précédent
                                players_display_menu = False
                                break
                            elif entry == 1:  # 2.2.1 Afficher joueurs par rang
                                by_rank = True
                            elif entry == 2:  # 2.2.2 Afficher joueurs par nom
                                by_rank = False
                            elif entry == 3:  # 2.2.3 Créer un nouveau joueur
                                player_data = PlayerView.new_player()
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
                            entry = PlayerView.player_choice_menu(higher_ID)
                            if entry == 0:  # 2.2.0 Menu précédent
                                continue
                            else:
                                selected_player = {}
                                for player in player_manager.players:
                                    if player["ID"] == entry:
                                        PlayerView.display_full_player(player)
                                        selected_player = player
                                entry = PlayerView.player_modification()
                                if entry == 0:
                                    players_display_menu = False
                                    break
                                if entry == 1:
                                    entry = PlayerView.player_modification_menu()
                                    if entry == 0:
                                        continue
                                    elif entry == 1:
                                        new_first_name = PlayerView.player_first_name_modification(selected_player)
                                        entry = MainView.confirmation()
                                        if entry == 0:
                                            continue
                                        elif entry == 1:
                                            selected_player["first_name"] = new_first_name
                                            MainView.data_changed("Prénom")
                                    elif entry == 2:
                                        new_last_name = PlayerView.player_last_name_modification(selected_player)
                                        entry = MainView.confirmation()
                                        if entry == 0:
                                            continue
                                        elif entry == 1:
                                            selected_player["last_name"] = new_last_name
                                            MainView.data_changed("Nom de famille")
                                    elif entry == 3:
                                        new_rank = PlayerView.player_rank_modification(selected_player)
                                        entry = MainView.confirmation()
                                        if entry == 0:
                                            continue
                                        elif entry == 1:
                                            selected_player["rank"] = new_rank
                                            MainView.data_changed("Rang")
                                    elif entry == 4:
                                        new_birthdate = PlayerView.player_birthdate_modification(selected_player)
                                        entry = MainView.confirmation()
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
            elif entry_main == 3:  # 3 Quitter
                run = False
                MainView.quit()



if __name__ == "__main__":
    main = Main()
    main.run_program()
