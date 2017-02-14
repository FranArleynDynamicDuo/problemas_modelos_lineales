# *** coding: utf*8 ***
from simulacion import iniciar_simulacion
import math
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones=1):
    
    print ""
    print "********************************************************************************"
    print "********************************** Problema 8 **********************************"
    print "********************************************************************************"
    print ""
    
    VENDEDORES = 5
    promedio_total = 0
    lista_ventas = []
    
    for i in range(numero_simulaciones):
        x = iniciar_simulacion(VENDEDORES)
        lista_ventas.append(x)
        promedio_total += x
    
    promedio_total /= numero_simulaciones
        
    m_error_95 = error_95_prcnt(lista_ventas, promedio_total)
    
    print ""
    print "----------------------------------------------------------------------"
    print "El promedio de ventas TOTAL es: %f" % (promedio_total)
    
    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento esta entre %f y %f" % (promedio_total-m_error_95,promedio_total+m_error_95)
    print "----------------------------------------------------------------------"
    print ""
