# -*- coding: utf-8 -*-
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

def problema(numero_simulaciones=1):

    print ""
    print "********************************************************************************"
    print "********************problema************** Problema 1 **********************************"
    print "********************************************************************************"
    print ""
    
    maximo_personas = 2000
    maximo_servidores = 6
    lista_porcentaje_declinaron = []
    lista_esperanza_cliente = []
    promedio_total_porcentaje_declinaron = 0
    promedio_total_esperanza_cliente = 0
    
    for i in range(numero_simulaciones):
        x = iniciar_simulacion(maximo_personas, maximo_servidores)
        lista_porcentaje_declinaron.append(x[0])
        lista_esperanza_cliente.append(x[1])
        promedio_total_porcentaje_declinaron += x[0]
        promedio_total_esperanza_cliente += x[1]

    promedio_total_porcentaje_declinaron /= numero_simulaciones
    promedio_total_esperanza_cliente /= numero_simulaciones    
    
    m_error_95_decl = error_95_prcnt(lista_porcentaje_declinaron, promedio_total_porcentaje_declinaron)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio de porcentaje de declinación TOTAL es: %0.2f" % (promedio_total_porcentaje_declinaron)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de la declinación esta entre %f y %f" % (promedio_total_porcentaje_declinaron-m_error_95_decl,promedio_total_porcentaje_declinaron+m_error_95_decl)
    print "----------------------------------------------------------------------"
    print ""
    
    m_error_95_esp = error_95_prcnt(lista_esperanza_cliente, promedio_total_esperanza_cliente)

    print ""
    print "----------------------------------------------------------------------"
    print "El tiempo esperado que un cliente pasa en el sistema TOTAL es: %0.2f" % (promedio_total_esperanza_cliente)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de la esperanza esta entre %0.4f y %0.4f" % (promedio_total_esperanza_cliente-m_error_95_esp,promedio_total_esperanza_cliente+m_error_95_esp)
    print "----------------------------------------------------------------------"
    print ""

