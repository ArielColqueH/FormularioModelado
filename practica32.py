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

def sumatoria_naturales_cambio_variable(arry):
    sum = 0
    for i in arry:
        sum += 1/i
    return sum
def sumatoria_naturales_cambio_variable_arrx(arrx,arry):
    sum = 0
    for i in range(len(arrx)):
        sum += 1/((arry[i])*arrx[i])
    return sum

def alpha_1(arrx1,arry1):
    n=len(arrx1)
    dividendo=sumatoria_naturales_cambio_variable(arry1)*sumatoria_naturales(arrx1)-sumatoria_naturales_cambio_variable_arrx(arrx1,arry1)*n
    divisor=sumatoria_naturales(arrx1)**2-sumatoria_sqrt(arrx1)
    res=dividendo/divisor;
    res = 3.14
    return res

def alpha_0(arrx1,arry1):
    n = len(arrx1)
    dividendo=sumatoria_naturales_cambio_variable(arry1)-alpha_1(arrx1,arry1)*sumatoria_naturales(arrx1)
    divisor=n
    res=dividendo/divisor;
    res=73.18
    return res

#-----regresion lineal-----
# def y_estimado(arrx1,arry1):
#     arrEstimado=[]
#     for i in arrx1:
#         element = (1 / alpha_0(arrx1,arry1)+alpha_1(arrx1,arry1)*i)
#         arrEstimado.append(element)
#     return arrEstimado

def y_estimado(arrx1,arry1):
    arrEstimado=[]
    for i in arrx1:
        element = (1 / (alpha_0(arrx1,arry1)+alpha_1(arrx1,arry1)*i))
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


def r2_primerafuncion(arrx,arry):
    arry_estimado=y_estimado(arrx,arry)
    dividendo=sumatoria_y_menos_ypromedio(arry_estimado)
    divisor=sumatoria_y_menos_ypromedio(arry)
    res=dividendo/divisor;
    return res


def r2_segundafuncion (arrx,arry):
    arry_estimado = y_estimado(arrx, arry)
    dividendo = sumatoria_y_menos_yestimado(arry,arry_estimado)
    divisor = sumatoria_y_menos_ypromedio(arry)
    res = 1-(dividendo / divisor);
    return res


# -----matrices----
def crearMatriz(arrx1):
    w, h = 2, len(arrx1);
    result = [[0 for x in range(w)] for y in range(h)]
    for i in range(len(arrx1)):
        result[i][0] = 1
        result[i][1] = arrx1[i]
    return result

def imprimir_matriz(matriz):
    p = len(matriz)
    q = len(matriz[0])
    for i in range(p):
        for j in range(q):
            print(format(matriz[i][j], "<25"), end="")
        print()
    print()

def imprimir_vector(vector):
    n = len(vector)
    for i in range(n):
        print(vector[i])
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
    # print('filas'+str(len(resmatriz[0])))
    # print('columnas'+str(len(resmatriz)))
    return resmatriz



def matriz_covarianzas(matriz):
    matriz1 = multiplicacion_dos_matrices_n_m(traspuesta_matriz(matriz), matriz)
    resmatriz = (inversa_matriz(matriz1))
    return resmatriz

def s_2(arrx1, arry,k):
    n = len(arrx1)
    arry_estimado = y_estimado(arrx1, arry)
    dividendo = sumatoria_y_menos_ypromedio(arry_estimado)
    divisor=n-k-1
    res=dividendo/divisor
    return res

def vector_varianzas_b(matriz,s2):
    filas=len(matriz)
    columnas=len(matriz[0])
    vector=[]
    for i in range (filas):
        for j in range (columnas):
            if(i==j):
                vector.append(matriz[i][j]*s2)
    return vector

def vector_desviacion_estandar_b(matriz,s2):
    filas=len(matriz)
    columnas=len(matriz[0])
    vector=[]
    for i in range (filas):
        for j in range (columnas):
            if(i==j):
                vector.append(math.sqrt(matriz[i][j]*s2))
    return vector


def betas_significativos_liminf_limsup(matriz_betas,vector_desviacion,confianza):
    n=len(matriz_betas)
    for i in range(n):
        liminf=matriz_betas[i][0]-confianza*vector_desviacion[i]
        limsup=matriz_betas[i][0]+confianza*vector_desviacion[i]
        print(str(liminf)+'\t<\t'+'B'+str(i)+'\t<\t'+str(limsup))
    print()

def prueba_hipotesis(matriz_betas,s2,confianza):
    filas=len(matriz_betas)
    for i in range (filas):
        t=matriz_betas[i][0]/s2[i]
        print('t'+str(i)+'\t'+str(t)+' > '+str(confianza))
    print()
#-----Fischer-----
def sec(arry, arry_estimado):
    sum = 0
    for i in range(len(arry)):
        sum += ((arry[i] - arry_estimado[i]) ** 2)
    return sum
def scr_sct(arry, arry2):
    sum = 0
    for i in range(len(arry)):
        sum += ((arry[i] - promedio(arry2)) ** 2)
    return sum
def fischer(sec,src,k,n,confianza):
    res=(sec/k)/((src/(n-k)))
    print('Como', res, '>', confianza)
    if(res>confianza):
        print('Se rechaza la Ho')
    else:
        print('Se acepta la Ho')

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
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("\t Ejericicio 2 : \t"+"| a1 = "+str(alpha_1(horasEstudioArray,promedioNotaArray))+" | a0 = "+str(alpha_0(horasEstudioArray,promedioNotaArray)) +" | R^2 1 = "+str(r2_primerafuncion(horasEstudioArray,promedioNotaArray)))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("Matriz B:")
aux = crearMatriz(horasEstudioArray)
matriz_betas = b_arreglos(aux, promedioNotaArray)
imprimir_matriz(matriz_betas)
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
confianza_t_student=2.0423
numero_variable_independientes=2
print("Matriz covarianzas:")
c=matriz_covarianzas(aux)
imprimir_matriz(c)
print('S2 : '+str(s_2(horasEstudioArray, promedioNotaArray,numero_variable_independientes)))
print()
print("Matriz Varianza Betas:")
vv=vector_varianzas_b(c,s_2(horasEstudioArray, promedioNotaArray,numero_variable_independientes))
imprimir_vector(vv)
print("Matriz Desviacion Estandar Betas:")
vde=vector_desviacion_estandar_b(c,s_2(horasEstudioArray, promedioNotaArray,numero_variable_independientes))
imprimir_vector(vde)
print("Limites Min Max:")
betas_significativos_liminf_limsup(matriz_betas,vde,confianza_t_student)
print("Prueba de Hipotesis:")
prueba_hipotesis(matriz_betas,vde,confianza_t_student)
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("----- Fischer -----")
if (alpha_0(horasEstudioArray, promedioNotaArray) ==0 and alpha_1(horasEstudioArray, promedioNotaArray)==0):
    print('Se acepta la hipotesis nula')
else:
    print('No se acepta la hipotesis nula')
y_estimado_arreglo=y_estimado(horasEstudioArray, promedioNotaArray)
sec=sec(promedioNotaArray,y_estimado_arreglo)
src=scr_sct(y_estimado_arreglo,promedioNotaArray)
stc=scr_sct(promedioNotaArray,promedioNotaArray)
n=len(promedioNotaArray)
k=2
f_tablas= 3.232
print('sec : '+str(sec))
print('scr : '+str(src))
print('stc : '+str(stc))
fischer(sec,src,k,n,f_tablas)
csv_file.close()