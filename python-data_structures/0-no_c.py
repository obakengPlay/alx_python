def no_c(my_string):

    new_string = ''.join(char for char in my_string if char not in {'c', 'C'})
    return new_string


print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun"))
