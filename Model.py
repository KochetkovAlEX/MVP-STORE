from abc import ABC, abstractmethod
from Core import Shoes


class DataBase:
    male_db: list[Shoes] = [
        Shoes("м", "кроссовки", "красный", 'пума', 42, 5999),
        Shoes("м", "кроссовки", "красный", 'пума', 41, 5999),
        Shoes("м", "туфли", "белый", '...', 42, 7999),
    ]

    female_db: list[Shoes] = [
        Shoes("ж", "кроссовки", "красный", 'пума', 42, 5999),
        Shoes("ж", "кроссовки", "красный", 'пума', 41, 5999),
        Shoes("ж", "туфли", "белый", '...', 42, 7999),
    ]

    def get_male_db(self):
        return self.male_db

    def get_female_db(self):
        return self.female_db


class IModel(ABC):
    @abstractmethod
    def check_shoes(self, shoes: Shoes):
        pass


class Model(IModel):
    def __init__(self):
        self.db = DataBase()

    def check_shoes(self, shoes: Shoes):
        if shoes.gender.lower() == 'м':
            all_info = self.db.get_male_db()
        elif shoes.gender.lower() == 'ж':
            all_info = self.db.get_female_db()
        else:
            return "..."
        for i in all_info:
            if i.type == shoes.type.lower() and i.gender == shoes.gender.lower() and i.size == shoes.size and \
                    i.creator == shoes.creator.lower() and i.cost == shoes.cost and i.color == shoes.color.lower():
                return True
        return False

