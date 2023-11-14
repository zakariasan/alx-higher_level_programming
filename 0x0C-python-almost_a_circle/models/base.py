#!/usr/bin/python3
"""
Class : Base
"""
import json
import csv


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
            return "[]"
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """desc of load save to a csv_file"""

        file_name = "{}".format(cls.__name__)
        with open(file_name, 'w', newline='') as target:
            str = csv.writer(target)
            for item in list_objs:
                if cls.__name__ == "Rectangle":
                    str.writerow([item.id, item.width, item.height, item.x,
                                  item.y])
                elif cls.__name__ == "Square":
                    str.writerow([item.id, item.size, item.x, item.y])

    @classmethod
    def load_from_file_csv(cls):
        file_name = "{}".format(cls.__name__)
        try:
            with open(file_name, 'r', encoding='utf-8') as target:
                str = csv.reader(target)
                if cls.__name__ == "Rectangle":
                    return [cls.create(width=int(row[1]), height=int(row[2]),
                                       x=int(row[3]), y=int(row[4]),
                                       id=int(row[0])) for row in str]

                elif cls.__name__ == "Square":
                    return [cls.create(size=int(row[1]), x=int(row[2]),
                                       y=int(row[3]),
                                       id=int(row[0])) for row in str]
        except FileNotFoundError:
            return []
