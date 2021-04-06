import numpy as np

a1=0.21238673
a2=0.03784707
a3=-0.01731492

rho= 66.9984677

def gamma_0 (a1,a2,a3):
    div = -a3+(1/a3)
    ig1 = a2/div - ((a1/a3)/div)
    ig2 = a1/div - ((a2/a3)/div)
    veci = np.array([1,ig1,ig2])
    return veci

def gamma_1(a1,a2,a3):
    div = -a2+(a1/a3)
    ig0 = a3/div -((1/a3)/div)
    ig2 = a1/div - ((a2/a3)/div)
    veci = np.array([ig0,1,ig2])
    return veci

def gamma_2(a1,a2,a3):
    div = -a1+(a2/a3)
    ig0 = a3/div - ((1/a3)/div)
    ig1 = a2/div - ((a1/a3)/div)
    veci = np.array([ig0,ig1,1])
    return veci

def vecrho(a1,a2,a3,rho):
    div0 = -a3+(1/a3)
    div1 = -a2+(a1/a3)
    div2 = -a1+(a2/a3)
    rho0 = ((1/a3)/div0)*rho
    rho1 = ((1/a3)/div1)*rho
    rho2 = ((1/a3)/div2)*rho
    vecirho = np.array([rho0,rho1,rho2])
    return vecirho


a = np.array([gamma_0(a1,a2,a3),gamma_1(a1,a2,a3),gamma_2(a1,a2,a3)])
b = np.array(vecrho(a1,a2,a3,rho))

x = np.linalg.solve(a,b)

print ('gamma 0',x[0])
print ('gamma 1',x[1])
print ('gamma 2',x[2])
