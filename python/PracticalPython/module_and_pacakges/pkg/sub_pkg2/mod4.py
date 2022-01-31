"""
Module 4's function and class
"""
def mod4_func():
    """Module 4 Function."""
    print("This is module 4 function.")
    from . import mod3
    mod3.mod3_func()

class mod4_class:
    """Module 4's Class(Not implemented)"""
    pass