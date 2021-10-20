#!/usr/bin/python3
import os

def get_path(filename):
    """Retun file's path or empty stirng if no path."""
    import pdb; pdb.set_trace()
    head, tail = os.path.split(filename)
    for char in tail: 
        pass # Check filename char.
    return head

filename = __file__
filename_path = get_path(filename)
print(f'path = {filename_path}')