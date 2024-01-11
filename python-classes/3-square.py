class Square:
    def __innit__(selfmsize=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size <0:
            raise ValueError("size must be >=0")
        else: 
            self.__size = selfmsize
            def area(self):
                return self.__size ** 2