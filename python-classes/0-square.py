#!/usr/bin/python3
class Square:
    def __init__(self, _Square__size):
        self.Square__size = _Square__size
        
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
