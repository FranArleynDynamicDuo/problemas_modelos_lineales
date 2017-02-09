from __future__ import division

class Persona:

    def __init__(self,tiempo_llegada=0):
        self.tiempo_sistema = 0
        self.tiempo_llegada = tiempo_llegada

    @staticmethod
    def tiempo_promedio_en_sistema(lista_personas):
        resultado = 0
        for persona in lista_personas:
            resultado += persona.tiempo_sistema
        return resultado/len(lista_personas)

    def __str__(self):
        return "Tiempo Llegada %0.6f" % self.tiempo_llegada

    def __unicode__(self):
        return "Tiempo Llegada %0.6f" % self.tiempo_llegada
