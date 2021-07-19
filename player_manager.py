import json
from typing import Union
from player import Player


class PlayerManager:

    def __init__(self):
        self.players = []

    def create(self, player_data: Union[dict, list]):
        if isinstance(player_data, dict):
            player = Player(*player_data.values())
            self.players.append(player.serialize())
            return player
        if isinstance(player_data, list):
            player = Player(*player_data)
            if not player.ID:
                new_ID = 1
                ID_free = False
                while ID_free is False:
                    ID_free = True
                    for p in self.players:
                        if new_ID == p["ID"]:
                            ID_free = False
                            new_ID += 1
                player.ID = new_ID
            self.save_player(player)
            return player

    def new_player(
                   self, first_name: str, last_name: str, birthdate: str, gender: str,
                   rank: int = 3000
                   ):
        return self.create(list([first_name, last_name, birthdate, gender, rank]))

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

    def sort_players(self, by_rank: bool = False):
        return sorted(
            self.players, key=lambda item: (
                item.get("last_name"), item.get("first_name"), int(item.get("rank"))) if not by_rank
            else (int(item.get("rank")), item.get("first_name"), item.get("last_name"))
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

if __name__ == "__main__":
    print(player_manager.players)
