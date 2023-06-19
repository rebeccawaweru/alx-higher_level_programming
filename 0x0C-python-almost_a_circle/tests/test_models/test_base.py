#!/usr/bin/python3
"""Base class unittests"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

    def test_class_member(self):
        """Base class unittest"""
        b0 = Base()
        self.assertIsInstance(b0, Base)

    def test_no_id(self):
        """Base class ids unittest"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 7)
        self.assertEqual(b2.id, 8)
        self.assertEqual(b3.id, 9)

    def test_id_and_no_id(self):
        """Base class ids unittest"""
        b4 = Base(5)
        b5 = Base()
        self.assertEqual(b4.id, 5)
        self.assertEqual(b5.id, 10)

    def test_to_json_string(self):
        """to_json_string method unittest"""
        rec = Rectangle(12, 8, 4, 6)
        rd = rec.to_dictionary()
        self.assertIsInstance(rd, dict)
        json_rd = Base.to_json_string([rd])
        self.assertIsInstance(json_rd, str)

        s = Square(10)
        sq = s.to_dictionary()
        self.assertIsInstance(sq, dict)
        json_sq = Base.to_json_string([sq])
        self.assertIsInstance(json_sq, str)

    def test_save_to_file(self):
        """save_to_file unittest"""
        rx = Rectangle(11, 8, 4, 5)
        ry = Rectangle(3, 5)
        Rectangle.save_to_file([rx, ry])
        arry = []
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            arry = json.load(f)
        self.assertIsInstance(arry, list)
        self.assertEqual(len(arry), 2)
        ref_arry = [
            {'id': 10, 'height': 8, 'x': 3, 'width': 12, 'y': 5},
            {'id': 11, 'height': 7, 'x': 0, 'width': 13, 'y': 0}
        ]
        self.assertListEqual(arry, ref_arry)

        Square.save_to_file([])
        arry = []
        with open('Square.json', 'r', encoding='utf-8') as f:
            arry = json.laod(f)
        self.assertIsInstance(arry, list)
        self.assertEqual(len(arry), 0)

        sx = Square(2, x=1, y=2, id=98)
        sy = Square(3, x=5, y=7, id=99)
        Square.save_to_file([sx, sy])
        arry = []
        with open('Square.json', 'r', encoding='utf-8') as f:
            arry = json.load(f)
        self.assertIsInstance(arry, list)
        self.assertEqual(len(arry), 2)
        ref_arry = [
           {'x': 1, 'id': 98, 'size': 2, 'y': 2},
           {'x': 5, 'id': 99, 'size': 3, 'y': 7}
        ]
        self.assertListEqual(arry, ref_arry)

    def test_from_json_string(self):
        """from_json_string method unittest"""
        arry = [
          {'id': 90, 'width': 12, 'height': 5},
          {'id': 5, 'width': 2, 'height': 9}
        ]
        input_json = Rectangle.to_json_string(arry)
        output = Rectangle.from_json_string(input_json)
        self.assertListEqual(output, arry)

        arry = []
        input_json = Rectangle.to_json_string(arry)
        output = Rectangle.from_json_string(input_json)
        self.assertListEqual(output, arry)

    def test_create_method(self):
        """Create method unittest"""
        rx = Rectangle(4, 5, 6)
        rx_dictionary = rx.to_dictionary()
        ry = Rectangle.create(**rx_dictionary)
        self.assertFalse(rx is ry)
        self.assertNotEqual(ry, rx)

        sx = Square(4, id=7, x=2, y=1)
        sx_dictionary = sx.to_dictionary()
        sy = Square.create(**sx_dictionary)
        self.assertFalse(sx is sy)
        self.assertNotEqual(sy, sx)

    def test_load_from_file_method(self):
        """load_from_file method unittest"""
        rx = Rectangle(12, 8, 3, 9, id=8)
        ry = Rectangle(2, 6, id=12)
        rect_input = [rx, ry]
        Rectangle.save_to_file(rect_input)
        output = Rectangle.load_from_file()

if __name__ == '__main__':
    unittest.main()
