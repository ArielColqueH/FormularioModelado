import csv

def promedio(num):
    sum = 0
    for i in num:
        sum += i
    return sum / len(num)

def sumatoriasqrt(num):
    sum = 0
    for i in num:
        sum += (i ** 2)
    return sum

def sumatoria(num):
    sum = 0
    for i in num:
        sum += i
    return sum

def sumatoriadoble(arrx, arry):
    auxarray=[]
    for i in range(len(arrx)):
        auxarray.append(arrx[i]*arry[i])
    return sumatoria(auxarray)

def b1(arrx,arry):
    res = ((sumatoriadoble(arrx,arry)-promedio(arry)*sumatoria(arrx))/(sumatoriasqrt(arrx)-promedio(arrx)*sumatoria(arrx)))
    return res

def b0(arrx,arry):
    res = (promedio(arry)-b1(arrx,arry)*promedio(arrx))
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

print("---------- ---------- ---------- ---------- ---------- ----------")
print("\t Modelo 1 : \t"+"| B0 = "+str(round(b0(edadArray,promedioNotaArray),4))+"\t | B1 = "+str(round(b1(edadArray,promedioNotaArray),4))+"\t |")
print("\t Modelo 2 : \t"+"| B0 = "+str(round(b0(materiaArray,promedioNotaArray),4))+"\t | B1 = "+str(round(b1(materiaArray,promedioNotaArray),4))+"\t |")
print("\t Modelo 3 : \t"+"| B0 = "+str(round(b0(horasEstudioArray,promedioNotaArray),4))+"\t | B1 = "+str(round(b1(horasEstudioArray,promedioNotaArray),4))+"\t |")
print("\t Modelo 4 : \t"+"| B0 = "+str(round(b0(recreoArray,promedioNotaArray),4))+"\t | B1 = "+str(round(b1(recreoArray,promedioNotaArray),4))+"\t |")
print("\t Modelo 5 : \t"+"| B0 = "+str(round(b0(amigosArray,promedioNotaArray),4))+"\t | B1 = "+str(round(b1(amigosArray,promedioNotaArray),4))+"\t |")
print("---------- ---------- ---------- ---------- ---------- ----------")
csv_file.close()

