import matplotlib
import math

matplotlib.use('tkagg')
import matplotlib.pyplot as plt

n=100

vecx = []
vect = []
for i in range(n):
    if(i==0):
        vecx.append(math.cos(pow(math.e,i))-1)
    else:
        vecx.append(math.cos(pow(math.e,i))-vecx[i-1])
    vect.append(i)
print(vecx)

plt.plot(vect,vecx)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Values')
plt.show()