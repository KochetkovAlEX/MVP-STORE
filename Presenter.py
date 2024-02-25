from abc import ABC, abstractmethod
from Core import Shoes
from typing import List
from View import IView
from Model import IModel


class IPresenter(ABC):
    @abstractmethod
    def check_shoes(self):
        pass


class Presenter(IPresenter):
    def __init__(self, model: IModel, view: IView):
        self.model = model
        self.view = view

    def check_shoes(self):
        shoes: Shoes = self.view.search()
        result = self.model.check_shoes(shoes)
        self.view.found(result)