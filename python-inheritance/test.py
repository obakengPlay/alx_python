
class SameClass:
    @staticmethod
    def is_same_class(obj, a_class):
        return type(obj) is a_class
    
is_same_class = SameClass()

a=1 
print(is_same_class.is_same_class(a, int))

''' main_1.py '''

is_same_class = __import__('0-is_same_class').is_same_class

a = True
print(is_same_class(a, int))

'''main_2.py'''

is_same_class = __import__('0-is_same_class').is_same_class

a = 3.14
print(is_same_class(a, int))

'''main_3.py'''

is_same_class = __import__('0-is_same_class').is_same_class

a = True
print(is_same_class(a, object))

'''main_4.py'''

is_same_class = __import__('0-is_same_class').is_same_class

a = None
print(is_same_class(a, object))

'''main_5.py'''

is_same_class = __import__('0-is_same_class').is_same_class

a = None
print(is_same_class(a, list))

'''main_6.py'''

is_same_class = __import__('0-is_same_class').is_same_class

a = [1, 2, 3]
print(is_same_class(a, list))

'''main_7.py'''

is_same_class = __import__('0-is_same_class').is_same_class

a = [1, 2, 3]
print(is_same_class(a, object))
