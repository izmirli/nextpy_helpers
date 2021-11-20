"""ETest exercise 2.3.3 - next.py course.

Usage:
pytest test_octopus2.py
"""
import inspect
import re
import ch02_oop.octopus2 as octopus


class TestOctopus:

    # def __init__(self):
    #     self.started = True

    def test01_init(self):
        self.oct = octopus.Octopus2()
        attributes = self.get_obj_attributes()
        assert len(attributes['private']) >= 2
        assert '_name' in attributes['private'] \
               and isinstance(self.oct._name, str) \
               and self.oct._name == "Octavio"
        assert '_age' in attributes['private'] \
               and isinstance(self.oct._age, int)
        self.oct2 = octopus.Octopus2('oct2')
        assert self.oct2._name == 'oct2'

    def test02_set_name(self):
        self.oct2.set_name('Octopussy')
        assert self.oct2._name == 'Octopussy'

    def test03_get_name(self):
        assert self.oct.get_name() == "Octavio"

    def test04_count_animals(self):
        assert octopus.Octopus2.count_animals == 3

    def get_obj_attributes(self, obj: object = None) -> dict:
        attributes = {'visible': [], 'private': [], 'magic': []}
        obj = self.oct if obj is None else obj
        for attr_name, attr_val in inspect.getmembers(obj):
            if re.fullmatch(r'__.+__', attr_name):
                attributes['magic'].append(attr_name)
            elif attr_name.startswith('_'):
                attributes['private'].append(attr_name)
            else:
                attributes['visible'].append(attr_name)

        return attributes
