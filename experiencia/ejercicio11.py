import csv
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
def array_media(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)


def array_mediana(arr):
    arr.sort()
    size = len(arr)
    if (size % 2 == 0):
        position = (size / 2);
        res = (arr[position] + arr[position + 1]) / 2
        return res
    else:
        return arr[int((size / 2)) + 1]

def array_desviacion(arr):
    dividendo=0
    for i in range(len(arr)):
        dividendo+=math.pow(arr[i]-array_media(arr),2)
    divisor= len(arr)-1
    res = math.sqrt(dividendo/divisor)
    return round(res,4)

def array_sesgo(arr):
    dividendo = 0
    for i in range(len(arr)):
        dividendo += math.pow(arr[i] - array_media(arr), 3)
    divisor = len(arr) * math.pow(array_desviacion(arr),3)
    res = dividendo / divisor
    return round(res, 4)

def array_kurtosis(arr):
    dividendo = 0
    for i in range(len(arr)):
        dividendo += math.pow(arr[i] - array_media(arr), 4)
    divisor = len(arr) * math.pow(array_desviacion(arr),4)
    res = (dividendo / divisor)-3
    return round(res, 4)

def array_jaque_bera(arr):
    n=len(arr)
    n1=(math.pow(array_desviacion(arr),2)/6)
    n2=(math.pow(array_kurtosis(arr),2)/24)
    res = (n1+n2)*n
    return round(res, 4)

def promedio(num):
    sum = 0
    for i in num:
        sum += i
    return sum / len(num)
def lnpromedio(num):
    sum = 0
    for i in num:
        sum += math.log(i)
    return sum / len(num)

def sumatoria_arr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
def sumatoria_lnarr(arr):
    sum = 0
    for i in arr:
        sum += math.log(i)
    return sum

def sumatoria_arr_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (i ** 2)
    return sum

def sumatoria_lnarr_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (math.log(i) ** 2)
    return sum

def sumatoria_arrx_arry(arrx1, arrx2):
    sum = 0
    for i in range(len(arrx1)):
        sum += (arrx1[i]*arrx2[i])
    return sum
def sumatoria_lnarrx_arry(arrx1, arrx2):
    sum = 0
    for i in range(len(arrx1)):
        sum += (math.log(arrx1[i])*arrx2[i])
    return sum

def pendiente(arrx,arry):
    n=len(arrx)
    dividendo = n*sumatoria_arrx_arry(arrx,arry)-sumatoria_arr(arrx)*sumatoria_arr(arry)
    divisor = n*sumatoria_arr_sqrt(arrx)-(sumatoria_arr(arrx)**2)
    return dividendo/divisor

def lnpendiente(arrx,arry):
    n=len(arrx)
    dividendo = n*sumatoria_lnarrx_arry(arrx,arry)-sumatoria_lnarr(arrx)*sumatoria_arr(arry)
    divisor = n*sumatoria_lnarr_sqrt(arrx)-(sumatoria_lnarr(arrx)**2)
    return dividendo/divisor

def b(arrx,arry):
    b=promedio(arry)-pendiente(arrx,arry)*promedio(arrx)
    return b
def lnb(arrx,arry):
    size = len(arrx)
    b=promedio(arry)-lnpendiente(arrx,arry)*lnpromedio(arrx)
    return b

def formula_recta(arrx,arry):
    y=[]
    for i in arrx:
        y.append(pendiente(arrx,arry)*i+(b(arrx,arry)))
    return y

def formula_logaritmo(arrx,arry):
    y=[]
    for i in arrx:
       y.append(lnpendiente(arrx,arry)*math.log(i)+(lnb(arrx,arry)))
       # y.append(math.log(i))
    return y

csv_file = open('eje11.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
anios = []
dp = []
inpe = []
prpollo = []
prcerdo = []
prres = []
for row in csv_reader:
    aniosaux, dpaux, inpeaux, prpolloaux, prcerdoaux, prresaux, a = row
    anios.append((float(aniosaux)))
    dp.append((float(dpaux)))
    inpe.append((float(inpeaux)))
    prpollo.append((float(prpolloaux)))
    prcerdo.append((float(prcerdoaux)))
    prres.append((float(prresaux)))


varaux = prres
print('Media: ', array_media(varaux))
print('Mediana:', array_mediana(varaux))
print('Desviacion estandar:', array_desviacion(varaux))
print('Sesgo:', array_sesgo(varaux))
print('Kurtosis:', array_kurtosis(varaux))
print('Jarque bera:', array_jaque_bera(varaux))
beta = b(varaux,dp)
pend = pendiente(varaux,dp)
lnbeta = lnb(varaux,dp)
lnpend = lnpendiente(varaux,dp)
print('beta : ',beta)
print('pendiente = ',pend)
print('y = ',pend,' * x + ',beta)
print('lnbeta : ',lnbeta)
print('lnpendiente = ',lnpend)
print('y = ',lnpend,' * x + ',lnbeta)
plt.scatter(varaux, dp, marker='o');
plt.plot(varaux,formula_recta(varaux,dp),)
plt.plot(varaux,formula_logaritmo(varaux,dp))
plt.xlabel('años')
plt.ylabel('demanda de pollo')
plt.title('precio real del res por libra')
plt.show()