import numpy
import random

def tiempo_de_llegada():
	return numpy.random.exponential(scale=0.083)

def proximo_evento(proxima_llegada, cajeros):
    servidores_validos = Cajero.tiempo_servicio_valido(cajeros)
    
    if servidores_validos == [] and proxima_llegada == 0:
        print "Error"
        exit()
    if len(servidores_validos) > 0 and proxima_llegada is not None:
        if min(servidores_validos) == 0:
            print "Error"
            exit()
        if proxima_llegada <= min(servidores_validos):
            return proxima_llegada
        elif proxima_llegada > min(servidores_validos):
            return min(servidores_validos)
    elif proxima_llegada is None:
        return min(servidores_validos)
    else:
        return proxima_llegada