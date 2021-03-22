import numpy as np
import matplotlib

matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [11.353]

t = np.linspace(2018, 2118, num=1000)

tasa_natalidad = 21.75/1000
tasa_mortalidad = 6.77/1000

params = [tasa_natalidad, tasa_mortalidad]


def sim(variable, t, params):
    x = variable[0]
    tasa_natalidad = params[0]
    tasa_mortalidad = params[1]

    dxdt = tasa_natalidad * x - tasa_mortalidad * x
    return ([dxdt])

y = odeint(sim, y0, t, args=(params,))


f,(ax2) = plt.subplots(1)

line1, = ax2.plot(t,y[:,0], color="b")

ax2.set_ylabel("POBLACIÓN")
ax2.set_xlabel("TIEMPO")

plt.show()