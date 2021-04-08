import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

datos = pd.read_excel("data.xlsx")
v = datos["w"]
w = datos["x"]
s = datos["y"]
t = datos["z"]

sum_w_e = w.dot(np.exp(v.pow(2/3))).sum()
w_mean_e = w.mean()*(np.exp(v.pow(2/3)).sum())
e_square = np.exp(v.pow(2/3)).pow(2).sum()
last = np.exp(v.pow(2/3)).mean()*np.exp(v.pow(2/3)).sum()

w_mean = w.mean()
e_mean = np.exp(v.pow(2/3)).mean()

lamda = (sum_w_e - w_mean_e)/(e_square - last)
beta = w_mean - (lamda * e_mean)
print(lamda)
print(beta)

top1 = v.dot(np.exp(s)).sum() * (np.exp(s).dot((s+t).pow(3/2)).sum())
top2 = v.dot((s+t).pow(3/2)).sum() * (np.exp(s).pow(2).sum())
bottom1 = (np.exp(s).dot((s+t).pow(3/2)).sum())**2
bottom2 = (np.exp(s).pow(2).sum()) * (s+t).pow(3/2).pow(2).sum()

alfa1 = (top1-top2)/(bottom1-bottom2)
alfa0 = (v.dot((s+t).pow(3/2)).sum() - (alfa1 * (s+t).pow(3/2).pow(2).sum()))/((np.exp(s).dot((s+t).pow(3/2)).sum()))

print(alfa1)
print(alfa0)

v_est = []
w_est = []
time = []

for i in range(0, s.size):
    v_est.append((alfa0*(math.e**s[i]))+(alfa1 * (math.pow(s[i]+t[i],3/2))))
    time.append(i)
for j in range(0,len(v_est)):
    w_est.append(beta+(lamda * (math.e**(math.pow(v_est[j],2/3)))))

plt.plot(time,w_est,label = "Estimados")
plt.plot(time,w,label = "Real")
plt.legend()
plt.show()