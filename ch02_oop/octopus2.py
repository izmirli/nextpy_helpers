"""EX 2.3.3 - next.py course.

A. Write an "upgrade" to the Octopus class from previous task (2.2.2) by:
    1. Hide name & age attributes (using the underscore prefix).
    2. Enable setting name on initialization. If not set, use "Octavio".
    3. Add "set_name" method that changes the name attribute.
    4. Add "get_name" method that returns the name.
    5. Add, in the proper place, a "count_animals" attribute to
    count the number of instances created from this class.
B. Write main function that will:
    1. Make two instances - one with a name you give it, and one without.
    2. Print each instance name. Check one has the name you gave it,
       and the other has the default name.
    3. Change the name for one of them, and than print it with "get_name" method.
    4. Print count_animals value, and check it is: 2.
"""


class Octopus2:
    count_animals = 0

    def __init__(self, name: str = 'Octavio'):
        self._name = name
        self._age = 0
        Octopus2.count_animals += 1

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_age(self, age: int) -> None:
        self._age = age

    def birthday(self) -> None:
        self._age += 1

    def get_age(self) -> int:
        return self._age


def main():
    olee = Octopus2('Olee')
    oct = Octopus2()
    print(f'[t0] Octopus#1 name: {olee.get_name()}\tOctopus#2 name: {oct.get_name()}')

    oct.set_name('OctiOct')
    print(f'[t1] Octopus#1 name: {olee.get_name()}\tOctopus#2 name: {oct.get_name()}')

    print(f'Octopus.count_animals: {Octopus2.count_animals}')


if __name__ == '__main__':
    main()
