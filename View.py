from abc import ABC, abstractmethod
from Core import Shoes


class IView(ABC):
    @abstractmethod
    def search(self) -> Shoes:
        pass

    @abstractmethod
    def found(self, result: bool) -> None:
        pass


class ConsoleView(IView):
    def search(self) -> Shoes:
        return Shoes(gender=input("М / Ж ? \n"), type=input("Вид обуви: \n"), color=input("Цвет: \n"),
                     creator=input('Производитель: \n'), size=int(input("Размер: \n")), cost=int(input("Цена: ")))

    def found(self, result: bool) -> None:
        print(result)


