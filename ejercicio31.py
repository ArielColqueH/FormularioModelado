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

def sumatoria_log(arr):
    sum = 0
    for i in arr:
        sum += math.log(i,10)
    return sum
def sumatoria_log_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.log(i,10)**2)
    return sum

def alpha_2(arrx1,arrx2,arry1):
    n=len(arrx1)
    loge = math.log(math.e, 10);
    dloge=(n*loge**2)-(n*loge)**2
    dx2=((sumatoria_log(arrx2)**2)-sumatoria_log_sqrt(arrx2))
    dividendo=sumatoria_log(arry1)*sumatoria_log(arrx2)*(sumatoria_log(arrx1)**2)*(dloge**2)+(sumatoria_log(arry1)*sumatoria_log(arrx2)*(sumatoria_log(arrx1)**2)*(dloge))*(((n*loge)**2)-n*loge**2)
    divisor=sumatoria_log_sqrt(arrx1)*(n*loge**2)*((n*loge)**2)*dx2-((n*loge)**4)*(sumatoria_log(arrx1)**2)*(dx2)-((sumatoria_log(arrx1)*sumatoria_log(arrx2))**2)*(dloge)
    res=dividendo/divisor;
    return res
def alpha_1 (arrx1,arrx2,arry1):
    n=len(arrx1)
    loge=math.log(math.e,10);
    dividendo=sumatoria_log(arry1)*sumatoria_log(arrx1)*(n*(loge**2)-(n*loge)**2)+alpha_2(arrx1,arrx2,arry1)*sumatoria_log(arrx1)*sumatoria_log(arrx2)*(((n*loge)**2)-n*(loge**2));
    divisor=(sumatoria_log(arrx1)**2)*(n*(loge**2))-(n*loge*sumatoria_log(arrx1))**2
    res=dividendo/divisor;
    return res

def alpha_0 (arrx1,arrx2,arry1):
    n=len(arrx1)
    loge=math.log(math.e,10);
    dividendo=sumatoria_log(arry1)*sumatoria_log(arrx1)-alpha_1 (arrx1,arrx2,arry1)*(sumatoria_log(arrx1)**2)-alpha_2(arrx1,arrx2,arry1)*sumatoria_log(arrx2)*sumatoria_log(arrx1)
    divisor=sumatoria_log(arrx1)*n*loge
    res=dividendo/divisor;
    print(dividendo)
    print(divisor)
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
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------")
print("\t Ejericicio 1 : \t"+"| a2 = "+str(alpha_2(horasEstudioArray,horasEstudioArray,promedioNotaArray))+"\t | a1 = "+str(alpha_1(horasEstudioArray,amigosArray,promedioNotaArray)) +"\t | a0 = "+str(alpha_0(horasEstudioArray,amigosArray,promedioNotaArray)))
print("---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ")
csv_file.close()
