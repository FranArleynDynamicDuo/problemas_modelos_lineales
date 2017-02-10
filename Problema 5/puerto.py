from buque import Buque 
from commons.servidor import Servidor

class Puerto(Servidor):
    pass

class Puerto_A(Puerto):
    
    TIEMPO_BUQUE = 4
    TIEMPO_BUQUE_MEDIANO = 3
    TIEMPO_BUQUE_PEQUENO = 2
    
    def recibir_buque(self,buque):
        self.disponible = False
        self.persona_atendida = buque
        if buque.tipo == Buque.BOAT:
            self.tiempo_servicio = self.TIEMPO_BUQUE
        elif buque.tipo == Buque.MEDIUM_BOAT:
            self.tiempo_servicio = self.TIEMPO_BUQUE_MEDIANO
        elif buque.tipo == Buque.SMALL_BOAT:
            self.tiempo_servicio = self.TIEMPO_BUQUE_PEQUENO
    
class Puerto_B(Puerto):
    
    TIEMPO_BUQUE = 3
    TIEMPO_BUQUE_MEDIANO = 2
    TIEMPO_BUQUE_PEQUENO = 1
    
    def recibir_buque(self,buque):
        self.persona_atendida = buque
        self.disponible = False
        if buque.tipo == Buque.BOAT:
            self.tiempo_servicio = self.TIEMPO_BUQUE
        elif buque.tipo == Buque.MEDIUM_BOAT:
            self.tiempo_servicio = self.TIEMPO_BUQUE_MEDIANO
        elif buque.tipo == Buque.SMALL_BOAT:
            self.tiempo_servicio = self.TIEMPO_BUQUE_PEQUENO
            
def Existe_Puerto_Libre(puertos):
    for puerto in puertos:
        if puerto.disponible:
            return True
    return False
