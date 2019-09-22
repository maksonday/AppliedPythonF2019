#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    tmp = 1
    if (number < 0):
    	tmp = -1
    a = str(abs(number))
    a = a[::-1]
    number = int(a) * tmp
    return number
