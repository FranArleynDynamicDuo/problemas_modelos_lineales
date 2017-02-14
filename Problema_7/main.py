# *** coding: utf*8 ***
from simulacion import iniciar_simulacion
import math

def varianza( lis_data, promedio ):
    suma = 0
    for i in range(len(lis_data)):
        suma += ((lis_data[i] - promedio)*(lis_data[i] - promedio))
    suma /= (len(lis_data))
    return suma

def error_95_prcnt (lis_data, promedio):
    varz = varianza( lis_data, promedio )
    nmuestra = len(lis_data)
    return (1.96*(math.sqrt(varz/nmuestra)))  

def problema(numero_simulaciones):

	print ""
	print "********************************************************************************"
	print "********************************** Problema 7 **********************************"
	print "********************************************************************************"
	print ""

	MAXIMO_DIAS = 60
	Q = 100
	acum_reorden = 0
	acum_costo_unidades = 0

	print "----------------------------------------------------------------"
	print "------------------- Preparando la simulacion! ------------------"
	print "----------------------------------------------------------------"
	print "Parametros: "
	print "----------------------------------------------------------------"
	print "(a) maximo_dias %d" % (MAXIMO_DIAS)
	print "(b) maximo_punto_reorden %d" % (Q)
	print "----------------------------------------------------------------"
	print ""

	print "----------------------------------------------------------------"
	print "------------------- Iniciando la simulacion! -------------------"
	print "----------------------------------------------------------------"
	print ""

	for i in range(numero_simulaciones):
		result = iniciar_simulacion(MAXIMO_DIAS,Q)

		acum_reorden += result[0]
		lista_reorden.append(result[0])
		acum_costo_unidades += result[1]
		lista_costo_unidades.append(result[1])

	# Calculamos la media del punto de reorden optimo y de la sunidades de costo
	media_reorden = acum_reorden/numero_simulaciones
	media_costo_unidades = acum_costo_unidades/numero_simulaciones
	# Calculamos el margen de error del punto de reorden optimo y de las unidades de costo
	m_error_95_reorden = error_95_prcnt( lista_reorden, media_reorden)
	m_error_95_costo_unidades = error_95_prcnt( lista_costo_unidades, media_costo_unidades)

	print "----------------------------------------------------------------"
	print "---------------- Se ha terminado la simulacion! ----------------"
	print "----------------------------------------------------------------"
	print "Analisis de resultados: "
	print "----------------------------------------------------------------"
	print "(a) El punto de reorden optimo es %d unidades con costo $%d " % (media_reorden, media_costo_unidades)
	print "---------------------------------------------------------------- "
	print ""

	print "----------------------------------------------------------------"
	print "Intervalo de Confianza: "
	print "----------------------------------------------------------------"
	print ""
	print "----------------------------------------------------------------------"
	print "El intervalo de confianza de 95 por ciento del punto de reorden optimo esta entre (%f , %f)" % (media_reorden-m_error_95_reorden,media_reorden+m_error_95_reorden)
	print "El intervalo de confianza de 95 por ciento de las unidades de costo esta entre (%f , %f)" % (media_costo_unidades-m_error_95_costo_unidades,media_costo_unidades+m_error_95_costo_unidades)
	print "----------------------------------------------------------------------"
	print ""



y = input("Numero de simulaciones: ")
numero_simulaciones = int(y)

lista_reorden = []
lista_costo_unidades = []
promedio_total = 0

problema(numero_simulaciones)

