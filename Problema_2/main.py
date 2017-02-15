# -*- coding: utf-8 -*-
from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt


def problema(numero_simulaciones=1):

    print ""
    print "********************************************************************************"
    print "********************************** Problema 1 **********************************"
    print "********************************************************************************"
    print ""

    maximo_de_tiempo = 200
    maximo_servidores = 4
    lista_porcentaje_declinaron = []
    lista_esperanza_cliente = []
    promedio_total_porcentaje_declinaron = 0
    promedio_total_esperanza_cliente = 0
    promedio_total_cajeros1_lista = 0
    promedio_total_cajeros2_lista = 0
    promedio_total_cajeros3_lista = 0
    promedio_total_cajeros4_lista = 0
    lista_cajeros1 = []
    lista_cajeros2 = []
    lista_cajeros3 = []
    lista_cajeros4 =[]

    for i in range(numero_simulaciones):
        x = iniciar_simulacion(maximo_de_tiempo, maximo_servidores)
        lista_porcentaje_declinaron.append(x[0])
        lista_esperanza_cliente.append(x[1])
        lista_cajeros1.append(x[2])
        lista_cajeros2.append(x[3])
        lista_cajeros3.append(x[4])
        lista_cajeros4.append(x[5])
        promedio_total_porcentaje_declinaron += x[0]
        promedio_total_esperanza_cliente += x[1]
        promedio_total_cajeros1_lista += x[2]
        promedio_total_cajeros2_lista += x[3]
        promedio_total_cajeros3_lista += x[4]
        promedio_total_cajeros4_lista += x[5]

    promedio_total_porcentaje_declinaron /= numero_simulaciones
    promedio_total_esperanza_cliente /= numero_simulaciones
    promedio_total_cajeros1_lista /= numero_simulaciones
    promedio_total_cajeros2_lista /= numero_simulaciones
    promedio_total_cajeros3_lista /= numero_simulaciones
    promedio_total_cajeros4_lista /= numero_simulaciones
    
    m_error_95_decl = error_95_prcnt(
        lista_porcentaje_declinaron,
        promedio_total_porcentaje_declinaron)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio de porcentaje de declinación TOTAL es: %0.2f" % (promedio_total_porcentaje_declinaron)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de la declinación esta entre %f y %f" % (promedio_total_porcentaje_declinaron - m_error_95_decl, promedio_total_porcentaje_declinaron + m_error_95_decl)
    print "----------------------------------------------------------------------"
    print ""

    m_error_95_esp = error_95_prcnt(
        lista_esperanza_cliente,
        promedio_total_esperanza_cliente)

    print ""
    print "----------------------------------------------------------------------"
    print "El tiempo esperado que un cliente pasa en el sistema TOTAL es: %0.2f" % (promedio_total_esperanza_cliente)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de la esperanza esta entre %0.4f y %0.4f" % (promedio_total_esperanza_cliente - m_error_95_esp, promedio_total_esperanza_cliente + m_error_95_esp)
    print "----------------------------------------------------------------------"
    print ""
    
    promedio_total_cajerosd_lista = [promedio_total_cajeros1_lista,
                                     promedio_total_cajeros2_lista,
                                     promedio_total_cajeros3_lista,
                                     promedio_total_cajeros4_lista]
    
    lista_cajeros = [lista_cajeros1,
                     lista_cajeros2,
                     lista_cajeros3,
                     lista_cajeros4]
    for i in range(maximo_servidores):
        m_error_95_esp = error_95_prcnt(
            lista_cajeros[i],
            promedio_total_cajerosd_lista[i])
            
        
        print ""
        print "----------------------------------------------------------------------"
        print "El tiempo esperado de porcentaje de desocupacion del cajero %d TOTAL es: %0.2f" % (i,promedio_total_cajerosd_lista[i])
    
        print "----------------------------------------------------------------------"
        print "El intervalo de confianza de 95 por ciento de este cajero esta entre %0.4f y %0.4f" % (promedio_total_cajerosd_lista[i] - m_error_95_esp, promedio_total_cajerosd_lista[i] + m_error_95_esp)
        print "----------------------------------------------------------------------"
        print ""
        
    
