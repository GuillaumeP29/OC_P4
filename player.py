class Player:
    def __init__(
                 self, first_name: str, last_name: str, birthdate: str, gender: str,
                 rank: int = 3000, ID: int = None
                ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.ID = ID
