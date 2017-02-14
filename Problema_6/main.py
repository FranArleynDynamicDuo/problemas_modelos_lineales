from simulacion import iniciar_simulacion
from random import sample
from commons.estadistica import error_95_prcnt
# Tint = tiempo de recorrido en segundos entre una estacion y otra.
# Npas = numero de pasajeros a bordo entre las estaciones consideradas.
# Tde = tiempo total de desembarque y embarque de pasajeros (en segundos)







def problema(numero_simulaciones):

    print ""
    print "********************************************************************************"
    print "********************************** Problema 6 **********************************"
    print "********************************************************************************"
    print ""


    print "----------------------------------------------------------------"
    print "------------------- Preparando la simulacion! ------------------"
    print "----------------------------------------------------------------"
    print ""

    Nemb = [127,162,179,75,223,186,124,45,100,171,235,176,130,159,117,100,92,68,242,122,184,84,240,319,61,78,20,141,202, 
        213,204,360,169,206,326,210,335,233,102,243,135,310,138,95,216,99,346,220,191,230,219,225,271,270,110,305,157,
        128,163,90,148,70,40,80,105,159,141,150,164,200,213,195,134,141,107,177,109,48,145,114,400,212,258,198,229,175,
        199,177,194,185,303,335,310,104,374,190,211,160,138,227,122,230,97,166,232,187,212,125,119,90,286,310,115,277,
        189,159,266,170,28,141,155,309,152,122,262,111,254,124,138,190,136,110,396,96,86,111,81,226,50,134,131,120,112,
        140,280,145,208,333,250,221,318,120,72,166,194,87,94,170,65,190,359,312,205,77,197,359,174,140,167,181,143,99,
        297,92,246,211,275,224,171,290,291,220,239,126,89,66,35,26,129,234,181,180,58,40,54,123,78,319,389,121]

    
    acum_tiempo_total = 0
    acum_prom_pasajero = 0
    acum_maximo_pasajero = 0
    lista_tiempo_total = []
    lista_prom_pasajero = []
    lista_maximo_pasajero = []

    print "----------------------------------------------------------------"
    print "------------------- Iniciando la simulacion! -------------------"
    print "----------------------------------------------------------------"
    print ""

    for i in range(numero_simulaciones):
        embarques = sample(Nemb, 9)
        result = iniciar_simulacion(embarques)

        acum_tiempo_total += result[0]
        acum_prom_pasajero += result[1]
        acum_maximo_pasajero += result[2]

        lista_tiempo_total.append(result[0])
        lista_prom_pasajero.append(result[1])
        lista_maximo_pasajero.append(result[2])
    
    # Calculamos la media del tiempo total, promedio de pasajero y maximo de pasajeros
    media_tiempo_total = acum_tiempo_total/numero_simulaciones
    media_prom_pasajero = acum_prom_pasajero/numero_simulaciones
    media_maximo_pasajero = acum_maximo_pasajero/numero_simulaciones

    # Se calcula el margen de error del tiempo total, promedio de pasajero y maximo de pasajeros
    m_error_95_tiempo_total = error_95_prcnt(lista_tiempo_total, media_tiempo_total)
    m_error_95_prom_pasajero = error_95_prcnt(lista_prom_pasajero, media_prom_pasajero)
    m_error_95_maximo_pasajero = error_95_prcnt(lista_maximo_pasajero, media_maximo_pasajero)

    print "----------------------------------------------------------------"
    print "---------------- Se ha terminado la simulacion! ----------------"
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(a) El tiempo total del recorrido en segundos: %0.2f " % (media_tiempo_total)
    print "(b) El nro de pasajeros promedio a bordo del tren es: %0.2f" % (media_prom_pasajero)  
    print "(c) El nro maximo de pasajeros embarcados es: %d " % (media_maximo_pasajero)
    print ""
    print "----------------------------------------------------------------"
    print "Intervalo de Confianza: "
    print "----------------------------------------------------------------"
    print "El intervalo de confianza de 95 por ciento del tiempo total esta entre (%0.2f , %0.2f)" % (media_tiempo_total-m_error_95_tiempo_total,media_tiempo_total+m_error_95_tiempo_total)
    print "El intervalo de confianza de 95 por ciento del promedio de pasajeros esta entre (%0.2f , %0.2f)" % (media_prom_pasajero-m_error_95_prom_pasajero,media_prom_pasajero+m_error_95_prom_pasajero)
    print "El intervalo de confianza de 95 por ciento del maximo de pasajeros esta entre (%0.2f , %0.2f)" % (media_maximo_pasajero-m_error_95_maximo_pasajero,media_maximo_pasajero+m_error_95_maximo_pasajero)
    print ""
