def no_c(my_string):

    new_string = ''.join(char for char in my_string if char not in {'c', 'C'})
    return new_string

print("School")
print("Chicago")
print("Holberton")
print(no_c("Holberton School"))
print(no_c(""))
print("hellcCcccooccoscccss")