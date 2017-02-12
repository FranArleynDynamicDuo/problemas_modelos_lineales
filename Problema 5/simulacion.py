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
    lista_servidores = maximo_servidores * [Puerto()]
    buques_fuera_del_sistema = []

    for i in range(maximo_buques):
        cola_por_llegar.encolar(random_boat_type())

    lista_servidores[0] = Puerto_A()
    lista_servidores[1] = Puerto_B()

    print "----------------------------------------------------------------"
    print "------------------- Iniciando la simulacion! -------------------"
    print "----------------------------------------------------------------"
    print ""
    # SIMULACION
    while (cola_por_llegar.tamano() > 0 or not Existe_Puerto_Libre(
            lista_servidores) or cola_por_atender.tamano() > 0):
        servidor_recien_asignado = 10
    #     print "Tiempo Actual: %0.6f" % (tiempo_actual)
        # Verificamos cual es el evento mas proximo
        if cola_por_llegar.tamano() > 0:
            tiempo_para_evento = proximo_evento(
                cola_por_llegar.primero().tiempo_llegada,
                lista_servidores)
        # En caso de que la cola este vacia, hacemos la llamada de manera
        # distinta
        else:
            tiempo_para_evento = proximo_evento(
                None,
                lista_servidores)
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
                        lista_servidores):
                    # Encontramos el proximo servidor disponible
                    for i in range(maximo_servidores):
                        if lista_servidores[i].disponible:
                            lista_servidores[i].recibir_buque(cola_por_llegar.desencolar())
                            servidor_recien_asignado = lista_servidores[i]
                            break
                else:
                    cola_por_atender.encolar(cola_por_llegar.desencolar())
        # Manejo de servidores
        for i in range(maximo_servidores):
            if (lista_servidores[i].tiempo_servicio > 0
                    and not lista_servidores[i].disponible
                    and servidor_recien_asignado != lista_servidores[i]):
                # Disminuimos el tiempo de servicio restante para el cliente
                # actual
                lista_servidores[i].tiempo_servicio -= tiempo_para_evento
                # Le sumamos tiempo de servicio al cajero
                lista_servidores[i].tiempo_servicio_total += tiempo_para_evento
                # Le sumamos tiempo de sistema a la persona siendo atendida por el
                # cajero
                lista_servidores[
                    i].persona_atendida.tiempo_sistema += tiempo_para_evento
                # Verificamos si el cajero termino te atender a alguien
                if lista_servidores[i].tiempo_servicio == 0:
                    buques_fuera_del_sistema.append(
                            lista_servidores[i].persona_atendida)
                    lista_servidores[i].buques_atendidos.append(
                            lista_servidores[i].persona_atendida)
                    if cola_por_atender.tamano() > 0:
                        lista_servidores[i].recibir_buque(cola_por_atender.desencolar())
                    else:
                        lista_servidores[i].persona_atendida = None
                        lista_servidores[i].disponible = True
        # Agregamos tiempo en el sistema a las buques en la cola
        for persona in cola_por_atender.items:
            persona.tiempo_sistema += tiempo_para_evento

    print "----------------------------------------------------------------"
    print "---------------- Se ha terminado la simulacion! ----------------"
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(a) Número promedio de buques tanque en el puerto: %d" % (len(lista_servidores[0].buques_atendidos) + len(lista_servidores[1].buques_atendidos))
    total_tiempo_en_sistema = 0
    for buque in buques_fuera_del_sistema:
        total_tiempo_en_sistema += buque.tiempo_sistema
    print "(b) Número promedio de días que pasa un buque tanque en el puerto: %0.6f" % (total_tiempo_en_sistema / maximo_buques)
    print "(c) El porcentaje de tiempo desocupado de cada terminal"
    print "    Terminal A: %0.6f" % (tiempo_actual - lista_servidores[0].tiempo_servicio_total)
    print "    Terminal B: %0.6f" % (tiempo_actual - lista_servidores[1].tiempo_servicio_total)
    print "---------------------------------------------------------------- "
