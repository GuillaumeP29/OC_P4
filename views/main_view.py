class MainView:
    @staticmethod
    def main():
        print("Bienvenue dans le menu principal du programme de tournoi Suisse de jeu d'échec")
        print("Que souhaitez-vous faire ?")
        entry = ""
        entry_list = ("1", "2", "3")
        while entry not in entry_list:
            entry = input("""\
                \n1: Gérer un tournoi\
                \n2: Accéder aux archives\
                \n3: quitter le programme\
                \n""")
            if entry not in entry_list:
                print("Vous devez rentrer une des valeur suivantes : {}".format(entry_list))
        return int(entry)

    @staticmethod
    def display_menu():
        print("""Bienvenue dans les archives du programme. Que souhaitez-vous faire ?""")
        entry = ""
        entry_list = ("0", "1", "2", "3")
        while entry not in entry_list:
            entry = input("""\
            \n0 : Retourner à l'accueil\
            \n1 : Voir les tournois\
            \n2 : Voir les joueurs\
            \n3 : Quitter le programme\
            \n""")
            if entry not in entry_list:
                print("Vous devez rentrer une des valeur suivantes : {}".format(entry_list))
        return int(entry)

    @staticmethod
    def confirmation():
        entry = ""
        entry_list = ("0", "1")
        while entry not in entry_list:
            entry = (input("""\n0 : Non\n1 : Oui\n"""))
            if entry not in entry_list:
                print("Vous devez rentrer une des valeur suivantes : {}".format(entry_list))
        return int(entry)

    @staticmethod
    def data_changed(data: str):
        print("{} remplacé(e)".format(data))

    @staticmethod
    def quit():
        print("Vous avez choisi de quitter le programme. À bientôt !")
