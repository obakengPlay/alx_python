def fibonacci_sequence(n):
    fib_sequence = [] 
    if n <= 0: 
        return fib_sequence 
    elif n == 1: return [0] 
    else: fib_sequence = [0, 1] 
    while len(fib_sequence) < n: fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) 
    return fib_sequence

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))