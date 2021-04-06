import math
tazaAhorro=0.2
depreciacionCapital = 0.12
crecimientoTecnologia = 0.18
crecimientoPoblacion = 0.22

def estacionario(tazaAhorro,depreciacionCapital,crecimientoTecnologia,crecimientoPoblacion):
    dividendo = tazaAhorro
    divisor = depreciacionCapital+crecimientoTecnologia+crecimientoPoblacion
    res = math.pow(dividendo/divisor,2)
    return res

ee=estacionario(tazaAhorro,depreciacionCapital,crecimientoTecnologia,crecimientoPoblacion,)
print('Capital correspondiente al estado estacionario por trabajador : ',ee)
print('PIB : ',math.sqrt(ee))
print('Consumo por trabajador : ',(1-tazaAhorro)*math.sqrt(ee))

