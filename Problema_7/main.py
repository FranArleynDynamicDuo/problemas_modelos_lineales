# *** coding: utf*8 ***
from simulacion import iniciar_simulacion

def problema(numero_simulaciones=1):

    print ""
    print "********************************************************************************"
    print "********************************** Problema 7 **********************************"
    print "********************************************************************************"
    print ""
    
    MAXIMO_DIAS = 60
    Q = 100
    
    for i in range(numero_simulaciones):
        iniciar_simulacion(MAXIMO_DIAS,Q)
