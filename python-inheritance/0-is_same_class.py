'''same class code'''

class SameClass:
    @staticmethod
    def is_same_class(obj, a_class):
        return type(obj) is a_class
 
 #creating an instance of sameclass    
same_obj = SameClass()

a=1 
#using method through the object instance 
print(same_obj.is_same_class(a, int))