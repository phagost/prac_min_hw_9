from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

#The general builder for the CS player
class PlayerBuilder(ABC):

    def product(self) -> None:
        pass

    @abstractmethod
    def bulletproof_vest(self) -> None:
        pass

    @abstractmethod
    def cold_weapon(self) -> None:
        pass

    @abstractmethod
    def pistol(self) -> None:
        pass

    @abstractmethod
    def machine_gun(self) -> None:
        pass

    @abstractmethod
    def grenade(self) -> None:
        pass

    @abstractmethod
    def speciality(self) -> None:
        pass

#The specific builder for contr-terrorist
class CounterTerroristBuilder(PlayerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._char = CounterTerrorist()

    @property
    def char(self) -> CounterTerrorist:
        product = self._char
        self.reset()
        return product

    def bulletproof_vest(self) -> None:
        self._char.add("Bulletproof vest")

    def cold_weapon(self) -> None:
        self._char.add("Knife")

    def pistol(self) -> None:
        self._char.add("P250")

    def machine_gun(self) -> None:
        self._char.add("M4A1")

    def grenade(self) -> None:
        self._char.add("Smoke grenade")

    def speciality(self) -> None:
        self._char.add("Sapper set")

#The specific builder for terrorist
class TerroristBuilder(PlayerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._char = Terrorist()

    @property
    def char(self) -> Terrorist:
        product = self._char
        self.reset()
        return product

    def bulletproof_vest(self) -> None:
        self._char.add("Bulletproof vest")

    def cold_weapon(self) -> None:
        self._char.add("Knife")

    def pistol(self) -> None:
        self._char.add("P250")

    def machine_gun(self) -> None:
        self._char.add("AK47")

    def grenade(self) -> None:
        self._char.add("Frag grenade")

    def speciality(self) -> None:
        self._char.add("Bomb")

#Contrterrorist class
class CounterTerrorist():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Counterterrorist set is {', '.join(self.parts)}", end="")

#Terrorist class
class Terrorist():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Contrterrorist set is {', '.join(self.parts)}", end="")

#Director aka assembler
class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> PlayerBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PlayerBuilder) -> None:
        self._builder = builder

    """
    Директор может строить несколько вариаций продукта, используя одинаковые
    шаги построения.
    """

    def build_minimal_char_set(self) -> None:
        self.builder.cold_weapon()

    def build_full_char_set(self) -> None:
        self.builder.cold_weapon()
        self.builder.bulletproof_vest()
        self.builder.pistol()
        self.builder.machine_gun()
        self.builder.grenade()
        self.builder.speciality()

if __name__ == "__main__":

    director = Director()
    counterterrorist = CounterTerroristBuilder()
    director.builder = counterterrorist

    print("Initial counterterrorist set is: ")
    director.build_minimal_char_set()
    counterterrorist.char.list_parts()

    print("\n")

    print("Full counterterrorist set is: ")
    director.build_full_char_set()
    counterterrorist.char.list_parts()

    print("\n")

    director = Director()
    terrorist = TerroristBuilder()
    director.builder = terrorist

    print("Initial terrorist set is: ")
    director.build_minimal_char_set()
    terrorist.char.list_parts()

    print("\n")

    print("Full terrorist set is: ")
    director.build_full_char_set()
    terrorist.char.list_parts()

    print("\n")



