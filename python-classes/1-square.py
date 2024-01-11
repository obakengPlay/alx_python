
# import module 
my_square_1 = __import__('0-square').Square 
class Square: 
           def __init__(self, size=0): 
               if not isinstance(size, int): 
                   raise TypeError("size must be an integer") 
               elif size < 0: 
                   raise ValueError("size must be >= 0") 
               else: self.__size = size 
# Creating an instance of Square outside the class 
my_square_1 = Square(3)

# Checking the type and attributes of my_square_1 
print(type(my_square_1)) 
print(my_square_1.__dict__)
