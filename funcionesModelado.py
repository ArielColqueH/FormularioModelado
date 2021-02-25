import csv
import math

def promedio(num):
    sum = 0
    for i in num:
        sum += i
    return sum / len(num)

def sumatoria_naturales(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def sumatoria_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (i ** 2)
    return sum

def sumatoria_coseno(arr):
    sum = 0
    for i in arr:
        sum += math.cos(math.radians(i))
    return sum

def sumatoria_seno(arr):
    sum = 0
    for i in arr:
        sum += math.sin(math.radians(i))
    return sum

def sumatoria_coseno_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.cos(math.radians(i))**2)
    return sum

def sumatoria_seno_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.sin(math.radians(i))**2)
    return sum

def sumatoria_naturales_cambio_variable(arr):
    sum = 0
    for i in arr:
        sum += 1/i
    return sum
def sumatoria_log(arr):
    sum = 0
    for i in arr:
        sum += math.log(i,10)
    return sum
def sumatoria_log_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.log(i,10)**2)
    return sum
