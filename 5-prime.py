def is_prime(number): 
    if number <= 1: 
        return False 
    elif number <= 3: 
        return True 
    elif number % 2 == 0 or number % 3 == 0: 
        return False 
    i = 5 
    while i * i <= number: 
        if number % i == 0 or number % (i + 2) == 0: 
            return False 
        i += 6 
        return True
    
print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))