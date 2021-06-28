class Match:
    def __init__(self, player1: int, player2: int, result1: float = None, result2: float = None):
            self.player1 = player1
            self.player2 = player2
            self.result1 = result1
            self.result2 = result2    
            
    @property
    def player1(self) -> int:
        return self.__player1

    @player1.setter
    def player1(self, value: int):
        if isinstance(value, int):
            if 0 < value <= 3000:
                self.__player1 = value
            else:
                raise AttributeError("Le joueur 1 doit être un nombre entier positif (ID du joueur)")
        else:
            raise AttributeError("Le joueur 1 doit être un nombre entier positif (ID du joueur)")

    @property
    def player2(self) -> int:
        return self.__player2

    @player2.setter
    def player2(self, value: int):
        if isinstance(value, int):
            if 0 < value <= 3000:
                self.__player2 = value
            else:
                raise AttributeError("Le joueur 2 doit être un nombre entre 1 et 3000 (ID du joueur)")
        else:
            raise AttributeError("Le joueur 2 doit être un nombre entre 1 et 3000 (ID du joueur)")

    @property
    def result1(self) -> float:
        return self.__result1

    @result1.setter
    def result1(self, value: float):
        if value is None:
            self.__result1 = value
        elif isinstance(value, float):
            if 0 <= value <= 1:
                self.__result1 = value
            else:
                raise AttributeError("Le résultat du joueur 1 doit être entre 0 et 1 inclus")
        else:
            raise AttributeError("Le résultat du joueur 1 doit être un nombre entre 0 et 1")

    @property
    def result2(self) -> float:
        return self.__result2

    @result2.setter
    def result2(self, value: float):
        if value is None:
            self.__result2 = value
        elif isinstance(value, float):
            if 0 <= value <= 1:
                self.__result2 = value
            else:
                raise AttributeError("Le résultat du joueur 2 doit être entre 0 et 1 inclus")
        else:
            raise AttributeError("Le résultat du joueur 2 doit être un nombre entre 0 et 1")

    def set_result(self, winner: int):
        if winner == 0:
            self.result1 = 0.5
            self.result2 = 0.5
        elif winner == 1:
            self.result1 = 1.0
            self.result2 = 0.0
        elif winner == 2:
            self.result1 = 0.0
            self.result2 = 1.0
        else:
            raise AttributeError(
                                 """La fonction set_result ne peut recevoir que 0 (pour églité), 1 (pour victoire du
                                 joueur 1) ou 2 (pour victoire du joueur 2) en paramètre"""
                                )

    def serialize(self) -> dict:
        return {
            "player 1": {"ID": self.player1, "score": self.result1},
            "player 2": {"ID": self.player2, "score": self.result2}
        }
