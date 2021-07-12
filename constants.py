# Players regex
REGEX_PLAYER_ID = r'^[0-9]{1,4}$'
REGEX_FIRST_NAME = r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,30}$'
REGEX_LAST_NAME = r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,30}$'
REGEX_BIRTHDATE = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
REGEX_RANK = r'^[0-9]{1,4}$'

# Tournaments regex
REGEX_TOURNAMENT_NAME = r'^[0-9a-zA-Z- àéèçîôâûùäëïüö]{2,100}$'
REGEX_LOCATION = r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,50}$'
REGEX_DATE = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
REGEX_DESCRIPTION = r'^[0-9a-zA-Z- àéèçîôâûùäëïüö]{2,250}$'
REGEX_NUMBER_OF_PLAYERS = r'^[0-9]{1,2}$'
REGEX_NUMBER_OF_ROUNDS = r'^[2-8]{1}$'
REGEX_TOURNAMENT_NUMBER = r'^[0-9]{1,3}$'
