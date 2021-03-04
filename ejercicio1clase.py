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
def sumatoria_xy(arr,arry):
    sum=0
    for i in arr:
        sum += i*arry[i]
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


def sumatoria_seno_coseno(arrx1, arrx2):
    sum = 0
    for i in range(len(arrx1)):
        sum += (math.sin(math.radians(arrx1[i])) * math.cos(math.radians(arrx2[i])))
    return sum


def sumatoria_y_seno(arrx, arry):
    sum = 0
    for i in range(len(arrx)):
        sum += math.sin(math.radians(arrx[i])) * arry[i]
    return sum


def sumatoria_y_coseno(arrx, arry):
    sum = 0
    for i in range(len(arrx)):
        sum += (math.cos(math.radians(arrx[i])) * arry[i])
    return sum


def sumatoria_coseno_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.cos(math.radians(i))) ** 2
    return sum


def sumatoria_seno_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.sin(math.radians(i))) ** 2
    return sum


def sumatoria_seno_coseno_sqrt(arrx1, arrx2):
    sum = 0
    for i in range(len(arrx1)):
        sum += ((math.sin(math.radians(arrx1[i])) ** 2) * (math.cos(math.radians(arrx2[i])) ** 2))
    return sum


def psi_1(arrx1,arry1):
 dividendo=(sumatoria_naturales(arrx1)*sumatoria_naturales(arry1))
 divisor=sumatoria_sqrt(arrx1)
 res=dividendo/divisor;
 return res

# -----regresion lineal-----

def y_estimado(arrx1, arry1):
    arrEstimado = []
    for i in range(len(arrx1)):
        element = psi_1(arrx1, arry1)
        arrEstimado.append(element)
    return arrEstimado


def sumatoria_y_menos_ypromedio(arry):
    sum = 0
    for i in arry:
        sum += (i - promedio(arry)) ** 2
    return sum


def sumatoria_y_menos_yestimado(arry, arryestimado):
    sum = 0
    for i in range(len(arry)):
        sum += ((arry[i] - arryestimado[i]) ** 2)
    return sum


def r2_primerafuncion(arrx1, arry):
    arry_estimado = y_estimado(arrx1, arry)
    dividendo = sumatoria_y_menos_ypromedio(arry_estimado)
    divisor = sumatoria_y_menos_ypromedio(arry)
    res = dividendo / divisor;
    return res


def r2_segundafuncion(arrx1, arrx2, arry):
    arry_estimado = y_estimado(arrx1, arrx2, arry)
    dividendo = sumatoria_y_menos_yestimado(arry, arry_estimado)
    divisor = sumatoria_y_menos_ypromedio(arry)
    res = 1 - (dividendo / divisor);
    return res

csv_file = open('simulacion1.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
promedioNotaArray = []
edadArray = []
materiaArray = []
horasEstudioArray = []
recreoArray = []
amigosArray = []

for row in csv_reader:
    promedio_nota, edad, materia, horas_estudio, recreo, amigos = row
    promedioNotaArray.append(float(promedio_nota))
    edadArray.append(float(edad))
    materiaArray.append(float(materia))
    horasEstudioArray.append(float(horas_estudio))
    recreoArray.append(float(recreo))
    amigosArray.append(float(amigos))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("\t Ejericicio 1 : \t" + "| a0 = " + str(
    psi_1(edadArray, promedioNotaArray)) + " | R^2 1 = " + str(
    r2_primerafuncion(edadArray, promedioNotaArray)))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
csv_file.close()