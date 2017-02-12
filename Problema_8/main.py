# *** coding: utf*8 ***
from simulacion import iniciar_simulacion

print ""
print "********************************************************************************"
print "********************************** Problema 8 **********************************"
print "********************************************************************************"
print ""

numero_simulaciones = 1
MAXIMO_DIAS = 60
Q = 100
VENDEDORES = 5

for i in range(numero_simulaciones):
    iniciar_simulacion(VENDEDORES)
