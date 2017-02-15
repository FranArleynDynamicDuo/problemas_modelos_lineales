from __future__ import division
from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt


def problema(numero_simulaciones=1):

    print ""
    print "********************************************************************************"
    print "********************************** Problema 9 **********************************"
    print "********************************************************************************"
    print ""

    maximo_de_tiempo = 2000

    lista_prct_desa = []
    lista_prct_desb = []
    prom_lista_prct_desa = 0
    prom_lista_prct_desb = 0
    
    print "----------------------------------------------------------------"
    print "------------------- Preparando la simulacion! ------------------"
    print "----------------------------------------------------------------"
    print "Parametros: "
    print "----------------------------------------------------------------"
    print "(a) maximo_de_tiempo %d" % (maximo_de_tiempo)

    for i in range(numero_simulaciones):
        x = iniciar_simulacion(maximo_de_tiempo)
        lista_prct_desa.append(x[0])
        lista_prct_desb.append(x[1])
        prom_lista_prct_desa += x[0]
        prom_lista_prct_desb += x[1]

    prom_lista_prct_desa /= numero_simulaciones
    prom_lista_prct_desb /= numero_simulaciones

    m_error_95_decl = error_95_prcnt(lista_prct_desa, prom_lista_prct_desa)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio de porcentaje de tiempo de desocupado del terminal A TOTAL es: %0.2f" % (prom_lista_prct_desa)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento del tiempo de desocupado (A) esta entre %f y %f" % (prom_lista_prct_desa - m_error_95_decl, prom_lista_prct_desa + m_error_95_decl)
    print "----------------------------------------------------------------------"
    print ""

    m_error_95_decl = error_95_prcnt(lista_prct_desb, prom_lista_prct_desb)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio de porcentaje de tiempo de desocupado del terminal B es: %0.2f" % (prom_lista_prct_desb)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento del tiempo de desocupado (B) esta entre %f y %f" % (prom_lista_prct_desb - m_error_95_decl, prom_lista_prct_desb + m_error_95_decl)
    print "----------------------------------------------------------------------"
    print ""
