import matplotlib
import math

matplotlib.use('tkagg')
import matplotlib.pyplot as plt

n=100

vecx = []
vect = []
for i in range(n):
    it=1+i
    if(i==0):
        vecx.append(pow(it,-1)-1)
    else:
        vecx.append(pow(it,-1)-vecx[i-1])
    vect.append(i)
print(vecx)

plt.plot(vect,vecx)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Values')
plt.show()