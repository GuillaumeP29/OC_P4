import json
import random
from typing import Union
from tournament import Tournament


class TournamentManager:

    def __init__(self):
        self.tournaments = []

    def load_from_json(self):
        """Load the whole tournaments.json file into """
        with open("JSON/tournaments.json") as f:
            tournaments = json.load(f)
            for tournament_data in tournaments:
                self.tournaments.append(tournament_data)

    def create(self, tournament: Union[dict, list]):
        """Create the tournament"""
        if isinstance(tournament, dict):
            tournament = Tournament(*tournament.values())
        elif isinstance(tournament, list):
            tournament = Tournament(*tournament)
        else:
            raise AttributeError("le paramètre entré dans la méthode create doit être un dictionnaire ou une liste")
        return tournament

    def unserialize_tournament(self, tournament_ID: str):
        """Load a specific tournament from the self.tournaments list"""
        for tournament_data in self.tournaments:
            if tournament_data["ID"] == tournament_ID:
                return self.create(tournament_data)
        raise AttributeError("le tournois demandé n'a pas été trouvé dans la liste de tournois")

    def new_tournament(
        self, name: str, location: str, date: str, time_control: str, description: str,
        number_of_players: int, number_of_rounds: int = 4
    ):
        """Create a new tournament from user's values"""
        tournament = [name, location, date, time_control, description, number_of_players, number_of_rounds]
        return self.create(tournament)

    def sort_tournaments(self, by_date: bool = False):
        sorted_list = sorted(
            self.tournaments, key=lambda item: (item.get("name"), item.get("date")) if not by_date
            else (item.get("date"), item.get("name"))
            )
        return sorted_list

    def save_tournament(self, tournament: Tournament):
        """save a tournament in self.tournaments then write self.tournaments in a json file"""
        for saved_tournament in self.tournaments:
            if tournament.ID == saved_tournament["ID"]:
                self.tournaments.remove(saved_tournament)
        self.tournaments.append(tournament.serialize())
        with open('JSON/tournaments.json', 'w') as f:
            json.dump(self.tournaments, f, indent=4)


tournament_manager = TournamentManager()


if __name__ == "__main__":
    tournament_manager.load_from_json()

    # tournament_name = "Tournament test"

    # tournament = tournament_manager.unserialize_tournament(tournament_name)

    # tournament_manager.save_tournament(tournament)

    name = "tournois pb"
    location = "Brech"
    date = "2021-06-01"
    time_control = "Bullet"
    description = "petit tournois pour essayer"
    number_of_players = 8
    number_of_rounds = 4

    tournament = tournament_manager.new_tournament(
        name, location, date, time_control, description, number_of_players,
        number_of_rounds
    )
    player_list = []
    for n in range(number_of_players):
        player_list.append(n + 1)
    tournament.players = player_list
    for round in range(number_of_rounds):
        round_number = round + 1
        tournament.create_round(round_number)
        print("round {} crée !".format(round_number))
        scores = []
        for match in range(4):
            score = random.randrange(0, 3, 1)
            scores.append(score)
        tournament.set_scores(scores)
    tournament_manager.save_tournament(tournament)
