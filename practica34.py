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

def alpha_1(arrx1,arrx2,arry1):
    dividendo=sumatoria_naturales(arry1)*sumatoria_coseno(arrx2)*(sumatoria_seno_sqrt(arrx1)-(sumatoria_seno(arrx1)**2))
    divisor=sumatoria_coseno_sqrt(arrx2)*sumatoria_seno_sqrt(arrx1)-(sumatoria_seno(arrx1)*sumatoria_coseno(arrx2))**2;
    res=dividendo/divisor;
    return res

def alpha_0(arrx1,arrx2,arry1):
    dividendo=sumatoria_naturales(arry1)*sumatoria_seno(arrx1)-(alpha_1(arrx1,arrx2,arry1)*(sumatoria_coseno(arrx2)*sumatoria_seno(arrx1)))
    divisor=sumatoria_seno_sqrt(arrx1);
    res=dividendo/divisor;
    return res

#-----regresion lineal-----

def y_estimado(arrx1,arrx2,arry1):
    arrEstimado=[]
    for i in range(len(arrx1)):
        element =  alpha_0(arrx1,arrx2,arry1)*math.sin(math.radians(arrx1[i]))+ alpha_1(arrx1,arrx2,arry1)*math.cos(math.radians(arrx2[i]))
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
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("\t Ejericicio 4 : \t"+"| a0 = "+str(alpha_0(horasEstudioArray,edadArray,promedioNotaArray))+"\t | a1 = "+str(alpha_1(horasEstudioArray,edadArray,promedioNotaArray)) +" | R^2 1 = "+str(r2_primerafuncion(horasEstudioArray,edadArray,promedioNotaArray))  +" | R^2 2 = "+str(r2_segundafuncion(horasEstudioArray,edadArray,promedioNotaArray))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
csv_file.close()
