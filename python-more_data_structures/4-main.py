#!/usr/bin/python3
common_elements = __import__('1-common_elements').common_elements

set_1 = { "Python" }
set_2 = { "Python" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))