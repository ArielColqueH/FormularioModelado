import numpy as np
import matplotlib

matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [10, 1]

t = np.linspace(0, 50, num=1000)

alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4

params = [alpha, beta, delta, gamma]


def sim(variable, t, params):
    x = variable[0]
    y = variable[1]

    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]

    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return ([dxdt, dydt])

y = odeint(sim, y0, t, args=(params,))


f,(ax1,ax2) = plt.subplots(2)

line1, = ax1.plot(t,y[:,0], color="b")
line2, = ax2.plot(t,y[:,1], color="r")

ax1.set_ylabel("PRESA")
ax2.set_ylabel("PREDADOR")
ax2.set_xlabel("TIEMPO")

plt.show()