import constants
import re


class TournamentView:
    @staticmethod
    def tournament_management_menu():
        print("Vous voici dans le gestionaire de tournois")
        print("Que voulez-vous faire ?")
        entry = ""
        entry_list = ("0", "1", "2", "3")
        while entry not in entry_list:
            entry = input("""\
                \n0: Retourner au menu précédent\
                \n1: Créer un nouveau tournoi\
                \n2: Jouer un tournoi\
                \n3: Quitter le programme\
                \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def new_tournament_data():
        print("Vous voici dans l'outil de création d'un nouveau tournoi")
        print("Veuillez entrer les informations relatives au tournoi : ")
        name = ""
        while not re.match(constants.REGEX_TOURNAMENT_NAME, name):
            name = input("""Quel est le nom du tournoi ? """)
            if not re.match(constants.REGEX_TOURNAMENT_NAME, name):
                print("""Le nom du tournoi doit faire entre 2 et 100 caractères""")
        location = ""
        while not re.match(constants.REGEX_LOCATION, location):
            location = input("""Où aura lieu le tournoi ? """)
            if not re.match(constants.REGEX_LOCATION, location):
                print("""Le lieu du tournoi doit faire entre 2 et 50 caractères et ne doit pas comporter de chiffre""")
        date = ""
        while not re.match(constants.REGEX_DATE, date):
            date = input("""À quelle date aura-t-il lieu ? (AAAA-MM-JJ) """)
            if not re.match(constants.REGEX_DATE, date):
                print("""Vous devez rentrer une date sous le format : "AAAA-MM-JJ" """)
        time_control = ""
        time_control_list = ("1", "2", "3")
        while time_control not in time_control_list:
            time_control = input(
                """Quel type de contrôle du temps souhaitez-vous appliquer ?\
                \n1: Bullet\
                \n2: Blitz\
                \n3: Coup rapide\
                \n""")
            if time_control not in time_control_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(time_control_list))
        if time_control == "1":
            time_control = "Bullet"
        elif time_control == "2":
            time_control = "Blitz"
        elif time_control == "3":
            time_control = "Coup rapide"
        else:
            raise ValueError(
                """Le programme ne comprends pas votre réponse "{}" """.format(time_control)
            )
        description = ""
        while not re.match(constants.REGEX_DESCRIPTION, description):
            description = input("""Veuillez entrer une description au tournoi\n""")
            if not re.match(constants.REGEX_DESCRIPTION, description):
                print("""La description du tournoi doit compter entre 2 et 250 caractères""")
        number_of_players = ""
        while not re.match(constants.REGEX_NUMBER_OF_PLAYERS, number_of_players):
            number_of_players = input("""Combien de joueurs participeront au tournoi ? """)
            if not re.match(constants.REGEX_NUMBER_OF_PLAYERS, number_of_players):
                print("""Veuillez entrer un nombre entre 8 et 99""")
        number_of_rounds = ""
        while not re.match(constants.REGEX_NUMBER_OF_ROUNDS, number_of_rounds):
            number_of_rounds = input("""En combien de manche se déroulera le tournoi ? """)
            if not re.match(constants.REGEX_NUMBER_OF_ROUNDS, number_of_rounds):
                print("""Veuillez entrer un nombre entre 2 et 8""")
        print("""Le tournoi {} a bien été créé !\
            \nVeuillez maintenant y ajouter des joueurs pour le sauvegarder :\n""".format(name))
        return name, location, date, time_control, description, int(number_of_players), int(number_of_rounds)

    @staticmethod
    def created_tournament():
        print("Le tournoi a bien été créé et enregistré avec succès !")

    @staticmethod
    def display_in_progress_tournament(tournament_nb: int, tournament: dict, next_round: str):
        if tournament_nb == 1:
            print("Voici la liste des tournois en cours :\n")
        print("{}: ID : {} | {} | {} | {}".format(
            tournament_nb, tournament["ID"], tournament["name"], tournament["date"], next_round))

    @staticmethod
    def select_tournament(tournament_nb: int):
        entry = ""
        entry_OK = False
        while not entry_OK:
            entry = input(
                """\nVeuillez entrer le numéro (situé avant l'ID) du tournois que vous souhaitez démarrer ou\
                \nreprendre ou "0" pour annuler\n"""
                )
            if re.match(constants.REGEX_TOURNAMENT_NUMBER, entry):
                if int(entry) <= tournament_nb:
                    entry_OK = True
            if not entry_OK:
                print("Le nombre doit être entier et se situer entre 0 et {}".format(tournament_nb))
        return int(entry)

    @staticmethod
    def selected_tournament(name: str):
        print("""Tournoi "{}" sélectionné""".format(name))

    @staticmethod
    def create_round(round_number: int):
        print("Round {} créé !".format(round_number))
        print(round.serialize())
        print("Round {} en cours".format(round_number))

    @staticmethod
    def play_match(matchs: list, match: str):
        print("{} : joueur {} contre joueur {}".format(
                match, matchs[match].player1, matchs[match].player2
            ))
        score = ""
        score_list = ("0", "1", "2")
        while score not in score_list:
            score = input(
                """Veuillez indiquer l'issue du match\n1 : victoire du joueur {}\
                \n2 : victoire du joueur {}\n0 : égalité\n""".format(
                    matchs[match].player1, matchs[match].player2)
                )
            if score not in score_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(score_list))
        return int(score)

    @staticmethod
    def play_next_round():
        entry = ""
        entry_list = ("0", "1", "2")
        while entry not in entry_list:
            entry = input("""\
                \nSouhaitez-vous jouer le prochain round ?\
                \n0 : Non, arrêter le tournoi pour le moment\
                \n1 : Oui\
                \n2 : annuler les modifications apportées au tournois\
            \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def display_tournament_menu():
        entry = ""
        entry_list = ("0", "1", "2", "3")
        while entry not in entry_list:
            entry = input("""\
                \n0 : Retourner au menu précédent\
                \n1 : Afficher les tournois par date\
                \n2 : Afficher les tournois par nom\
                \n3 : Quitter le programme\
                \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

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
    def tournament_choice_menu(higher_nb):
        nb_OK = False
        while not nb_OK:
            tournament_nb = input("""\
                \nSouhaitez-vous afficher un tournois ?\
                \nOui : Veuillez indiquer le numéro du tournoi qui vous intéresse\
                \nNon : Entrez '0' pour retourner au menu précédent\
                \n""")
            if re.match(constants.REGEX_TOURNAMENT_NUMBER, tournament_nb):
                if int(tournament_nb) <= higher_nb:
                    nb_OK = True
                else:
                    print("""Le numéro du tournoi ne peut excéder {}\n""".format(higher_nb))
            else:
                print("Vous devez entrer un nombre entier\n")
        return int(tournament_nb)

    @staticmethod
    def selected_tournament_menu():
        entry = ""
        entry_list = ("0", "1", "2", "3")
        while entry not in entry_list:
            entry = input("""\nQue souhaitez vous faire ?\
                \n0 : Retour au menu précédent\
                \n1 : Afficher le tournoi complet\
                \n2 : Afficher les joueurs du tournoi\
                \n3 : Modifier un élement du tournoi\
                \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def tournament_modification_menu():
        entry = ""
        entry_list = ("0", "1", "2", "3")
        while entry not in entry_list:
            entry = input("""\nQue souhaitez-vous modifier ?\
                \n0 : Rien, annuler\
                \n1 : Le nom\
                \n2 : La date\
                \n3 : La descrition\
                \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def tournament_name_modification(tournament: dict):
        print("""Vous allez modifier le nom du tournoi : {}""".format(tournament["name"]))
        new_name = ""
        while not re.match(constants.REGEX_TOURNAMENT_NAME, new_name):
            new_name = input("""Veuillez indiquer le nouveau nom du tournoi\n""")
            if not re.match(constants.REGEX_TOURNAMENT_NAME, new_name):
                print("""Le nom du tournoi doit faire entre 2 et 100 caractères""")
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            tournament["name"], new_name))
        return new_name

    @staticmethod
    def tournament_date_modification(tournament: dict):
        print("""Vous allez modifier la date du tournoi : {}""".format(tournament["date"]))
        new_date = ""
        while not re.match(constants.REGEX_DATE, new_date):
            new_date = input("""Veuillez indiquer la nouvelle date du tournoi (AAAA-MM-JJ)\n""")
            if not re.match(constants.REGEX_DATE, new_date):
                print("""Vous devez rentrer une date sous le format : "AAAA-MM-JJ" """)
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            tournament["date"], new_date))
        return new_date

    @staticmethod
    def tournament_description_modification(tournament: dict):
        print("""Vous allez modifier la description du tournoi : {}""".format(tournament["description"]))
        new_description = ""
        while not re.match(constants.REGEX_DESCRIPTION, new_description):
            new_description = input("""Veuillez indiquer la nouvelle description du tournoi\n""")
            if not re.match(constants.REGEX_DESCRIPTION, new_description):
                print("""La description du tournoi doit faire entre 2 et 250 caractères""")
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            tournament["description"], new_description))
        return new_description

    @staticmethod
    def display_round(tournament_name: str, round_number: int):
        round_name = "round{}".format(str(round_number))
        print(tournament_name)
        print(round_name)
