from aleatorio import random_demand, random_delivery_time

Q = 100
COSTO_POR_MANTENER = 0.2
COSTO_POR_ESCASEZ = 1
COSTO_POR_PEDIDO = 10


def iniciar_simulacion(maximo_dias, maximo_punto_reorden):
	# Inicalizamos las variables compartidas 
    costo_minimo = 0
    reorden_optimo = 0
	# Ciclamos por distintos puntos de reorden para conseguir un punto de reorden optimo
    for punto_reorden in range(maximo_punto_reorden):
    	# Inicializamos las variables de la simulacion
        dias_transcurridos = 0
        inventario_actual = Q
        costo_acumulado = 0
        dias_para_proximo_envio = 0
        envio_en_camino = False
		# Iniciamos la simulacion para un nuevo punto de reorden
        for dias_transcurridos in range(maximo_dias):
        	# Si habia un envio en camino pero ya llego, recibimos el envio
            if dias_para_proximo_envio == 0 and envio_en_camino:
            	inventario_actual += Q
                costo_acumulado += COSTO_POR_PEDIDO
                envio_en_camino = False
            # Si hay un envio en camino pero no ha llegado, reducimos el tiempo
            elif dias_para_proximo_envio > 0 and envio_en_camino:
            	dias_para_proximo_envio -= 1
            # 
            demanda_del_dia = random_demand()
            inventario_actual -= demanda_del_dia
            # Manejo del costo de la escasez
            if inventario_actual < 0:
                costo_acumulado += abs(inventario_actual) * COSTO_POR_ESCASEZ
			# Manejo del costo por mantener
            elif inventario_actual > 0:
                costo_acumulado += inventario_actual * COSTO_POR_MANTENER
			# Si estamos por debajo del punto de reorden, hacemos un pedido
            if inventario_actual <= punto_reorden and not envio_en_camino:
            	dias_para_proximo_envio = random_delivery_time()
            	envio_en_camino = True
            
		# Si el punto de reorden en cuestion es el primero, no lo comparo
        if punto_reorden == 0:
            costo_minimo = costo_acumulado
            reorden_optimo = punto_reorden
        elif costo_acumulado < costo_minimo:
            costo_minimo = costo_acumulado
            reorden_optimo = punto_reorden

    print "La punto de reorden optimo es %d unidades con costo $%d " % (reorden_optimo, costo_minimo)
    return [reorden_optimo,costo_minimo]
