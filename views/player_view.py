import re
from views.main_view import MainView
from constants import *


class PlayerView:
    @staticmethod
    def way_to_add_player(player: int):
        print("Comment voulez-vous ajouter le joueur N°{} ?".format(player + 1))
        entry = input("1: Ajouter un joueur depuis la liste de joueurs\n2: Créer un nouveau joueur\n")
        return entry

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
    def selected_player(players_ID: list):
        print("Joueurs déjà choisis : {}".format(players_ID))

    @staticmethod
    def select_player():
        player_ID = input("Entrez l'ID du joueur à sélectionner : ")
        return player_ID

    @staticmethod
    def already_selected_player(player_ID):
        print("Le joueur {} ne peut pas être sélectionné une seconde fois".format(player_ID))

    @staticmethod
    def player_first_name():
        first_name = input("Quel est le prénom du joueur ? ")
        return first_name

    @staticmethod
    def player_first_name_modification(player: dict):
        print("""Vous allez modifier le prénom du joueur : {}""".format(player["first_name"]))

    @staticmethod
    def player_first_name_confirmation(player: dict, new_first_name):
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["first_name"], new_first_name))

    @staticmethod
    def player_last_name():
        last_name = input("Quel est le nom de famille du joueur ? ")
        return last_name

    @staticmethod
    def player_last_name_modification(player: dict):
        print("""Vous allez modifier le nom de famille du joueur : {}""".format(player["last_name"]))

    @staticmethod
    def player_last_name_confirmation(player: dict, new_last_name):
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["last_name"], new_last_name))

    @staticmethod
    def birthdate():
        birthdate = input("Veuillez entrer la date de naissance du joueur (AAAA/MM/JJ) : ")
        return birthdate

    @staticmethod
    def player_birthdate_modification(player: dict):
        print("""Vous allez modifier la date de naissance du joueur : {}""".format(player["birthdate"]))

    @staticmethod
    def player_birthdate_confirmation(player: dict, new_birthdate):
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["birthdate"], new_birthdate))

    @staticmethod
    def gender():
        gender = input("Quel est le sexe du joueur (M ou F) ? ")
        return gender

    @staticmethod
    def ranked(first_name, pronoun, termination):
        ranked = input(
            "{} est-{} classé{} (1: Oui ; 2: Non) ? ".format(first_name, pronoun, termination)
        )
        return ranked

    @staticmethod
    def rank():
        rank = input("Quel est le rang du joueur ? ")
        return rank

    @staticmethod
    def rank_modification(player: dict):
        print("""Vous allez modifier le rang du joueur : {}""".format(player["rank"]))

    @staticmethod
    def rank_confirmation(player: dict, new_rank):
        print("""Souhaitez vous vraiment remplacer "{}" par "{}" ? """.format(
            player["rank"], new_rank))

    @staticmethod
    def display_player_menu():
        entry = input("""\
            \n0 : Retourner au menu précédent\
            \n1 : Afficher les joueurs par rang\
            \n2 : Afficher les joueurs par nom\
            \n3 : Créer un nouveau joueur\
            \n4 : Quitter le programme\
            \n""")
        return entry

    @staticmethod
    def player_choice_menu():
        player_ID = input("""\
            \nSouhaitez-vous afficher un joueur ?\
            \nOui : Veuillez indiquer l'ID du joueur qui vous intéresse\
            \nNon : Entrez '0' pour retourner au menu précédent\
            \n""")
        return player_ID

    @staticmethod
    def player_modification():
        entry = input("""\
            \nSouhaitez-vous modifier le joueur ?\
            \n1 : Oui\
            \n0 : Non, retourner au menu précédent\
            \n""")
        return entry

    @staticmethod
    def player_modification_menu():
        entry = input("""Que souhaitez-vous modifier ?\
            \n0 : Rien, annuler la modification\
            \n1 : Le prénom du joueur\
            \n2 : Le nom de famille du joueur\
            \n3 : Le rang du joueur\
            \n4 : La date de naissance du joueur\
            \n""")
        return entry
