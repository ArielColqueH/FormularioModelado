import csv
import math


def promedio(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)


def sumatoria_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (i ** 2)
    return sum


def sumatoria_naturales(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def sumatoria_y_promedio(arry):
    sum = 0
    for i in arry:
        sum += (i-sumatoria_naturales(arry))**2
    return sum


def r_2_1(arry1):
    n = len(arry1)
    dividendo=n*math.e**2
    divisor=sumatoria_y_promedio(arry1)
    res=dividendo/divisor;
    return res


def r_2_2 (arry1):
    n = len(arry1)
    dividendo = n * math.e ** 2
    divisor = sumatoria_y_promedio(arry1)
    res = dividendo / divisor;
    return 1-res

