def no_c(my_string):
    result = ''. join( char for char in my_string if char not in'cC')
    return result 
  
