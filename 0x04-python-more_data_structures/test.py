#!/usr/bin/python3
complex_delete = __import__('102-complex_delete').complex_delete

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
print("Original dictionary:", my_dict)

value_to_delete = 2
complex_delete(my_dict, value_to_delete)
print("After deleting", value_to_delete, ":", my_dict)
