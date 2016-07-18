"""
Collection of utility methods serving a temporary purpose
Will try to remove the need for some tuple math in the future by changing
those that require math into some Vector data-structure with a supported
vector/vector-math library.
"""

import os


def tuple_add(a, b):
    return tuple(map(lambda x, y: x + y, a, b))


def tuple_sub(a, b):
    return tuple(map(lambda x, y: x - y, a, b))


def plural(n, s1):
    if n > 1 or n == 0:
        return s1 + 's'
    else:
        return s1


def split_every_nchars(instr, n):
    return [instr[i:i+n] for i in xrange(0, len(instr), n)]


def bits(char, nbits):
    b = ''
    for i in reversed(xrange(nbits)):
        b += str((char >> i) & 1)
    return b


def get_file_name(path):
    return os.path.basename(path).split('.')[0]


def get_item(blueprint_path):
    return blueprint_path.split('/')[-1].split('.')[-1]


def list_set(l, index, value):
    try:
        l[index] = value
    except IndexError:
        for _ in xrange(index - len(l)+1):
            l.append(None)
        l[index] = value