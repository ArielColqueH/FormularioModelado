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

def sumatoria_naturales_cambio_variable(arr):
    sum = 0
    for i in arr:
        sum += math.e**(1/i)
    return sum

def sumatoria_naturales_cambio_variable_arrx(arrx,arry):
    sum = 0
    for i in range(len(arrx)):
        sum += (math.e**(1/arry[i]))*(arrx[i])
    return sum

def sumatoria_naturales_arrx1_arrx2(arrx1,arrx2):
    sum = 0
    for i in range(len(arrx1)):
        sum += (arrx1[i]+arrx2[i])
    return sum

def alpha_2(arrx1,arrx2,arry1):
    dividendo=sumatoria_naturales_cambio_variable_arrx(arrx2,arry1)*(sumatoria_sqrt(arrx1)-((sumatoria_naturales(arrx1))**2))
    divisor=(sumatoria_naturales_arrx1_arrx2(arrx1,arrx2))**2-((sumatoria_sqrt(arrx2))*(sumatoria_sqrt(arrx1)))
    res=dividendo/divisor
    return res

def alpha_1(arrx1,arrx2,arry1):
    dividendo=sumatoria_naturales_cambio_variable_arrx(arrx1,arry1)-alpha_2(arrx1,arrx2,arry1)*(sumatoria_naturales_arrx1_arrx2(arrx1,arrx2))
    divisor=sumatoria_sqrt(arrx1)
    res=dividendo/divisor;
    return res

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
            print(format(matriz[i][j], "<25"), end="")
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


def multiplicacion_matrices_vector_n_m(matrixN, vect):
    fila = len(matrixN)
    columna = 1
    n = len(vect)
    result = [[0 for i in range(columna)] for j in range(fila)]
    for i in range(fila):
        for j in range(columna):
            for k in range(n):
                result[i][j] = result[i][j] + matrixN[i][k] * vect[k]
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
    matriz2 = multiplicacion_dos_matrices_n_m(inversa_matriz(matriz1), traspuesta_matriz(matriz))
    resmatriz = multiplicacion_matrices_vector_n_m(matriz2, matrizy)
    return resmatriz

def crearMatriz(arrx1, arrx2):
    w, h = 2, len(arrx1);
    result = [[0 for x in range(w)] for y in range(h)]
    for i in range(len(arrx1)):
        result[i][0] = arrx1[i]
        result[i][1] = arrx2[i]
    return result

csv_file = open('simulacion1.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
promedioNotaArray = []
edadArray = []
materiaArray = []
horasEstudioArray = []
recreoArray=[]
amigosArray=[]

for row in csv_reader:
    promedio_nota, edad, materia, horas_estudio, recreo, amigos = row
    promedioNotaArray.append(float(promedio_nota))
    edadArray.append(float(edad))
    materiaArray.append(float(materia))
    horasEstudioArray.append(float(horas_estudio))
    recreoArray.append(float(recreo))
    amigosArray.append(float(amigos))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("\t Ejercicio de clase 3 : \t"+"| a2 = "+str(alpha_2(horasEstudioArray,edadArray,promedioNotaArray))+" | a1 = "+str(alpha_1(horasEstudioArray,edadArray,promedioNotaArray)) +" | R^2 1 = "+str(r2_primerafuncion(horasEstudioArray,edadArray,promedioNotaArray)))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("Matriz B:")
aux = crearMatriz(horasEstudioArray, edadArray)
imprimir_matriz(b_arreglos(aux, promedioNotaArray))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
csv_file.close()