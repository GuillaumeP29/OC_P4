import json
from player import Player


class PlayerManager:

    def __init__(self):
        self.players = []

    def create(self, player_data: dict):
        if isinstance(player_data, dict):
            player = Player(*player_data.values())
            self.players.append(player.serialize())
            return player

    def load_from_json(self):
        with open("JSON/players.json") as f:
            self.players = []
            players = json.load(f)
            for player_data in players:
                self.players.append(player_data)

    def load_player(self, ID: int) -> Player:
        player_found = False
        for player_data in self.players:
            if player_data["ID"] == ID:
                player = {}
                player["ID"] = ID
                player["score"] = 0.0
                player["rank"] = player_data["rank"]
                return player
        if not player_found:
            raise AttributeError(
                """Aucun joueur ayant pour ID {} n'a été trouvée dans la base de donnée
                "players.json" (L'ID doit être un nombre entre 1 et 3000, inclus)""".format(ID)
                )

    def save_player(self, player: Player = None):
        """save a tournament in self.tournaments then write self.tournaments in a json file"""
        if player:
            player_exist = False
            for saved_player in self.players:
                if player.ID == saved_player["ID"]:
                    player_exist = True
            if player_exist is False:
                self.players.append(player.serialize())
        with open('JSON/players.json', 'w') as f:
            json.dump(self.players, f, indent=4)


player_manager = PlayerManager()
player_manager.load_from_json()
