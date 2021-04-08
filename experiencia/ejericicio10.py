import csv
import math
import matplotlib.pyplot as plt
import numpy as np
def combinaciones(difL, limS,limI):
    rango = limS-limI
    numInt=int(rango/difL)
    numInt=numInt+1
    c = 4
    f = pow(41,4)
    nueva_matriz = [[0 for x in range(f)] for y in range(c)]
    matriz_intervalos = [[0 for x in range(numInt+1)] for y in range(1)]
    cont=0
    for i in range (numInt):
        matriz_intervalos[0][i]=limI
        limI=round(limI+difL,2)

    for i in range(numInt):
        for j in range(numInt):
            for k in range(numInt):
                for l in range(numInt):
                    nueva_matriz[0][cont] = matriz_intervalos[0][i]
                    nueva_matriz[1][cont] = matriz_intervalos[0][j]
                    nueva_matriz[2][cont] = matriz_intervalos[0][k]
                    nueva_matriz[3][cont] = matriz_intervalos[0][l]
                    cont = cont + 1

    return nueva_matriz

def imprimirEstimaciones(matriz):
    f = len(matriz) #4
    c = len(matriz[0]) #2825761
    for i in range(100):#solo imprime 100 combinaciones
        print("y^",matriz[0][i]," = x^",matriz[1][i], " + x^",matriz[2][i]," = x^",matriz[3][i])

def transformadaBoxCox(matriz,intervalos,fila):
    f = len(matriz)
    c = len(matriz[0])
    nueva_mat=[[0 for x in range(c-1)] for y in range(f)]
    for i in range(f):
        for j in range(c):
            if(j!=0):
                if(intervalos[j][fila]==0):
                    nueva_mat[i][j-1]=np.log(matriz[i][j])
                else:
                    nueva_mat[i][j-1]=(pow(matriz[i][j],intervalos[j][fila])-1)/intervalos[j][fila]
    return nueva_mat
def estimacionaciones(combinaciones,datosX,datosY):
    tamanio=len(combinaciones[0])-2825661 #solo 100 combinaciones
    mest=[[0 for x in range(4)]for y in range(1)]
    r=0
    for i in range(tamanio):
        aux = transformadaBoxCox(datosX, combinaciones, i)
        matriz_tranpuesta = np.transpose(aux)
        maXtransX=np.dot(matriz_tranpuesta,aux)
        try:
            inversaXtrans_X=np.linalg.inv(maXtransX)
            matriz_inv_xt=np.dot(inversaXtrans_X,matriz_tranpuesta)
            beta=np.dot(matriz_inv_xt,datosY)
            maXB=np.dot(aux,beta)
            SEC=sumatoriaSEC(maXB)
            SRC = sumatoriaSRC(datosY, maXB)
            STC = sumatoriaSTC(datosY)
            R2 = SEC / STC
            if(R2>r):
                r=R2
                mest[0][0] = combinaciones[0][i]
                mest[0][1] = combinaciones[1][i]
                mest[0][2] = combinaciones[2][i]
                mest[0][3] = combinaciones[3][i]
        except:
            print("Excepcion")
    return mest
def promedioY(datos,f):
    fila=len(datos)
    sum = 0
    for i in range(fila):
        sum=sum+datos[i][f]
    return sum /fila

def sumatoriaSEC(datos_f):
    suma=0
    f=len(datos_f)
    promedio=promedioY(datos_f,0)
    for i in range(f):
        suma=suma+(datos_f[i][0]-promedio)*(datos_f[i][0]-promedio)
    return suma
def matrizElevadoCuadrado(a):
    fil = len(a)
    col = len(a[0])
    c = [[0 for x in range(col)] for y in range(fil)]
    for i in range(fil):
        for j in range(col):
            c[i][j]=math.pow(a[i][j],2)
    return c

def sumatoriaSRC(datosY, datosBeta):
    matrizY_yestimado = datosY-datosBeta
    matrizY_y2 = matrizElevadoCuadrado(matrizY_yestimado)
    sum=0
    for i in range(len(matrizY_y2)):
        sum=sum+matrizY_y2[i][0]
    return sum
def sumatoriaSTC(datos):
    sum=0
    promedio=promedioY(datos,0)
    for i in range(len(datos)):
        sum=sum+(datos[i][0]-promedio)*(datos[i][0]-promedio)
    return sum
def mostrarMatrizDouble(matriz):
    f = len(matriz)
    c = len(matriz[0])
    for i in range(f):
        cad=''
        for j in range(c):
            cad=cad+str(matriz[i][j])+'  '
        print(cad)

csv_file = open('../simulacion1.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
promedioNotaArray = []
edadArray = []
materiaArray = []
horasEstudioArray = []
recreoArray = []
amigosArray = []

for row in csv_reader:
    promedio_nota, edad, materia, horas_estudio, recreo, amigos = row
    promedioNotaArray.append(float(promedio_nota))
    edadArray.append(float(edad))
    materiaArray.append(float(materia))
    horasEstudioArray.append(float(horas_estudio))
    recreoArray.append(float(recreo))
    amigosArray.append(float(amigos))
#Segunda opcion de llenar tus datos mediante un archivo csv
def matriz_datos(arrx1,arrx2,arrx3):
    matriz_x = np.empty((37, 4))
    #print(matriz_x)
    for i in range(37):
        matriz_x[i][0]=1
        matriz_x[i][1]=arrx1[i]
        matriz_x[i][2]=arrx2[i]
        matriz_x[i][3]=arrx3[i]
    #print(matriz_x)
    return matriz_x
def matriz_datosY(arry):
    matriz_y = np.empty((37, 1))
    for i in range(37):
        matriz_y[i][0]=arry[i]
    #print(matriz_y)
    return matriz_y


datos=matriz_datos(edadArray,materiaArray,horasEstudioArray)
datosy=matriz_datosY(promedioNotaArray)
nueva_matriz=combinaciones(0.1, 2,-2)

imprimirEstimaciones(nueva_matriz)
print("y x1  x2 x3 ")
mestimado=estimacionaciones(nueva_matriz,datos,datosy)
print()
mostrarMatrizDouble(mestimado)