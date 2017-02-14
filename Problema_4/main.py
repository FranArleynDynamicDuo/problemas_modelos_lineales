from simulacion import iniciar_simulacion
import math

print ""
print "********************************************************************************"
print "********************************** Problema 4 **********************************"
print "********************************************************************************"
print ""

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


y = input("Numero de simulaciones: ")
numero_simulaciones = int(y)

maquinas_funcionando = 4
maquinas_repuesto    = 3
esperanza = 0
lista_esperanza = []

def problema(esperanza, numero_simulaciones, maquinas_funcionando, maquinas_repuesto):
    acum_esperanza = 0
    for i in range(numero_simulaciones):
        esperanza = iniciar_simulacion(maquinas_funcionando, maquinas_repuesto)
        acum_esperanza += esperanza

        lista_esperanza.append(esperanza)
    return acum_esperanza/numero_simulaciones, lista_esperanza


print "----------------------------------------------------------------"
print "------------------- Preparando la simulacion! ------------------"
print "----------------------------------------------------------------"
print "Parametros: "
print "----------------------------------------------------------------"
print "(a) maquinas_funcionando %d" % (maquinas_funcionando)
print "(b) maquinas_repuesto	%d" % (maquinas_repuesto)

print "----------------------------------------------------------------"
print "------------------- Iniciando la simulacion! -------------------"
print "----------------------------------------------------------------"
print ""

print "----------------------------------------------------------------"
print "---------------- Se ha terminado la simulacion! ----------------"
print "----------------------------------------------------------------"
print "Analisis de resultados: "
print "----------------------------------------------------------------"
result = problema(esperanza, numero_simulaciones, maquinas_funcionando, maquinas_repuesto)
print "(a) Tiempo de falla esperado del sistema: %0.2f horas" % round(result[0],2)
print ""
print "----------------------------------------------------------------"
print "Intervalo de Confianza: "
print "----------------------------------------------------------------"

# Se calcula la media para 
promedio_total = result[0]
lista_esperanza = result[1]
# Se calcula el margen de error
m_error_95 = error_95_prcnt(lista_esperanza, promedio_total)
print "El intervalo de confianza de 95 por ciento esta entre (%f , %f)" % (promedio_total-m_error_95,promedio_total+m_error_95)
print ""

