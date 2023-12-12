#!/usr/bin/python3
import sys

if __name__ == "__main__":

    # Get the number of arguments
    num_args = len(sys.argv) - 1  
    
    # Subtract 1 to exclude the script name itself

    # Print the number of arguments
    print("{} argument{}:".format(num_args, 's' if num_args != 1 else '') + ('.' if num_args == 0 else ''))

    # Print each argument and its position
    for i in range(1, num_args + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
