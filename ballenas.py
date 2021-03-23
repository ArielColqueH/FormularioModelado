import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


# def f(x,y):
#     tasa_natalidad = 0.06
#     tasa_mortalidad = 0.04
#     tasa_pesca = 0.136
#
#     dxdt = tasa_natalidad * x - tasa_mortalidad * x - tasa_pesca * x
#     return (dxdt)
#
#
# poblacion_inicial = 15000
#
# t = np.linspace(1989, 2089, num=100)
# y = odeint(f, poblacion_inicial,t)
# print(y)

# plt.plot(t,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Poblacion de ballenas')
# plt.show()


def f2(x):
    tasa_natalidad = 0.06
    tasa_mortalidad = 0.04
    tasa_pesca = 0.136
    res = tasa_natalidad * x - tasa_mortalidad * x - tasa_pesca * x
    return (res)

dt = 1
l=100
iteraciones = int((l/dt))
xx = np.zeros(iteraciones+1)
yy = np.zeros(iteraciones+1)
xx[0], yy[0] = 1989, 15000
for i in range (iteraciones):
    y_dot = f2(yy[i])
    yy[i+1] = yy[i] + y_dot*dt
    xx[i+1] = xx[i] + dt
    print(xx[i],yy[i])

plt.plot(xx,yy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Poblacion de ballenas')
plt.show()



