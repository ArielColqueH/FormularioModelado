import csv
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
        sum += 1/i
    return sum


def alpha_1(arrx1,arry1):
    n=len(arrx1)
    dividendo=sumatoria_naturales_cambio_variable(arry1)*sumatoria_naturales(arrx1)-sumatoria_naturales_cambio_variable(arry1)*sumatoria_naturales(arrx1)*n
    divisor=sumatoria_naturales(arrx1)**2-sumatoria_sqrt(arrx1)
    res=dividendo/divisor;
    return res

def alpha_0(arrx1,arry1):
    n = len(arrx1)
    dividendo=sumatoria_naturales_cambio_variable(arry1)-alpha_1(arrx1,arry1)*sumatoria_naturales(arrx1)
    divisor=n
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
print("\t Ejericicio 2 : \t"+"| a1 = "+str(alpha_1(horasEstudioArray,promedioNotaArray))+" | a0 = "+str(alpha_0(horasEstudioArray,promedioNotaArray)))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
csv_file.close()