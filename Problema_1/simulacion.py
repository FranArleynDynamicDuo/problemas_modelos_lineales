# -*- coding: utf-8 -*-
from __future__ import division

from aleatorio import (random_arrival_time, proximo_evento, random_service_time,
                       random_decline)
from cajero import Cajero
from commons.cola import Cola
from persona import Persona


def iniciar_simulacion(maximo_personas, maximo_servidores):
    print "----------------------------------------------------------------"
    print "------------------- Preparando la simulacion! ------------------"
    print "----------------------------------------------------------------"
    print "Parametros: "
    print "----------------------------------------------------------------"
    print "(a) maximo_personas %d" % (maximo_personas)
    print "(b) maximo_servidores %d" % (maximo_servidores)
    print "----------------------------------------------------------------"
    print ""

    cola_por_llegar = Cola()
    cola_por_atender = Cola()

    tiempo_actual = 0
    personas_que_declinaron = 0
    lista_cajeros = maximo_servidores * [Cajero()]
    personas_fuera_del_sistema = []

    for i in range(maximo_personas):
        cola_por_llegar.encolar(Persona(random_arrival_time()))

    for i in range(maximo_servidores):
        lista_cajeros[i] = Cajero()

    print "----------------------------------------------------------------"
    print "------------------- Iniciando la simulacion! -------------------"
    print "----------------------------------------------------------------"
    print ""
    # SIMULACION
    while (cola_por_llegar.tamano() > 0 or not Cajero.todos_servidores_disponibles(
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
                if cola_por_atender.esta_vacia() and Cajero.existe_servidor_disponible(
                        lista_cajeros):
                    # Encontramos el proximo servidor disponible
                    for i in range(maximo_servidores):
                        if lista_cajeros[i].disponible:
                            lista_cajeros[
                                i].tiempo_servicio = random_service_time()
                            lista_cajeros[
                                i].persona_atendida = cola_por_llegar.desencolar()
                            lista_cajeros[i].disponible = False
                            servidor_recien_asignado = i
                            break
                else:
                    if cola_por_atender.tamano() < 6:
                        cola_por_atender.encolar(cola_por_llegar.desencolar())
                    else:
                        personas_que_declinaron = random_decline(
                            cola_por_atender,
                            cola_por_llegar,
                            personas_que_declinaron,
                            personas_fuera_del_sistema)
        # Manejo de servidores
        for i in range(maximo_servidores):
            if (lista_cajeros[i].tiempo_servicio > 0
                    and not lista_cajeros[i].disponible
                    and servidor_recien_asignado != i):
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
                    if cola_por_atender.tamano() > 0:
                        personas_fuera_del_sistema.append(
                            lista_cajeros[i].persona_atendida)
                        lista_cajeros[
                            i].persona_atendida = cola_por_atender.desencolar()
                        lista_cajeros[
                            i].tiempo_servicio = random_service_time()
                        lista_cajeros[i].disponible = False
                    else:
                        personas_fuera_del_sistema.append(
                            lista_cajeros[i].persona_atendida)
                        lista_cajeros[i].persona_atendida = None
                        lista_cajeros[i].disponible = True
        # Agregamos tiempo en el sistema a las personas en la cola
        for persona in cola_por_atender.items:
            persona.tiempo_sistema += tiempo_para_evento

    print ""
    print "----------------------------------------------------------------"
    print "---------------- Se ha terminado la simulacion! ----------------"
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(a) El tiempo esperado que un cliente pasa en el sistema %0.2f" % (Persona.tiempo_promedio_en_sistema(personas_fuera_del_sistema))
    print "(b) Porcentaje de personas que declinaron %0.2f" % (personas_que_declinaron * 100 / maximo_personas)
    print "(c) El porcentaje de tiempo desocupado de cada cajero"
    for i in range(maximo_servidores):
        print "    Cajero %d: %0.6f" % (i, tiempo_actual - lista_cajeros[i].tiempo_servicio_total)
    print "---------------------------------------------------------------- "
    print ""