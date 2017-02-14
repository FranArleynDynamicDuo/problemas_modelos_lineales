# -*- coding: utf-8 -*-
from __future__ import division

from aleatorio import tiempo_de_llegada
from commons.cola import Cola
from commons.servidor import Servidor
from persona import Persona
from Problema_9.aleatorio import proximo_evento, random_service_time_A,\
    randome_service_time_B


def iniciar_simulacion(maximo_personas):

    cola_por_llegar = Cola()

    personas_fuera_del_sistema = []
    lista_servidores = [Servidor(), Servidor()]
    centro_a = lista_servidores[0]
    centro_b = lista_servidores[1]
    tiempo_actual = 0
    numeros_de_trabajos = 0
    tiempo_interrupcion_A = 0
    tiempo_finalizacion_trabajo = 0
    persona_recien_llegada_A = None
    persona_recien_llegada_B = None

    for i in range(maximo_personas):
        cola_por_llegar.encolar(Persona(tiempo_de_llegada()))

    while (cola_por_llegar.tamano() > 0 or not Servidor.todos_servidores_disponibles(lista_servidores) or centro_b.cola_por_atender.tamano() > 0
           or not Servidor.todos_servidores_disponibles(lista_servidores) or centro_b.cola_por_atender.tamano() > 0):

        persona_recien_llegada_A = None
        persona_recien_llegada_B = None

        # print "Tiempo Actual: %0.6f" % (tiempo_actual)
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

        tiempo_actual += tiempo_para_evento

        # Manejamos las llegadas al sistema
        if cola_por_llegar.tamano() > 0:
            cola_por_llegar.primero().tiempo_llegada -= tiempo_para_evento
            # Verificamos si un cliente ha llegado
            if cola_por_llegar.primero().tiempo_llegada == 0:
                # Si llego un cliente, no hay cola y hay servidor disponible, lo
                # aceptamos
                if centro_a.cola_por_atender.esta_vacia(
                ) and centro_a.disponible:
                    # Encontramos el proximo servidor disponible
                    centro_a.tiempo_servicio = random_service_time_A()
                    centro_a.persona_atendida = cola_por_llegar.desencolar()
                    centro_a.disponible = False
                    persona_recien_llegada_A = centro_a.persona_atendida
                else:
                    centro_a.cola_por_atender.encolar(
                        cola_por_llegar.desencolar())
        # Manejamos las llegadas de la cola A
        if (centro_a.persona_atendida and centro_a.persona_atendida !=
                persona_recien_llegada_A):
            #
            if centro_a.tiempo_servicio > 0:
                centro_a.tiempo_servicio -= tiempo_para_evento
            #
            if centro_a.tiempo_servicio == 0 and centro_b.cola_por_atender.tamano() < 4:
                #
                if centro_b.cola_por_atender.esta_vacia(
                ) and centro_b.disponible:
                    # Encontramos el proximo servidor disponible
                    centro_b.tiempo_servicio = random_service_time_A()
                    centro_b.persona_atendida = centro_a.persona_atendida
                    centro_b.disponible = False
                    persona_recien_llegada_B = centro_a.persona_atendida
                else:
                    centro_b.cola_por_atender.encolar(
                        centro_a.persona_atendida)
                #
                if not centro_a.cola_por_atender.esta_vacia():
                    centro_a.persona_atendida = centro_a.cola_por_atender.desencolar()
                    centro_a.tiempo_servicio = random_service_time_A()
                    centro_a.disponible = False
                else:
                    centro_a.persona_atendida = None
                    centro_a.disponible = True
        # Manejamos las llegadas de la cola B
        if (centro_b.persona_atendida and centro_b.persona_atendida !=
                persona_recien_llegada_B):
            centro_b.tiempo_servicio -= tiempo_para_evento

            if centro_b.tiempo_servicio == 0:
                if centro_b.cola_por_atender.tamano() > 0:
                    personas_fuera_del_sistema.append(
                        centro_b.persona_atendida)
                    centro_b.persona_atendida = centro_b.cola_por_atender.desencolar()
                    centro_b.tiempo_servicio = randome_service_time_B()
                    centro_b.disponible = False
                else:
                    personas_fuera_del_sistema.append(
                        centro_b.persona_atendida)
                    centro_b.persona_atendida = None
                    centro_b.disponible = True
    p_desocupado_a = (
        tiempo_actual -
        lista_servidores[0].tiempo_servicio_total)
    p_desocupado_b = (
        tiempo_actual -
        lista_servidores[1].tiempo_servicio_total)
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(c) El porcentaje de tiempo desocupado de cada terminal"
    print "    Terminal A: %0.6f" % (p_desocupado_a)
    print "    Terminal B: %0.6f" % (p_desocupado_b)
    print "---------------------------------------------------------------- "

    return [p_desocupado_a, p_desocupado_b]
