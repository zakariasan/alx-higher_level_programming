#!/usr/bin/python3
"""
Class : Base
"""
import json


class Base:
    """desc of Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """desc of json to string """
        if (list_dictionaries is None):
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """desc save_to_file"""
        name = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is not None:
            for item in list_objs:
                if isinstance(item, cls):
                    list_dic.append(item.to_dictionary())
        with open(name, 'w', encoding='utf-8') as target:
            target.write(Base.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """desc of from_json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """desc of create"""
        if cls.__name__ == 'Rectangle':
            dummy_inst = cls(4, 4)
        elif cls.__name__ == 'Square':
            dummy_inst = cls(2)
        else:
            dummy_inst = cls()
        dummy_inst.update(**dictionary)

        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """desc of load from_json_string"""
        name = "{}.json".format(cls.__name__)
        try:

            with open(name, 'r', encoding='utf-8') as target:
                json_string = target.read()
                list_dic = cls.from_json_string(json_string)
                return [cls.create(**obj) for obj in list_dic]
        except FileNotFoundError:
            return []
