from cola import Cola


class Cajero:

    def __init__(self):
        self.disponible = True
        self.persona_atendida = None
        self.cola_por_atender = Cola()
        self.tiempo_servicio = 0
        self.tiempo_servicio_total = 0

    @staticmethod
    def existe_cajero_disponible(lista):
        for cajero in lista:
            if cajero.disponible:
                return True
        return False

    @staticmethod
    def todos_cajeros_disponibles(lista):
        for cajero in lista:
            if not cajero.disponible:
                return False
        return True

    @staticmethod
    def tiempo_servicio_valido(cajeros):
        lista = []
        for x in range(len(cajeros)):
            if not cajeros[x].disponible:
                lista.append(cajeros[x].tiempo_servicio)
        return lista

    def __str__(self):
        return "Tiempo Servicio %0.6f - Disponible %b" % (
            self.tiempo_servicio, self.disponible)

    def __unicode__(self):
        return "Tiempo Servicio %0.6f - Disponible %b" % (
            self.tiempo_servicio, self.disponible)


def cajero_con_menos_cola(lista_cajeros):
    min_cajero_cola = lista_cajeros[0]
    for cajero in lista_cajeros:
        if cajero.cola_por_atender.tamano(
        ) < min_cajero_cola.cola_por_atender.tamano():
            min_cajero_cola = cajero
    return min_cajero_cola
