import csv
import matplotlib.pyplot as plt
import numpy as np


# -----matrices----

def imprimir_matriz(matriz):
    p = len(matriz)
    q = len(matriz[0])
    for i in range(p):
        for j in range(q):
            print(format(matriz[i][j], "<5"), end="")
        print()
    print()


def multiplicacion_dos_matrices_n_m(matrixN, matrixM):
    p = len(matrixN)
    n = len(matrixN[0])
    n2 = len(matrixM)
    q = len(matrixM[0])
    if (n != n2):
        print('Las matrices no son PxN NxQ por lo tanto, no se pueden multiplicar')
    else:
        result = [[0 for i in range(q)] for j in range(p)]
        for i in range(p):
            for j in range(q):
                for k in range(n):
                    result[i][j] = result[i][j] + matrixN[i][k] * matrixM[k][j]

        return result


def traspuesta_matriz(matriz):
    t = []
    for i in range(len(matriz[0])):
        t.append([])
        for j in range(len(matriz)):
            t[i].append(matriz[j][i])

    return t


def subM(M, N):
    n = len(M)
    R = []
    for i in range(n):
        R.append([0] * n)
    for i in range(n):
        for j in range(n):
            R[i][j] = M[i][j] - N[i][j]
    return R


def KI(k, n):
    R = []
    for i in range(n):
        R.append([0] * n)
    for i in range(n):
        R[i][i] = k
    return R


def trazM(M):
    n = len(M)
    t = 0
    for i in range(n):
        t += M[i][i]
    return t


def kM(k, M):
    n = len(M)
    R = []
    for i in range(n):
        R.append([0] * n)
    for i in range(n):
        for j in range(n):
            R[i][j] = k * M[i][j]
    return R


def inversa_matriz(M):
    n = len(M)
    Bi = M
    for i in range(1, n - 1):
        bi = trazM(Bi) / i
        Bi = multiplicacion_dos_matrices_n_m(M, subM(Bi, KI(bi, n)))
    bip = trazM(Bi) / (n - 1)
    Biu = multiplicacion_dos_matrices_n_m(M, subM(Bi, KI(bip, n)))
    biu = trazM(Biu) / (n)
    invM = kM(1 / biu, subM(Bi, KI(bip, n)))
    return invM


def b_arreglos(matriz, matrizy):
    matriz1 = multiplicacion_dos_matrices_n_m(traspuesta_matriz(matriz), matriz)
    matriz2 = multiplicacion_dos_matrices_n_m(matriz1, traspuesta_matriz(matriz))
    resmatriz = multiplicacion_dos_matrices_n_m(matriz2, matrizy)
    return resmatriz


def crear_matrix_y(matriz_original_y, q):
    fil = len(matriz_original_y)
    # print(fi)
    aux = np.array(matriz_original_y)
    nueva_matriz_y = aux[q:fil, :]
    return nueva_matriz_y


def crear_matrix_x(matriz_original_y, q):
    filOriginal = len(matriz_original_y)
    fil = len(crear_matrix_y(matriz_original_y, q))
    aux = np.array(matriz_original_y)
    nueva_matriz_y = [[0 for x in range(q)] for y in range(fil)]
    for i in range(q):
        index = i + 1
        aux_matriz_1 = aux[0:filOriginal - index, :]
        aux_matriz_2 = aux_matriz_1[(q - index):filOriginal - index, :]
        for j in range(fil):
            nueva_matriz_y[j][i] = aux_matriz_2[j][0]
    return nueva_matriz_y


def mult_y_x(matrizx, matrizy, q):
    vecaux = [[0 for x in range(1)] for y in range(len(matrizx))]
    vecq = [0] * q
    for j in range(q):
        for i in range(len(matrizx)):
            vecaux[i][0] = matrizx[i][j]
        res = b_arreglos(vecaux, matrizy)
        vecq[j] = res
    # print(vecq)
    return vecq


def crear_matriz(array):
    fil = len(array)
    nueva_matriz = [[0 for x in range(1)] for y in range(fil)]
    for i in range(fil):
        nueva_matriz[i][0] = array[i]
    return nueva_matriz

def modelo(array,a,b):
    aux = array*a+b
    return aux
q = 500
# Y = [[10],[-5],[8],[-1],[9],[6],[-5],[11],[18],[7],[10],[-5],[8],[-1],[9],[6],[-5],[11],[18],[7]]
csv_file = open('todo1.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
aux = []
for row in csv_reader:
    num, = row
    aux.append((float(row[0])))
Y = crear_matriz(aux)

t = crear_matrix_y(Y, 1)
size = len(t)
x = np.arange(size)
casoA=modelo(t,0.1,0)
casoB=modelo(t,-0.1,0)
casoC=modelo(t,1,100)
casoD=modelo(t,1,0)
casoE=modelo(t,0,0)
casoF=modelo(t,-1,0)
casoG=modelo(t,1.5,0)
casoH=modelo(t,-1.5,0)
plt.plot(x,t,x,casoH)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Caso')
plt.show()