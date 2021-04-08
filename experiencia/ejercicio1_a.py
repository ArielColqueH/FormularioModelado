import matplotlib

matplotlib.use('tkagg')
import matplotlib.pyplot as plt

n=100

vecx = []
vect = []
for i in range(n):
    div = i + 1
    if(i==0):
        vecx.append(1/div)
    else:
        vecx.append(vecx[i-1]/div)
    vect.append(i)
print(vecx)

plt.plot(vect,vecx)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Values')
plt.show()