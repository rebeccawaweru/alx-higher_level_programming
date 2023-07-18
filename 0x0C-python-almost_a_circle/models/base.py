#!/usr/bin/python3
"""Define a new class Base"""
import json
import csv
import turtle


class Base:
    """Representing class Base
    Attribute: __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new instance of class Base
        Attribute:
        id - expected to be an integer
        __nb_objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string representation of object to a file"""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance where all attributes are set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for
                             dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                csv_string = cls.to._csv_string(obj)
                writer.writerow(csv_string)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV"""
        filename = cls.__name.__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    csv_string = ','.join(row)
                    instance = cls.from_csv_string(csv_string)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Drawing rectangles and squares using turtle module

        Arguments:
        list_rectangles: a list of Rectangles to draw
        list_squares : a list of Squares to draw
        """
        tut = turtle.Turle()
        tut.screen.bgcolor("#b9392c")
        tut.pensize(4)
        tut.shape("turtle")
        tut.color("#000000")
        for rectangle in list_rectangles:
            tut.showturtle()
            tut.up()
            tut.goto(rectangle.x, rectangle.y)
            tut.down()
            for j in range(2):
                tut.forward(rectangle.width)
                tut.left(90)
                tut.forward(rectangle.height)
                tut.left(90)
            tut.hideturtle()

        tut.color("#b5f7d6")
        for squr in list_squares:
            tut.showturtle()
            tut.up()
            tut.goto(squr.x, squr.y)
            tut.down()
            for j in range(2):
                tut.forward(squr.width)
                tut.left(90)
                tut.forward(squr.height)
                tut.left(90)
            tut.hideturtle()

        turtle.exitonclick()
