#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    EPS = 1e-15
    n = len(list_of_lists)
    for i in range(n):
        if len(list_of_lists[i]) != n:
            return None
    det = 1
    for i in range(n):
        maxel = i
        for j in range(i + 1, n):
            if abs(list_of_lists[j][i]) > abs(list_of_lists[maxel][i]):
                maxel = j
        if abs(list_of_lists[maxel][i]) < EPS:
            return 0
        list_of_lists[i], list_of_lists[maxel] = list_of_lists[maxel], list_of_lists[i]
        if i != maxel:
            det *= -1
        det *= list_of_lists[i][i]
        for j in range(i + 1, n):
            list_of_lists[i][j] /= list_of_lists[i][i]
        for j in range(n):
            if j != i and abs(list_of_lists[j][i]) > EPS:
                for k in range(i + 1, n):
                    list_of_lists[j][k] -= list_of_lists[i][k] * list_of_lists[j][i]
    return det
