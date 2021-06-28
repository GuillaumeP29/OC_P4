class Match:
    def __init__(self, player1: int, player2: int, result1: float = None, result2: float = None):
            self.player1 = player1
            self.player2 = player2
            self.result1 = result1
            self.result2 = result2

    def serialize(self) -> dict:
        return {
            "player 1": {"ID": self.player1, "score": self.result1},
            "player 2": {"ID": self.player2, "score": self.result2}
        }
