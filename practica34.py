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
print("\t Ejericicio 4 : \t"+"| a0 = "+str(alpha_0(horasEstudioArray,edadArray,promedioNotaArray))+"\t | a1 = "+str(alpha_1(horasEstudioArray,edadArray,promedioNotaArray)))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
csv_file.close()
