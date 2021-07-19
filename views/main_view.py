class MainView:
    @staticmethod
    def main():
        print("Bienvenue dans le menu principal du programme de tournoi Suisse de jeu d'échec")
        print("Que souhaitez-vous faire ?")

    @staticmethod
    def main_menu():
        entry = input("""\
            \n1: Gérer un tournoi\
            \n2: Accéder aux archives\
            \n3: quitter le programme\
            \n""")
        return entry

    @staticmethod
    def correct_value(entry_list):
        print("Vous devez rentrer une des valeur suivantes : {}".format(entry_list))

    @staticmethod
    def error(error):
        print(error)

    @staticmethod
    def ID_error(higher_ID):
        print("Le nombre doit être entier et se situer entre 0 et {}".format(higher_ID))

    @staticmethod
    def display_menu():
        print("""Bienvenue dans les archives du programme. Que souhaitez-vous faire ?""")
        entry = input("""\
        \n0 : Retourner à l'accueil\
        \n1 : Voir les tournois\
        \n2 : Voir les joueurs\
        \n3 : Quitter le programme\
        \n""")
        return entry

    @staticmethod
    def confirmation():
        entry = (input("""\n0 : Non\n1 : Oui\n"""))
        return entry

    @staticmethod
    def data_changed(data: str):
        print("{} remplacé(e)".format(data))

    @staticmethod
    def quit():
        print("Vous avez choisi de quitter le programme. À bientôt !")
