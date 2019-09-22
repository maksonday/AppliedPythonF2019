#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    tmp = 1
    if (number < 0):
        tmp = -1
    a = str(abs(number))
    a = a[::-1]
    number = int(a) * tmp
    return number
