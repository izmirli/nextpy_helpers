"""Test exercise 2.2.2 implementation.

Usage:
pytest test_octopus.py
"""
import re
import inspect
import ch02_oop.octopus as octopus


class TestOctopus:

    def test_init(self):
        self.oct = octopus.Octopus()
        oct_members = {k: v for k, v in inspect.getmembers(self.oct)}
        assert 'name' in oct_members and isinstance(oct_members['name'], str), "Octopus has 'name' str attribute"
        assert 'age' in oct_members and isinstance(oct_members['age'], int), "Octopus has 'age' int attribute"
        assert 'birthday' in oct_members and inspect.ismethod(oct_members['birthday']), "Octopus has 'birthday' method"
        self.oct2 = octopus.Octopus()
        assert self.oct.name == self.oct2.name, "2 Octopus instances has same name"
        assert self.oct.age == self.oct2.age, "2 Octopus instances has same age"

    def test_main(self, capsys):
        octopus.main()
        captured = capsys.readouterr()
        match = re.search(r'(?:\s|^)(\d+)(?:\W|$)\D*(\d+)(?:\W|$)', captured.out.strip())  # , re.MULTILINE)
        assert match, "Two number (age for both instances) printed"
        age1, age2 = int(match.group(1)), int(match.group(2))
        print(f"\n---\norg: '{captured.out.strip()}'\nage1: {age1}, age2: {age2};")
        assert age1 + 1 == age2 or age1 == age2 + 1, "age difference is 1"

