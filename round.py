class Round:

    def __init__(self, round_number: int, number_of_players: int, matchs: dict = None):
            self.round_number = round_number
            self.number_of_players = number_of_players
            self.number_of_matchs = int(number_of_players / 2)
            self.matchs = matchs
            self.name = round_number
            self.ID_tuple = []
