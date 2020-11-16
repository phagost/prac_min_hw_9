from __future__ import annotations
from abc import ABC, abstractmethod

class CharCreator(ABC):

    @abstractmethod
    def create_char(self):
        pass

    def operations(self) -> str:
        char = self.create_char()
        result = f"The character is created: {char.operation()}"
        return result

class CounterTerroristCreator(CharCreator):
    def create_char(self) -> Char:
        return CounterTerrorist()

class TerroristCreator(CharCreator):
    def create_char(self) -> Char:
        return Terrorist()

class HostageCreator(CharCreator):
    def create_char(self) -> Char:
        return Hostage()

class Char(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class CounterTerrorist(Char):
    def operation(self) -> str:
        return "{counter terrorist}"

class Terrorist(Char):
    def operation(self) -> str:
        return "{terrorist}"

class Hostage(Char):
    def operation(self) -> str:
        return "{hostage}"

def client_code(method: CharCreator) -> None:
    print(f"{method.operations()}", end="")

if __name__ == "__main__":

    print("Counter terrorist creation")
    client_code(CounterTerroristCreator())
    print("\n")

    print("Terrorist creation")
    client_code(TerroristCreator())
    print("\n")

    print("Hostage creation")
    client_code(HostageCreator())
    print("\n")