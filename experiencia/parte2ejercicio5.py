import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
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

def formula_recta_2(arrx,arry):
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

csv_file = open('parte2ejercicio5.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
n = []
unidades = []
for row in csv_reader:
    auxn, auxunidades = row
    n.append((float(auxn)))
    unidades.append((float(auxunidades)))

print(n)
print(unidades)
plt.scatter(n, unidades, marker='o');
# plt.plot(n,formula_recta(n,unidades))
plt.xlabel('numero de trabajadores')
plt.ylabel('produccion por miles')

datos = pd.read_csv('parte2ejercicio5.csv')
# print (datos)
xx = datos['n'].values.reshape(-1, 1) # necesitamos un array de 2D para SkLearn
yy = datos['unidades'].values.reshape(-1, 1)
# poly = PolynomialFeatures(degree=2, include_bias=False)
# x_poly = poly.fit_transform(xx)
# model = LinearRegression()
# model.fit(x_poly, yy)
# y_pred = model.predict(x_poly)
# # print(xx)
# # print(x_poly)
# plt.plot(xx, y_pred, color='r')

# poly3 = PolynomialFeatures(degree=3, include_bias=False)
# x_poly3 = poly3.fit_transform(xx)
# model = LinearRegression()
# model.fit(x_poly3, yy)
# y_pred3 = model.predict(x_poly3)
# plt.plot(xx, y_pred3, color='g')
plt.show()