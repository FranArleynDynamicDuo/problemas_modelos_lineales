# *** coding: utf*8 ***
from simulacion import iniciar_simulacion
import math

def varianza( lis_data, promedio ):
    suma = 0
    for i in range(len(lis_data)):
        suma += ((lis_data[i] - promedio)*(lis_data[i] - promedio))
    suma /= (len(lis_data))
    return suma

def error_95_prcnt (lis_data, promedio):
    varz = varianza( lis_data, promedio )
    nmuestra = len(lis_data)
    return (1.96*(math.sqrt(varz/nmuestra)))  

print ""
print "********************************************************************************"
print "********************************** Problema 8 **********************************"
print "********************************************************************************"
print ""

y = input("Numero de simulaciones: ")
numero_simulaciones = int(y)
MAXIMO_DIAS = 60
Q = 100
VENDEDORES = 5
promedio_total = 0
lista_ventas = []

for i in range(numero_simulaciones):
    x = iniciar_simulacion(VENDEDORES)
    lista_ventas.append(x)
    promedio_total += x

# Se calcula la media para 
promedio_total /= numero_simulaciones
    
# Se calcula el margen de error
m_error_95 = error_95_prcnt(lista_ventas, promedio_total)

print ""
print "----------------------------------------------------------------------"
print "El promedio de ventas TOTAL es: %f" % (promedio_total)

print "----------------------------------------------------------------------"
print "El intervalo de confianza de 95 por ciento esta entre %f y %f" % (promedio_total-m_error_95,promedio_total+m_error_95)
print "----------------------------------------------------------------------"
print ""
