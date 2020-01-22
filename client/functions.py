from random import randrange as rd


def random_string(ln):
    ret = ''
    for i in range(ln):
        ret += chr(rd(33, 125))
    return ret
