def no_c(my_string):

    new_string = ''.join(char for char in my_string if char not in {'c', 'C'})
    return new_string

word= "School"
new_word= no_c(word)

print(new_word)
print(word)

