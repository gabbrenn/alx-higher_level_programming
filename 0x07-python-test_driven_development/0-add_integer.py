#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a,int):
        raise TypeError("a must be an integer")
    if not isinstance(b,int):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a=int(a)
    if isinstance(b,float):
        b=int(b)

    return int(a+b)
