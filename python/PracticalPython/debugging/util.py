import os

def get_path(filename):
    """Retun file's path or empty stirng if no path."""
    import pdb; pdb.set_trace()
    head, tail = os.path.split(filename)
    return head