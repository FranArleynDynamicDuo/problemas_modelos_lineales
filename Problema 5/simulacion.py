# -*- coding: utf-8 -*-
from __future__ import division

from aleatorio import (random_boat_type, proximo_evento)
from buque import Buque
from commons.cola import Cola
from puerto import Puerto, Existe_Puerto_Libre, Puerto_A, Puerto_B


def iniciar_simulacion(maximo_buques):
    print "----------------------------------------------------------------"
    print "------------------- Preparando la simulacion! ------------------"
    print "----------------------------------------------------------------"
    print "Parametros: "
    print "----------------------------------------------------------------"
    print "(a) maximo_buques %d" % (maximo_buques)
    print "----------------------------------------------------------------"
    print ""
    maximo_servidores = 2
    cola_por_llegar = Cola()
    cola_por_atender = Cola()

    tiempo_actual = 0
    buques_que_declinaron = 0
    lista_cajeros = maximo_servidores * [Puerto()]
    buques_fuera_del_sistema = []

    for i in range(maximo_buques):
        cola_por_llegar.encolar(random_boat_type())

    lista_cajeros[0] = Puerto_A()
    lista_cajeros[1] = Puerto_B()

    print "----------------------------------------------------------------"
    print "------------------- Iniciando la simulacion! -------------------"
    print "----------------------------------------------------------------"
    print ""
    # SIMULACION
    while (cola_por_llegar.tamano() > 0 or not Existe_Puerto_Libre(
            lista_cajeros) or cola_por_atender.tamano() > 0):
        servidor_recien_asignado = 10
    #     print "Tiempo Actual: %0.6f" % (tiempo_actual)
        # Verificamos cual es el evento mas proximo
        if cola_por_llegar.tamano() > 0:
            tiempo_para_evento = proximo_evento(
                cola_por_llegar.primero().tiempo_llegada,
                lista_cajeros)
        # En caso de que la cola este vacia, hacemos la llamada de manera
        # distinta
        else:
            tiempo_para_evento = proximo_evento(
                None,
                lista_cajeros)
        if tiempo_para_evento == 0:
            print "Error tiempo para evento invalido"
            exit()
    #     print "El proximo evento ocurrira en %0.6f" % (tiempo_para_evento)
    #     print "En la cola inicial hay: %d" % (cola_por_llegar.tamano())
    #     print "En la cola de espera hay: %d" % (cola_por_atender.tamano())
        tiempo_actual += tiempo_para_evento
        # Manejamos las llegadas al sistema
        if cola_por_llegar.tamano() > 0:
            cola_por_llegar.primero().tiempo_llegada -= tiempo_para_evento
            # Verificamos si un cliente ha llegado
            if cola_por_llegar.primero().tiempo_llegada == 0:
                # Si llego un cliente, no hay cola y hay servidor disponible, lo
                # aceptamos
                if cola_por_atender.esta_vacia() and Existe_Puerto_Libre(
                        lista_cajeros):
                    # Encontramos el proximo servidor disponible
                    for i in range(maximo_servidores):
                        if lista_cajeros[i].disponible:
                            lista_cajeros[i].recibir_buque(cola_por_llegar.desencolar())
                            servidor_recien_asignado = lista_cajeros[i]
                            break
                else:
                    cola_por_atender.encolar(cola_por_llegar.desencolar())
        # Manejo de servidores
        for i in range(maximo_servidores):
            if (lista_cajeros[i].tiempo_servicio > 0
                    and not lista_cajeros[i].disponible
                    and servidor_recien_asignado != lista_cajeros[i]):
                # Disminuimos el tiempo de servicio restante para el cliente
                # actual
                lista_cajeros[i].tiempo_servicio -= tiempo_para_evento
                # Le sumamos tiempo de servicio al cajero
                lista_cajeros[i].tiempo_servicio_total += tiempo_para_evento
                # Le sumamos tiempo de sistema a la persona siendo atendida por el
                # cajero
                lista_cajeros[
                    i].persona_atendida.tiempo_sistema += tiempo_para_evento
                # Verificamos si el cajero termino te atender a alguien
                if lista_cajeros[i].tiempo_servicio == 0:
                    buques_fuera_del_sistema.append(
                            lista_cajeros[i].persona_atendida)
                    if cola_por_atender.tamano() > 0:
                        lista_cajeros[i].recibir_buque(cola_por_atender.desencolar())
                    else:
                        lista_cajeros[i].persona_atendida = None
                        lista_cajeros[i].disponible = True
        # Agregamos tiempo en el sistema a las buques en la cola
        for persona in cola_por_atender.items:
            persona.tiempo_sistema += tiempo_para_evento

    print "----------------------------------------------------------------"
    print "---------------- Se ha terminado la simulacion! ----------------"
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(a) El tiempo esperado que un cliente pasa en el sistema %0.2f" % (Buque.tiempo_promedio_en_sistema(buques_fuera_del_sistema))
    print "(b) Porcentaje de buques que declinaron %0.2f" % (buques_que_declinaron * 100 / maximo_buques)
    print "(c) El porcentaje de tiempo desocupado de cada cajero"
    for i in range(maximo_servidores):
        print "    Cajero %d: %0.6f" % (i, tiempo_actual - lista_cajeros[i].tiempo_servicio_total)
    print "---------------------------------------------------------------- "
