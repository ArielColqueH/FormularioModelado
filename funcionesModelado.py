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

def sumatoria_arr1_arr2(arrx1, arrx2):
    sum = 0
    for i in range(len(arrx1)):
        sum += (arrx1[i]*arrx2[i])
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

def sumatoria_log_e(arr):
    n = len(arr)*math.log(math.e)
    return n

def sumatoria_log_e_n(arr,expo):
    n = len(arr)*math.log((math.e)**expo)
    return n

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

#-----regresion lineal-----

def y_estimado(arrx1,arrx2,arry1):
    arrEstimado=[]
    for i in range(len(arrx1)):
        element = (1 / (math.log(alpha_1(arrx1,arrx2,arry1)*arrx1[i]+arrx2[i]*alpha_2(arrx1,arrx2,arry1))))
        arrEstimado.append(element)
    return arrEstimado


def sumatoria_y_menos_ypromedio(arry):
    sum = 0
    for i in arry:
        sum += (i-promedio(arry))**2
    return sum

def sumatoria_y_menos_yestimado(arry,arryestimado):
    sum = 0
    for i in range(len(arry)):
        sum += ((arry[i]-arryestimado[i])**2)
    return sum


def r2_primerafuncion(arrx1,arrx2,arry):
    arry_estimado=y_estimado(arrx1,arrx2,arry)
    dividendo=sumatoria_y_menos_ypromedio(arry_estimado)
    divisor=sumatoria_y_menos_ypromedio(arry)
    res=dividendo/divisor;
    return res




# -----matrices----

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




A = [[1, 4],
     [5, 3]]
#
# B = [[1, 4],
#      [2, 3],
#      [1, 3]]
# multiplicacion_dos_matrices_n_m(A, B)

def traspuesta_matriz(matriz):
    t= []
    for i in range(len(matriz[0])):
        t.append([])
        for j in range(len(matriz)):
            t[i].append(matriz[j][i])

    return t

#-----imprimir-----

def subM(M,N):
    n = len(M)
    R = []
    for i in range(n):
        R.append([0]*n)
    for i in range(n):
        for j in range(n):
            R[i][j]=M[i][j]-N[i][j]
    return R

def KI(k,n):
    R = []
    for i in range(n):
        R.append([0]*n)
    for i in range(n):
        R[i][i]=k
    return R

def trazM(M):
    n = len(M)
    t=0
    for i in range(n):
        t+=M[i][i]
    return t

def kM(k,M):
    n = len(M)
    R = []
    for i in range(n):
        R.append([0]*n)
    for i in range(n):
        for j in range(n):
            R[i][j]=k*M[i][j]
    return R

def inversa(M):
    n = len(M)
    Bi = A
    for i in range(1, n - 1):
        bi = trazM(Bi) / i
        Bi = multiplicacion_dos_matrices_n_m(A, subM(Bi, KI(bi,n)))
    bip = trazM(Bi) / (n - 1)
    Biu = multiplicacion_dos_matrices_n_m(A, subM(Bi, KI(bip,n)))
    biu = trazM(Biu) / (n)
    print("La inversa de la matris es :")
    invM = kM(1 / biu, subM(Bi, KI(bip,n)))
    return invM