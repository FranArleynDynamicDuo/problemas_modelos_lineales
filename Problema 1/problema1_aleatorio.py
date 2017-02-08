import random
import numpy

CLIENTS_PER_HOUR = 60
UNIFORM_LOW = 3
UNIFORM_HIGH = 5


def random_arrival_time():
    return numpy.random.exponential(scale=1)


def random_cola():
    proc_cola = random.random()
    print proc_cola
    return 1


def random_service_time():
    return numpy.random.uniform(low=UNIFORM_LOW, high=UNIFORM_HIGH)


def tiempo_servicio_valido(tiempo_servicio, servidores_disponible):
    lista = []
    for x in range(len(servidores_disponible)):
        if not servidores_disponible[x]:
            lista.append(tiempo_servicio[x])
    return lista


def proximo_evento(proxima_llegada, tiempo_servicio, servidores_disponible):
    servidores_validos = tiempo_servicio_valido(
        tiempo_servicio,
        servidores_disponible)
    if len(servidores_validos) > 0:
        if proxima_llegada <= min(servidores_validos):
            return proxima_llegada
        elif proxima_llegada > min(servidores_validos):
            return min(servidores_validos)
    else:
        return proxima_llegada
