   #!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 0
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))