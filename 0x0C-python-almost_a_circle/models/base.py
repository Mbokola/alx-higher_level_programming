#!/usr/bin/python3
""" base module """
import json
import csv


class Base:
    """ The Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        dict_list = [obj.to_dictionary() for obj in list_objs]
        string_rep = Base.to_json_string(dict_list)
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as f:
            f.write(string_rep)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy_instance = cls(1, 1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                content = f.read()
                obj = Base.from_json_string(content)
                instances = [cls.create(**dictionary) for dictionary in obj]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialize list_objs to a csv file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialize instance from csv file """
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, 'r') as f:
            content = csv.reader(f)
            for row in content:
                if cls.__name__ == "Rectangle":
                    instances.append(cls.create(id=int(row[0]),
                                                width=int(row[1]),
                                                height=int(row[2]),
                                                x=int(row[3]), y=int(row[4])))
                elif cls.__name__ == "Square":
                    instances.append(cls.create(id=int(row[0]),
                                                size=int(row[1]),
                                                x=int(row[2]), y=int(row[3])))
        return instances
