"""
    this is a class, nothing changes 
    
"""

class Square:
    
    """
    Squaring the number, class 
    
    """
    def __innit__(self,size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size <0:
            raise ValueError("size must be >=0")
        else: 
            self.__size = self,size
            def area(self):
                return self.__size ** 2