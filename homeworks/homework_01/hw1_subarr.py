#!/usr/bin/env python
# coding: utf-8


def find_subarr(input_lst, num):
    a = {}
    summa = 0
    for i, val in enumerate(input_lst):
        summa += val
        if summa - num in a:
            return(a[summa - num], i)
        elif val == num:
            return(i, i)
        else:
            a[summa - val] = i
    return ()
