import csv
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.datasets.sunspots import load

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
    #print(resmatriz)
    # print('filas'+str(len(resmatriz[0])))
    # print('columnas'+str(len(resmatriz)))
    return resmatriz



def crear_matrix_y(matriz_original_y,q):
    fil=len(matriz_original_y)
    # print(fi)
    aux=np.array(matriz_original_y)
    nueva_matriz_y=aux[q:fil,:]
    return nueva_matriz_y

def crear_matrix_x(matriz_original_y,q):
    filOriginal=len(matriz_original_y)
    fil=len(crear_matrix_y(matriz_original_y,q))
    aux=np.array(matriz_original_y)
    nueva_matriz_y=[[0 for x in range(q)] for y in range(fil)]
    for i in range(q):
        index=i+1
        aux_matriz_1=aux[0:filOriginal-index,:]
        aux_matriz_2=aux_matriz_1[(q-index):filOriginal-index,:]
        # print('matrix : column ',index)
        # print(aux_matriz_2)
        for j in range (fil):
            nueva_matriz_y[j][i] = aux_matriz_2[j][0]
    return nueva_matriz_y

def mult_y_x(matrizx,matrizy,q):
    vecaux=[[0 for x in range(1)] for y in range(len(matrizx))]
    vecq=[0]*q
    for j in range(q):
        for i in range(len(matrizx)):
            vecaux[i][0] = matrizx[i][j]
        res=b_arreglos(vecaux,matrizy)
        vecq[j]=res
    #print(vecq)
    return vecq

def crear_matriz(array):
    fil = len(array)
    nueva_matriz = [[0 for x in range(1)] for y in range(fil)]
    for i in range(fil):
        nueva_matriz[i][0] = array[i]
    return  nueva_matriz

q=1824
csv_file = open('DatosPC.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
x11 = []
x22 = []
x33 = []
x44 = []
x55 = []
y11 = []
y22 = []
y33 = []
for row in csv_reader:
     x1,x2,x3,x4,x5,y1,y2,y3 = row
     x11.append(float(x1))
     x22.append(float(x2))
     x33.append(float(x3))
     x44.append(float(x4))
     x55.append(float(x5))
     y11.append(float(y1))
     y22.append(float(y2))
     y33.append(float(y3))
xx11=crear_matriz(x11)#se crear la matriz con los datos originales
xx22=crear_matriz(x22)
xx33=crear_matriz(x22)
xx44=crear_matriz(x22)
xx55=crear_matriz(x22)
arregloOriginalx1 = np.squeeze(np.asarray(xx11))
arregloOriginalx2 = np.squeeze(np.asarray(xx22))
arregloOriginalx3 = np.squeeze(np.asarray(xx33))
arregloOriginalx4 = np.squeeze(np.asarray(xx44))
arregloOriginalx5 = np.squeeze(np.asarray(xx55))

rho1, sigma = sm.regression.yule_walker(arregloOriginalx1, order=1,method="adjusted") #se aplica la formula de yule-walker donde se nos devuelven Rho y el arreglo de sigmas
print('rho1',rho1)

rho2, sigma = sm.regression.yule_walker(arregloOriginalx2, order=1,method="adjusted") #se aplica la formula de yule-walker donde se nos devuelven Rho y el arreglo de sigmas
print('rho2',rho2)

def creary1(array1,array2,array3):
    w, h = 3, 20;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    for i in range(20):
            Matrix[i][0]=array1[i]
            Matrix[i][1]=array2[i]
            Matrix[i][2]=array3[i]
    return Matrix
matrixY=creary1(arregloOriginalx3,arregloOriginalx4,arregloOriginalx5)

