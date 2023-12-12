
#import module 
from square import my_square

class Square:
    def __init__(self,size=0):
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else: self.__size - size 
        
    my_square_1 = my_square(3)
    
print(type(my_square))
print(my_square.__dir__)
