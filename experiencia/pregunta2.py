import numpy as np
import matplotlib.pyplot as plt
def promedio(num):
    sum = 0
    for i in num:
        sum += i
    return sum / len(num)


def sumatoria_arr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def sumatoria_arr_sqrt(arr):
    sum = 0
    for i in arr:
        sum += (i ** 2)
    return sum

def sumatoria_arrx_arry(arrx1, arrx2):
    sum = 0
    for i in range(len(arrx1)):
        sum += (arrx1[i]*arrx2[i])
    return sum
def pendiente(arrx,arry):
    n=len(arrx)
    dividendo = n*sumatoria_arrx_arry(arrx,arry)-sumatoria_arr(arrx)*sumatoria_arr(arry)
    divisor = n*sumatoria_arr_sqrt(arrx)-(sumatoria_arr(arrx)**2)
    return dividendo/divisor
def b(arrx,arry):
    b=promedio(arry)-pendiente(arrx,arry)*promedio(arrx)
    return b

def formula_recta(arrx,arry,x):
    y=pendiente(arrx,arry)*x+(b(arrx,arry))
    return y

poblacion = [1000000,3500000, 6300000,10000000]
anio = [1900,1950,1990,2010]
print('Pendiente : ',pendiente(anio,poblacion))
print('b : ',b(anio,poblacion))
print('y : ',formula_recta(anio,poblacion,2020))
varAnio=2020
poblacion.append(formula_recta(anio,poblacion,varAnio))
anio.append(varAnio)
plt.plot(anio,poblacion)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Poblacion')
plt.show()