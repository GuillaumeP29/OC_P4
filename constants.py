# Regex
REGEX_TOURNAMENT_NAME = r'^[0-9a-zA-Z- àéèçîôâûùäëïüö]{2,100}$'
REGEX_LOCATION = r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,50}$'
REGEX_DATE = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
REGEX_DESCRIPTION = r'^[0-9a-zA-Z- àéèçîôâûùäëïüö]{2,250}$'
REGEX_NUMBER_OF_PLAYERS = r'^[0-9]{1,2}$'
REGEX_NUMBER_OF_ROUNDS = r'^[2-8]{1}$'
REGEX_TOURNAMENT_NUMBER = r'^[0-9]{1,3}$'
REGEX_PLAYER_ID = r'^[0-9]{1,4}$'
REGEX_FIRST_NAME = r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,30}$'
REGEX_LAST_NAME = r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,30}$'
REGEX_RANK = r'^[0-9]{1,4}$'

# Error messages
DATE_ERROR = """Vous devez rentrer une date sous le format : "AAAA-MM-JJ" """
TOURNAMENT_NAME_ERROR = """Le nom du tournoi doit faire entre 2 et 100 caractères"""
TOURNAMENT_LOCATION_ERROR = """
    Le lieu du tournoi doit faire entre 2 et 50 caractères et ne doit pas comporter de chiffre
"""
TOURNAMENT_DESCRIPTION_ERROR = """La description du tournoi doit faire entre 2 et 250 caractères"""
NUMBER_OF_PLAYERS_ERROR = """Veuillez entrer un nombre entre 8 et 99"""
NUMBER_OF_ROUNDS_ERROR = """Veuillez entrer un nombre entre 2 et 8"""
PLAYER_FIRST_NAME_ERROR = """
    Le prénom du joueur doit faire entre 2 et 30 caractères et ne doit pas comporter de chiffre
"""
PLAYER_LAST_NAME_ERROR = """
    Le nom de famille du joueur doit faire entre 2 et 30 caractères et ne doit pas comporter de chiffre
"""
RANK_ERROR = """Le rang du joueur doit être un nombre compris entre 1 et 3000"""
