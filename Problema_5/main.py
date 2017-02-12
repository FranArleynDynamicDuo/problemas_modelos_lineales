# -*- coding: utf-8 -*-
from simulacion import iniciar_simulacion

print ""
print "********************************************************************************"
print "********************************** Problema 5 **********************************"
print "********************************************************************************"
print ""

maximo_personas = 100
maximo_servidores = 2
numero_simulaciones = 1

for i in range(numero_simulaciones):
    iniciar_simulacion(maximo_personas)

