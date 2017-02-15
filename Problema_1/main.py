# -*- coding: utf-8 -*-
from __future__ import division

from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones):

    print ""
    print "********************************************************************************"
    print "********************************** Problema 1 **********************************"
    print "********************************************************************************"
    print ""

    maximo_de_tiempo = 450
    maximo_servidores = 4
    lista_porcentaje_declinaron = []
    lista_esperanza_cliente = []
    promedio_total_porcentaje_declinaron = 0
    promedio_total_esperanza_cliente = 0
    promedio_total_cajero1 = 0
    promedio_total_cajero2 = 0
    promedio_total_cajero3 = 0
    promedio_total_cajero4 = 0
    lista_cajero1 = []
    lista_cajero2 = []
    lista_cajero3 = []
    lista_cajero4 = []
    
    print "----------------------------------------------------------------"
    print "------------------- Preparando la simulacion! ------------------"
    print "----------------------------------------------------------------"
    print "Parametros: "
    print "----------------------------------------------------------------"
    print "(a) maximo_de_tiempo %d" % (maximo_de_tiempo)
    print "(b) maximo_servidores %d" % (maximo_servidores)
    print "----------------------------------------------------------------"
    print ""
    
    for i in range(numero_simulaciones):
        x = iniciar_simulacion(maximo_de_tiempo, maximo_servidores)
        lista_porcentaje_declinaron.append(x[0])
        lista_esperanza_cliente.append(x[1])
        promedio_total_porcentaje_declinaron += x[0]
        promedio_total_esperanza_cliente += x[1]
        lista_cajero1.append(x[2][0])
        lista_cajero2.append(x[2][1])
        lista_cajero3.append(x[2][2])
        lista_cajero4.append(x[2][3])
        promedio_total_cajero1 += x[2][0]
        promedio_total_cajero2 += x[2][1]
        promedio_total_cajero3 += x[2][2]
        promedio_total_cajero4 += x[2][3]

    promedio_total_porcentaje_declinaron /= numero_simulaciones
    promedio_total_esperanza_cliente /= numero_simulaciones    

    m_error_95_esp = error_95_prcnt(lista_esperanza_cliente, promedio_total_esperanza_cliente)

    print ""
    print "----------------------------------------------------------------------"
    print "El tiempo esperado que un cliente pasa en el sistema TOTAL es: %0.2f" % (promedio_total_esperanza_cliente)
    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de la esperanza esta entre %0.4f y %0.4f" % (promedio_total_esperanza_cliente-m_error_95_esp,promedio_total_esperanza_cliente+m_error_95_esp)

    m_error_95_decl = error_95_prcnt(lista_porcentaje_declinaron, promedio_total_porcentaje_declinaron)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio de porcentaje de declinación TOTAL es: %0.2f" % (promedio_total_porcentaje_declinaron)
    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de la declinación esta entre %f y %f" % (promedio_total_porcentaje_declinaron-m_error_95_decl,promedio_total_porcentaje_declinaron+m_error_95_decl)


    # Calculamos los intervalos de confianza de cada cajero
    promedio_total_cajero1 /= numero_simulaciones 
    promedio_total_cajero2 /= numero_simulaciones 
    promedio_total_cajero3 /= numero_simulaciones 
    promedio_total_cajero4 /= numero_simulaciones 

    m_error_95_cajero1 = error_95_prcnt(lista_cajero1, promedio_total_cajero1)
    m_error_95_cajero2 = error_95_prcnt(lista_cajero2, promedio_total_cajero2)
    m_error_95_cajero3 = error_95_prcnt(lista_cajero3, promedio_total_cajero3)
    m_error_95_cajero4 = error_95_prcnt(lista_cajero4, promedio_total_cajero4)

    print ""
    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento del tiempo desocupado del :" 
    print "----------------------------------------------------------------------"
    print "		Cajero1: (%f,%f)" % (promedio_total_cajero1 - m_error_95_cajero1, promedio_total_cajero1 + m_error_95_cajero1 )
    print "		Cajero2: (%f,%f)" % (promedio_total_cajero2 - m_error_95_cajero2, promedio_total_cajero2 + m_error_95_cajero2 )
    print "		Cajero3: (%f,%f)" % (promedio_total_cajero3 - m_error_95_cajero3, promedio_total_cajero3 + m_error_95_cajero3 )
    print "		Cajero4: (%f,%f)" % (promedio_total_cajero4 - m_error_95_cajero4, promedio_total_cajero4 + m_error_95_cajero4 )
    print "----------------------------------------------------------------------"
    

