from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt


def problema(numero_simulaciones=1):

    print ""
    print "********************************************************************************"
    print "********************************** Problema 9 **********************************"
    print "********************************************************************************"
    print ""

    maximo_de_tiempo = 2000
    
    
    lista_num_trabajos = []
    lista_interrup_a = []
    lista_esperanza_trabajo = []

    prom_num_trabajos = 0
    prom_interrup_a = 0
    prom_esperanza_trabajo = 0

    print "----------------------------------------------------------------"
    print "------------------- Preparando la simulacion! ------------------"
    print "----------------------------------------------------------------"
    print "Parametros: "
    print "----------------------------------------------------------------"
    print "(a) maximo_de_tiempo %d" % (maximo_de_tiempo)

    for i in range(numero_simulaciones):
        x = iniciar_simulacion(maximo_de_tiempo)
        lista_num_trabajos.append(x[0])
        lista_interrup_a.append(x[1])
        lista_esperanza_trabajo.append(x[2])
        prom_num_trabajos += x[0]
        prom_interrup_a += x[1]
        prom_esperanza_trabajo += x[2]


    prom_num_trabajos /= numero_simulaciones
    prom_interrup_a /= numero_simulaciones
    prom_esperanza_trabajo /= numero_simulaciones


    m_error_95_decl = error_95_prcnt(lista_num_trabajos, prom_num_trabajos)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio TOTAL de trabajos en el taller en cualquier momento es: %0.2f" % (prom_num_trabajos)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento del promedio de trabajos esta entre %f y %f" % (prom_num_trabajos - m_error_95_decl, prom_num_trabajos + m_error_95_decl)
    print "----------------------------------------------------------------------"
    print ""

    m_error_95_decl = error_95_prcnt(lista_interrup_a, prom_interrup_a)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio TOTAL del porcentaje de tiempo que se para el centro A por falta de espacio en la cola del centro B es: %0.2f" % (prom_interrup_a)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de este porcentaje esta entre %f y %f" % (prom_interrup_a - m_error_95_decl, prom_interrup_a + m_error_95_decl)
    print "----------------------------------------------------------------------"
    print ""

    m_error_95_decl = error_95_prcnt(lista_esperanza_trabajo, prom_esperanza_trabajo)

    print ""
    print "----------------------------------------------------------------------"
    print "El promedio TOTAL esperado de la terminacion del trabajo es: %0.2f" % (prom_esperanza_trabajo)

    print "----------------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento de la terminacion del trabajo esta entre %f y %f" % (prom_esperanza_trabajo - m_error_95_decl, prom_esperanza_trabajo + m_error_95_decl)
    print "----------------------------------------------------------------------"
    print ""


