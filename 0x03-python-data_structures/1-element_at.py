#!/usr/bin/python3
def element_at(my_list, idx):
    """
    A function that returns an
    element from a list like in C

    Args:
        my_list: A list looped through
        idx: the index to be returned
    """
    length = len(my_list) - 1
    if idx > length:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
