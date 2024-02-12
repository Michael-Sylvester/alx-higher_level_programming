#!/usr/bin/python3
"""Base class module"""
import json
import io


class Base:
    """Base class for manging instance ID"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initialization"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        jsonlist = json.dumps(list_dictionaries)
        return jsonlist

    @classmethod
    def save_to_file(cls, list_objs):
        """converts list of objects to """
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as json_file:
            jsonstring = ""
            if list_objs is None or list_objs == []:
                jsonstring = cls.to_json_string(list_objs)
            else:
                objdics_list = list()
                for object in list_objs:
                    objdics_list.append(object.to_dictionary())
                jsonstring = cls.to_json_string(objdics_list)
            json_file.write(jsonstring)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        obj_list = list(json.loads(json_string))
        return obj_list
    
    @classmethod
    def create(cls, **dictionary):
            if cls.__name__ == "Rectangle":
                dummy = cls(2, 1)
            else:
                dummy = cls(3)
            dummy.update(**dictionary)
            return dummy
