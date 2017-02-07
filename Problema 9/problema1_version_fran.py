import random
from problema1_aleatorio import random_arrival_time, proximo_evento,\
    random_service_time

LLEGADA = 'llegada'
SERVICIO = 'servicio'
INFINITO = 999999999
maximo_personas = 20
maximo_servidores = 4
cola = 0
llegada_persona = maximo_personas * [0]
servidor_disponible = maximo_servidores * [True]
tiempo_servicio = maximo_servidores * [0]
tiempo_actual = 0

for i in range(maximo_personas):
    llegada_persona[i] = random_arrival_time()
personas = 0


while (personas < maximo_personas or not all(servidor_disponible) or cola > 0):
    servidor_recien_asignado = 10
    print "Tiempo Actual: %0.6f" % (tiempo_actual)
    print personas
    if personas < maximo_personas:
        tiempo_para_evento = proximo_evento(
            llegada_persona[personas],
            tiempo_servicio,
            servidor_disponible)
    else:
        tiempo_para_evento = proximo_evento(
            INFINITO,
            tiempo_servicio,
            servidor_disponible)
    print "El proximo evento ocurrira en %0.6f" % (tiempo_para_evento)
    print "En la cola inicial hay: %d" % (cola)
    print "Tiempos de llegada"
    print llegada_persona
    print tiempo_servicio
    print servidor_disponible
    tiempo_actual += tiempo_para_evento

    if personas < maximo_personas:
        llegada_persona[personas] -= tiempo_para_evento
    
        if llegada_persona[personas] == 0:
            if cola == 0 and any(servidor_disponible):
                for j in range(maximo_servidores):
                    if servidor_disponible[j]:
                        tiempo_servicio[j] = random_service_time()
                        servidor_disponible[j] = False
                        servidor_recien_asignado = j
                        break
            else:
                if cola < 6:
                    cola = cola + 1
                else:
                    resp = random.random()
    
                    if 6 <= cola and cola <= 8:
                        if resp > 0.20:
                            cola = cola + 1
    
                    elif 9 <= cola and cola <= 10:
                        if resp > 0.40:
                            cola = cola + 1
    
                    elif 11 <= cola and cola <= 14:
                        if resp > 0.60:
                            cola = cola + 1
    
                    elif 15 >= cola:
                        if resp > 0.80:
                            cola = cola + 1
            personas += 1
    
    for i in range(maximo_servidores):
        if tiempo_servicio[i] > 0 and not servidor_disponible[
                i] and servidor_recien_asignado != i:
            tiempo_servicio[i] -= tiempo_para_evento
            if tiempo_servicio[i] == 0:
                if cola > 0:
                    cola -= 1
                    tiempo_servicio[i] = random_service_time()
                    servidor_disponible[i] = False
                else:
                    servidor_disponible[i] = True
