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
        sum += (math.cos(math.radians(i)) ** 2)
    return sum


def sumatoria_seno_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.sin(math.radians(i)) ** 2)
    return sum


def sumatoria_naturales_cambio_variable(arr):
    sum = 0
    for i in arr:
        sum += 1 / i
    return sum


def sumatoria_log(arr):
    sum = 0
    for i in arr:
        sum += math.log(i, 10)
    return sum


def sumatoria_log_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.log(i, 10) ** 2)
    return sum

def imprimir_matriz(matriz):
    p = len(matriz)
    q = len(matriz[0])
    for i in range(p):
        for j in range(q):
            print(format(matriz[i][j], "<5"), end="")
        print()


def multiplicacion_dos_matrices_n_m(matrixN, matrixM):
    p = len(matrixN)
    n = len(matrixN[0])
    n2 = len(matrixM)
    q = len(matrixM[0])
    print("matriz 1:")
    imprimir_matriz(matrixN)
    print("matriz 2:")
    imprimir_matriz(matrixM)
    if(n!=n2):
        print('Las matrices no son PxN NxQ por lo tanto, no se pueden multiplicar')
    else:
        result = [[0 for i in range(q)] for j in range(p)]
        for i in range(p):
            for j in range(q):
                for k in range(n):
                    result[i][j] = result[i][j] + matrixN[i][k] * matrixM[k][j]

        print('resultado: ')
        imprimir_matriz(result)

# A = [[1, 4, 5],
#      [5, 3, 4],
#      [1, 8, 9]]
#
# B = [[1, 4],
#      [2, 3],
#      [1, 3]]
# multiplicacion_dos_matrices_n_m(A, B)
