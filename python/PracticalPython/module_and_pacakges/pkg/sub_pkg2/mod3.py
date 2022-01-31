"""
Module 3's function and class
"""
def mod3_func():
    """Module 3 Function."""
    print("This is module 3 function.")
    from .. sub_pkg1 import mod1
    mod1.mod1_func()

class mod3_class:
    """Module 3's Class(Not implemented)"""
    pass