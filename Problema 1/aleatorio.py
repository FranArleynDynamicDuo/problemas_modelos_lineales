import numpy
import random

from cajero import Cajero


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


def random_decline(cola_por_atender, cola_por_llegar, personas_que_declinaron):
    resp = random.random()

    if 6 <= cola_por_atender.tamano(
    ) and cola_por_atender.tamano() <= 8:
        if resp > 0.20:
            cola_por_atender.encolar(
                cola_por_llegar.desencolar())
        else:
            personas_que_declinaron += 1
            cola_por_llegar.desencolar()

    elif 9 <= cola_por_atender.tamano() and cola_por_atender.tamano() <= 10:
        if resp > 0.40:
            cola_por_atender.encolar(
                cola_por_llegar.desencolar())
        else:
            personas_que_declinaron += 1
            cola_por_llegar.desencolar()

    elif 11 <= cola_por_atender.tamano() and cola_por_atender.tamano() <= 14:
        if resp > 0.60:
            cola_por_atender.encolar(
                cola_por_llegar.desencolar())
        else:
            personas_que_declinaron += 1
            cola_por_llegar.desencolar()

    elif 15 >= cola_por_atender.tamano():
        if resp > 0.80:
            cola_por_atender.encolar(
                cola_por_llegar.desencolar())
        else:
            personas_que_declinaron += 1
            cola_por_llegar.desencolar()


def proximo_evento(proxima_llegada, cajeros):
    servidores_validos = Cajero.tiempo_servicio_valido(
        cajeros)
    if len(servidores_validos) > 0 and proxima_llegada is not None:
        if proxima_llegada <= min(servidores_validos):
            return proxima_llegada
        elif proxima_llegada > min(servidores_validos):
            return min(servidores_validos)
    elif proxima_llegada is None:
        return min(servidores_validos)
    else:
        return proxima_llegada
