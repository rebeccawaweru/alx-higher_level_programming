#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing an instance of a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
