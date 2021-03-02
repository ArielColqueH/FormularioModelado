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
        sum += math.e**1/i
    return sum


def alpha_2(arrx1,arrx2,arry1):
    dividendo=sumatoria_naturales(arrx2)*sumatoria_naturales_cambio_variable(arry1)*((sumatoria_naturales(arrx1))**2)-sumatoria_naturales_cambio_variable(arry1)*sumatoria_naturales(arrx2)*sumatoria_sqrt(arrx1)
    divisor=(sumatoria_naturales(arrx1)*sumatoria_naturales(arrx2))**2-(sumatoria_sqrt(arrx2))*sumatoria_naturales(arrx1)
    res=dividendo/divisor;
    return res

def alpha_1(arrx1,arrx2,arry1):
    dividendo=sumatoria_naturales_cambio_variable(arry1)*sumatoria_naturales(arrx1)-alpha_2(arrx1,arrx2,arry1)*sumatoria_naturales(arrx1)*sumatoria_naturales(arrx2)
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


def r2_segundafuncion (arrx1,arrx2,arry):
    arry_estimado = y_estimado(arrx1, arrx2, arry)
    dividendo = sumatoria_y_menos_yestimado(arry,arry_estimado)
    divisor = sumatoria_y_menos_ypromedio(arry)
    res = 1-(dividendo / divisor);
    return res

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
print("\t Ejercicio de clase 3 : \t"+"| a2 = "+str(alpha_2(horasEstudioArray,edadArray,promedioNotaArray))+" | a1 = "+str(alpha_1(horasEstudioArray,edadArray,promedioNotaArray)) +" | R^2 1 = "+str(r2_primerafuncion(horasEstudioArray,edadArray,promedioNotaArray))  +" | R^2 2 = "+str(r2_segundafuncion(horasEstudioArray,edadArray,promedioNotaArray)))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
csv_file.close()