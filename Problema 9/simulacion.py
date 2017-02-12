# -*- coding: utf-8 -*-
from __future__ import division

from aleatorio import tiempo_de_llegada
from commons.cola import Cola
from persona import Persona

def iniciar_simulacion(maximo_personas):
	print "----------------------------------------------------------------"
	print "------------------- Preparando la simulacion! ------------------"
	print "----------------------------------------------------------------"
	print "Parametros: "
	print "----------------------------------------------------------------"
	print "(a) maximo_personas %d" % (maximo_personas, maximo_servidores)

	cola_por_llegar_para_A = Cola()
	cola_por_atender_para_A = Cola()

	cola_por_llegar_para_B = Cola()
	cola_por_atender_para_B = Cola()


	tiempo_actual = 0
	numeros_de_trabajos = 0
	tiempo_interrupcion_A = 0
	tiempo_finalizacion_trabajo = 0

	for i in range(maximo_personas):
		cola_por_atender_para_A.encolar(Persona( tiempo_de_llegada_A() ))

	for i in range(maximo_personas):
		print cola_por_atender_para_A.desencolar()

	for i in range(maximo_servidores):
        lista_cajeros[i] = Cajero()

    print "----------------------------------------------------------------"
    print "------------------- Iniciando la simulacion! -------------------"
    print "----------------------------------------------------------------"
    print ""

    while (cola_por_llegar.tamano() > 0 or not Cajero.todos_servidores_disponibles(lista_cajeros) or cola_por_atender.tamano() > 0):

		# print "Tiempo Actual: %0.6f" % (tiempo_actual)
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

        tiempo_actual += tiempo_para_evento




