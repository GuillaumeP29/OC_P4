class Tournament:

    def __init__(
        self, name: str, location: str, date: str, time_control: str, description: str,
        number_of_players: int, number_of_rounds: int = 4, ID: int = None, players: list = None, rounds: dict = None
    ):
            self.name = name
            self.location = location
            self.date = date
            self.time_control = time_control
            self.description = description
            self.number_of_players = number_of_players
            self.number_of_rounds = number_of_rounds
            self.ID = ID
            self.matchs_combinations = []
            self.players = players
            self.rounds = rounds

    def create_round(self, round_number: int):
        pass

    def set_scores(self, scores: list):
        pass

    def serialize(self) -> dict:
        return {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "time control": self.time_control,
                "description": self.description,
                "number_of_players": self.number_of_players,
                "number_of_rounds": self.number_of_rounds,
                "ID": self.ID,
                "players": self.players,
                "rounds": self.rounds
        }