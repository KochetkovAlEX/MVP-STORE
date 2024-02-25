from abc import ABC, abstractmethod
from Core import Shoes
from typing import List
from View import IView, ConsoleView
from Model import IModel, Model
from Presenter import IPresenter, Presenter


def main():
    view: IView = ConsoleView()
    model: IModel = Model()
    presenter: IPresenter = Presenter(view=view, model=model)
    presenter.check_shoes()


if __name__ == '__main__':
    main()
