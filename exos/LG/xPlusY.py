#!/usr/bin/python3
# -*- coding: utf-8 -*-

def parseInt(s):
    try:
        return int(s)
    except TypeError:
        print("%s => NaN" % s)
        exit(-1)


if __name__ == "__main__":
    x = input("x: ")
    X = parseInt(x)

    y = input("y: ")
    Y = parseInt(y)

    print(X+Y)