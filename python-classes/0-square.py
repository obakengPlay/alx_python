#!/usr/bin/python3

class Square: 
    def __init__(self, __size): 
        self.__size = __size 
    
my_square = Square(3) 
# Displaying the type of my_square object 
print(type(my_square)) 
# Displaying only the __size attribute value 
print(my_square.__dict__)
#Char_length = len('text')
#print("Character length:",Char_length)
