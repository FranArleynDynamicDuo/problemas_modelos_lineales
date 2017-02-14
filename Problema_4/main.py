from simulacion import iniciar_simulacion

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
    	for i in range(numero_simulaciones):
       		esperanza += iniciar_simulacion(maquinas_funcionando, maquinas_repuesto)

    return esperanza/numero_simulaciones

maquinas_funcionando = 4
maquinas_repuesto	 = 3
esperanza = 0

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
print "(a) Tiempo de falla esperado del sistema: %0.2f horas" % round(result,2)

