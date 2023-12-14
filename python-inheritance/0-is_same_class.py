class SameClass:
    @staticmethod
    def is_same_class(obj, a_class):
        return type(obj) is a_class
    
is_same_class = SameClass()

a=1 
print(is_same_class.is_same_class(a, int))