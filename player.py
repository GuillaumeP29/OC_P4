from typing import Union
import datetime
import re
import enum


class Player:

    class Gender(enum.Enum):
        Male = "M"
        Female = "F"

    def __init__(
                 self, first_name: str, last_name: str, birthdate: str, gender: str,
                 rank: int = 3000, ID: int = None
                ):
        errors = []
        try:
            self.first_name = first_name
        except AttributeError as e:
            errors.append(("first_name", str(e)))
        try:
            self.last_name = last_name
        except AttributeError as e:
            errors.append(("last_name", str(e)))
        try:
            self.birthdate = birthdate
        except AttributeError as e:
            errors.append(("birthdate", str(e)))
        try:
            self.gender = gender
        except AttributeError as e:
            errors.append(("gender", str(e)))
        try:
            self.rank = rank
        except AttributeError as e:
            errors.append(("rank", str(e)))
        try:
            self.ID = ID
        except AttributeError as e:
            errors.append(("ID", str(e)))
        if errors:
            raise Exception(errors)

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if (isinstance(value, str) and re.match(r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,10}$', value)):
            self.__first_name = value
        else:
            raise AttributeError("Veuillez rentrer une chaîne de caractères")

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        if (isinstance(value, str) and re.match(r'^[a-zA-Z- àéèçîôâûùäëïüö]{2,10}$', value)):
            self.__last_name = value
        else:
            raise AttributeError("Veuillez rentrer une chaîne de caractères")

    @property
    def birthdate(self) -> Union[str, datetime.date]:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value: Union[str, datetime.date]):
        if isinstance(value, str):
            try:
                self.__birthdate = datetime.date.fromisoformat(value)
            except ValueError:
                raise AttributeError("Veuillez entrer une date selon le format suivant : AAAA-MM-JJ : ")
        if isinstance(value, datetime.date):
            self.__birthdate = value
        if not (isinstance(value, str) or isinstance(value, datetime.date)):
            raise AttributeError("Veuillez entrer une date selon le format suivant : AAAA-MM-JJ : ")

    @property
    def gender(self) -> Gender:
        return self.__gender

    @gender.setter
    def gender(self, value: Union[str, Gender]):  # si bug, rajouter "Player." devant Gender
        if (value == "F" or value == "M"):
            self.__gender = value
        else:
            raise AttributeError("Veuillez entrer F pour féminin ou M pour masculin")

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, value: int):
        if (isinstance(value, int) and 0 <= value <= 3000):
            self.__rank = value
        else:
            raise AttributeError("Veuillez entrer une valeur entre 1 et 3000")

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, value: Union[int, None]):
        if value is None:
            value = value
        elif isinstance(value, int):
            if value > 0:
                value = value
            else:
                raise AttributeError("L'identifiant ne doit pas être un entier négatif ou nul")
        else:
            raise AttributeError("L'identifiant devrait être un nombre entier supérieur à 0")
        self.__ID = value

    def serialize(self) -> dict:
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "rank": self.rank,
            "ID": self.ID
        }