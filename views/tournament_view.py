class TournamentView:
    @staticmethod
    def tournament_management():
        print("Vous voici dans le gestionaire de tournois")
        print("Que voulez-vous faire ?")

    @staticmethod
    def tournament_management_menu():
        entry = input("""\
            \n0: Retourner au menu précédent\
            \n1: Créer un nouveau tournoi\
            \n2: Jouer un tournoi\
            \n3: Quitter le programme\
            \n""")
        return entry

    @staticmethod
    def new_tournament():
        print("Vous voici dans l'outil de création d'un nouveau tournoi")
        print("Veuillez entrer les informations relatives au tournoi : ")

    @staticmethod
    def tournament_players(name):
        print("""Le tournoi {} a bien été créé !\
            \nVeuillez maintenant y ajouter des joueurs pour le sauvegarder :\n""".format(name))

    @staticmethod
    def created_tournament():
        print("Le tournoi a bien été créé et enregistré avec succès !")

    @staticmethod
    def in_progress_tournaments_title():
        print("Voici la liste des tournois en cours :\n")

    @staticmethod
    def display_in_progress_tournament(tournament_nb: int, tournament: dict, next_round: str):
        print("{}: ID : {} | {} | {} | {}".format(
            tournament_nb, tournament["ID"], tournament["name"], tournament["date"], next_round))

    @staticmethod
    def select_tournament():
        entry = input(
            """\nVeuillez entrer le numéro (situé avant l'ID) du tournois que vous souhaitez démarrer ou\
            \nreprendre ou "0" pour annuler\n"""
            )
        return entry

    @staticmethod
    def selected_tournament(name: str):
        print("""Tournoi "{}" sélectionné""".format(name))

    @staticmethod
    def display_round(tournament_name: str, round_number: int):
        round_name = "round{}".format(str(round_number))
        print(tournament_name)
        print(round_name)

    @staticmethod
    def create_round(round_number: int):
        print("Round {} créé !".format(round_number))
        print(round.serialize())
        print("Round {} en cours".format(round_number))

    @staticmethod
    def match(matchs: list, match: str):
        print("{} : joueur {} contre joueur {}".format(
            match, matchs[match].player1, matchs[match].player2
        ))

    @staticmethod
    def play_match(matchs: list, match: str):
        score = input(
            """Veuillez indiquer l'issue du match\n1 : victoire du joueur {}\
            \n2 : victoire du joueur {}\n0 : égalité\n""".format(
                matchs[match].player1, matchs[match].player2)
        )
        return score

    @staticmethod
    def play_next_round():
        entry = input("""\
            \nSouhaitez-vous jouer le prochain round ?\
            \n0 : Non, arrêter le tournoi pour le moment\
            \n1 : Oui\
            \n2 : annuler les modifications apportées au tournois\
        \n""")
        return entry

    @staticmethod
    def display_tournament_menu():
        entry = input("""\
            \n0 : Retourner au menu précédent\
            \n1 : Afficher les tournois par date\
            \n2 : Afficher les tournois par nom\
            \n3 : Quitter le programme\
            \n""")
        return entry

    @staticmethod
    def display_tournament(tournament_nb: int, tournament: dict):
        print("""{}: {} | {} | {}""".format(
            tournament_nb, tournament["ID"], tournament["name"], tournament["date"]))

    @staticmethod
    def display_full_tournament(tournament: dict):
        print(tournament)

    @staticmethod
    def display_tournament_players(tournament: dict):
        print(tournament["players"])

    @staticmethod
    def tournament_choice_menu():
        entry = input("""\
            \nSouhaitez-vous afficher un tournois ?\
            \nOui : Veuillez indiquer le numéro du tournoi qui vous intéresse\
            \nNon : Entrez '0' pour retourner au menu précédent\
            \n""")
        return entry

    @staticmethod
    def selected_tournament_menu():
        entry = input("""\nQue souhaitez vous faire ?\
            \n0 : Retour au menu précédent\
            \n1 : Afficher le tournoi complet\
            \n2 : Afficher les joueurs du tournoi\
            \n3 : Modifier un élement du tournoi\
            \n""")
        return entry

    @staticmethod
    def tournament_modification_menu():
        entry = input("""\nQue souhaitez-vous modifier ?\
            \n0 : Rien, annuler\
            \n1 : Le nom\
            \n2 : La date\
            \n3 : La descrition\
            \n""")
        return entry

    @staticmethod
    def tournament_name():
        new_name = input("""Veuillez indiquer le nom du tournoi\n""")
        return new_name

    @staticmethod
    def tournament_name_modification(tournament: dict):
        print("""Vous allez modifier le nom du tournoi : {}""".format(tournament["name"]))

    @staticmethod
    def tournament_name_confirmation(tournament: dict, new_name):
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            tournament["name"], new_name))

    @staticmethod
    def tournament_location():
        new_location = input("""Veuillez indiquer le lieu du tournoi\n""")
        return new_location

    @staticmethod
    def tournament_date():
        new_date = input("""Veuillez indiquer la date du tournoi (AAAA-MM-JJ)\n""")
        return new_date

    @staticmethod
    def tournament_date_modification(tournament: dict):
        print("""Vous allez modifier la date du tournoi : {}""".format(tournament["date"]))

    @staticmethod
    def tournament_date_confirmation(tournament: dict, new_date):
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            tournament["date"], new_date))

    @staticmethod
    def time_control():
        time_control = input(
            """Quel type de contrôle du temps souhaitez-vous appliquer ?\
            \n1: Bullet\
            \n2: Blitz\
            \n3: Coup rapide\
            \n""")
        return time_control

    @staticmethod
    def tournament_description():
        new_description = input("""Veuillez décrire le tournoi\n""")
        return new_description

    @staticmethod
    def tournament_description_modification(tournament: dict):
        print("""Vous allez modifier la description du tournoi : {}""".format(tournament["description"]))

    @staticmethod
    def tournament_description_confirmation(tournament: dict, new_description):
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            tournament["description"], new_description))

    @staticmethod
    def number_of_players():
        number_of_players = input("""Combien de joueurs participeront au tournoi ? """)
        return number_of_players

    @staticmethod
    def number_of_rounds():
        number_of_rounds = input("""En combien de manche se déroulera le tournoi ? """)
        return number_of_rounds
