def no_c(my_string):
    results = ""
    for char in my_string:
        if char not in 'cC':
            results += char
    return results 
  
