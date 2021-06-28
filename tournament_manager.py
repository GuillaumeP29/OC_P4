import json
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

    def create(self, tournament: dict):
        """Create the tournament"""
        if isinstance(tournament, dict):
            tournament = Tournament(*tournament.values())
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

    def save_tournament(self, tournament: Tournament):
        """save a tournament in self.tournaments then write self.tournaments in a json file"""
        for saved_tournament in self.tournaments:
            if tournament.ID == saved_tournament["ID"]:
                self.tournaments.remove(saved_tournament)
        self.tournaments.append(tournament.serialize())
        with open('JSON/tournaments.json', 'w') as f:
            json.dump(self.tournaments, f, indent=4)


tournament_manager = TournamentManager()
