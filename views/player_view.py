import re
from constants import *


class PlayerView:
    @staticmethod
    def way_to_add_player(player: int):
        print("Comment voulez-vous ajouter le joueur N°{} ?".format(player + 1))
        entry = ""
        entry_list = ("1", "2")
        while entry not in entry_list:
            entry = input("1: Ajouter un joueur depuis la liste de joueurs\n2: Créer un nouveau joueur\n")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def display_player(player: dict):
        print("ID : {} | {} {}".format(player["ID"], player["first_name"], player["last_name"]))

    @staticmethod
    def display_player_by(player: dict, by_rank: bool):
        if by_rank:
            print("{}: {} | {} {}".format(player["ID"], player["rank"], player["first_name"], player["last_name"]))
        else:
            print("{}: {} {} | {}".format(player["ID"], player["last_name"], player["first_name"], player["rank"]))

    @staticmethod
    def display_full_player(player: dict):
        print(player)

    @staticmethod
    def select_player(players_ID: list, higher_ID: int):
        if players_ID != []:
            print("Joueurs déjà choisis : {}".format(players_ID))
        ID_OK = False
        while not ID_OK:
            player_ID = input("Entrez l'ID du joueur à sélectionner : ")
            if re.match(REGEX_PLAYER_ID, player_ID):
                if int(player_ID) <= higher_ID:
                    if int(player_ID) not in players_ID:
                        ID_OK = True
                    else:
                        print("Le joueur {} ne peut pas être sélectionné une seconde fois".format(player_ID))
                else:
                    print("Le nombre doit être entier et se situer entre 0 et {}".format(higher_ID))
            else:
                print("Le nombre doit être entier et se situer entre 0 et {}".format(higher_ID))
        return int(player_ID)

    @staticmethod
    def new_player():
        first_name = ""
        while not re.match(REGEX_FIRST_NAME, first_name):
            first_name = input("Quel est le prénom du nouveau joueur ? ")
            if not re.match(REGEX_FIRST_NAME, first_name):
                print("""
                    Le prénom du joueur doit faire entre 2 et 30 caractères et ne doit pas comporter de chiffre
                    """)
        last_name = ""
        while not re.match(REGEX_LAST_NAME, last_name):
            last_name = input("Quel est son nom de famille ? ")
            if not re.match(REGEX_LAST_NAME, first_name):
                print("""
                    Le nom de famille du joueur doit faire entre 2 et 30 caractères et ne doit pas comporter de chiffre
                    """)
        birthdate = ""
        while not re.match(REGEX_BIRTHDATE, birthdate):
            birthdate = input("Veuillez entrer sa date de naissance (AAAA/MM/JJ) : ")
            if not re.match(REGEX_BIRTHDATE, birthdate):
                print("""Vous devez rentrer une date sous le format : "AAAA-MM-JJ" """)
        gender = ""
        gender_list = ("M", "F")
        while gender not in gender_list:
            gender = input("Quel est le sexe du joueur (M ou F) ? ")
            if gender not in gender_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(gender_list))
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
            ranked = input(
                "{} est-{} classé{} (1: Oui ; 2: Non) ? ".format(first_name, pronoun, termination)
                )
            if ranked not in ranked_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(ranked_list))
        rank = None
        if int(ranked) == 1:
            rank_OK = False
            while not rank_OK:
                rank = input("Quel est son rang ? ")
                if re.match(REGEX_RANK, rank):
                    if 0 < int(rank) <= 3000:
                        rank_OK = True
                if not rank_OK:
                    print("Le rang du joueur doit être un nombre compris entre 1 et 3000")
        if not rank:
            rank = 3000
        return first_name, last_name, birthdate, gender, int(rank)

    @staticmethod
    def display_player_menu():
        entry = ""
        entry_list = ("0", "1", "2", "3", "4")
        while entry not in entry_list:
            entry = input("""\
                \n0 : Retourner au menu précédent\
                \n1 : Afficher les joueurs par rang\
                \n2 : Afficher les joueurs par nom\
                \n3 : Créer un nouveau joueur\
                \n4 : Quitter le programme\
                \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def player_choice_menu(higher_ID):
        ID_OK = False
        while not ID_OK:
            player_ID = input("""\
                \nSouhaitez-vous afficher un joueur ?\
                \nOui : Veuillez indiquer l'ID du joueur qui vous intéresse\
                \nNon : Entrez '0' pour retourner au menu précédent\
                \n""")
            if re.match(REGEX_PLAYER_ID, player_ID):
                if int(player_ID) <= higher_ID:
                    ID_OK = True
                else:
                    print("""L'ID joueur ne peut excéder {}\n""".format(higher_ID))
            else:
                print("Vous devez entrer un nombre entier\n")
        return int(player_ID)

    @staticmethod
    def player_modification():
        entry = ""
        entry_list = ("0", "1")
        while entry not in entry_list:
            entry = input("""\
                \nSouhaitez-vous modifier le joueur ?\
                \n1 : Oui\
                \n0 : Non, retourner au menu précédent\
                \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def player_modification_menu():
        entry = ""
        entry_list = ("0", "1", "2", "3", "4")
        while entry not in entry_list:
            entry = input("""Que souhaitez-vous modifier ?\
                \n0 : Rien, annuler la modification\
                \n1 : Le prénom du joueur\
                \n2 : Le nom de famille du joueur\
                \n3 : Le rang du joueur\
                \n4 : La date de naissance du joueur\
                \n""")
            if entry not in entry_list:
                print("""Vous devez rentrer une des valeurs suivantes : {} """.format(entry_list))
        return int(entry)

    @staticmethod
    def player_first_name_modification(player: dict):
        print("""Vous allez modifier le prénom du joueur : {}""".format(player["first_name"]))
        new_first_name = ""
        while not re.match(REGEX_FIRST_NAME, new_first_name):
            new_first_name = input("""Veuillez indiquer le nouveau prénom du joueur\n""")
            if not re.match(REGEX_FIRST_NAME, new_first_name):
                print("""Le prénom du joueur doit faire entre 2 et 30 caractères""")
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["first_name"], new_first_name))
        return new_first_name

    @staticmethod
    def player_last_name_modification(player: dict):
        print("""Vous allez modifier le nom de famille du joueur : {}""".format(player["last_name"]))
        new_last_name = ""
        while not re.match(REGEX_LAST_NAME, new_last_name):
            new_last_name = input("""Veuillez indiquer le nouveau nom de famille du joueur\n""")
            if not re.match(REGEX_LAST_NAME, new_last_name):
                print("""Le nom de famille du joueur doit faire entre 2 et 30 caractères""")
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["last_name"], new_last_name))
        return new_last_name

    @staticmethod
    def player_rank_modification(player: dict):
        print("""Vous allez modifier le rang du joueur : {}""".format(player["rank"]))
        new_rank = ""
        new_rank_OK = False
        while not new_rank_OK:
            new_rank = input("""Veuillez indiquer le nouveau rang du joueur\n""")
            if re.match(REGEX_RANK, new_rank):
                if 0 < int(new_rank) <= 3000:
                    new_rank_OK = True
            if not new_rank_OK:
                print("Le rang du joueur doit être un nombre compris entre 1 et 3000")
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["rank"], new_rank))
        return new_rank

    @staticmethod
    def player_birthdate_modification(player: dict):
        print("""Vous allez modifier la date de naissance du joueur : {}""".format(player["birthdate"]))
        new_birthdate = ""
        while not re.match(REGEX_BIRTHDATE, new_birthdate):
            new_birthdate = input("""Veuillez indiquer la nouvelle date de naissance du joueur (AAAA/MM/JJ)\n""")
            if not re.match(REGEX_BIRTHDATE, new_birthdate):
                print("""Vous devez rentrer une date sous le format : "AAAA-MM-JJ" """)
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["birthdate"], new_birthdate))
        return new_birthdate
