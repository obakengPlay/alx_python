def raise_exception():
    raise TypeError("An intentional TypeError")


try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
