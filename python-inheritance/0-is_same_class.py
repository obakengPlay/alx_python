def is_same_class(obj, a_class):
    return type(obj) is a_class

a=1 
print(is_same_class(a, int))