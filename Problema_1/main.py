# -*- coding: utf-8 -*-
from simulacion import iniciar_simulacion

print ""
print "********************************************************************************"
print "********************************** Problema 1 **********************************"
print "********************************************************************************"
print ""

maximo_personas = 2000
maximo_servidores = 6
numero_simulaciones = 1


for i in range(numero_simulaciones):
    iniciar_simulacion(maximo_personas, maximo_servidores)