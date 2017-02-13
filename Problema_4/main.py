from simulacion import iniciar_simulacion

print ""
print "********************************************************************************"
print "********************************** Problema 4 **********************************"
print "********************************************************************************"
print ""

def problema(esperanza,numero_simulaciones,maquinas_funcionando, maquinas_repuesto):

    for i in range(numero_simulaciones):
        esperanza += iniciar_simulacion(maquinas_funcionando, maquinas_repuesto)

    return esperanza/1000

maquinas_funcionando = 4
maquinas_repuesto	 = 3
numero_simulaciones = 1000
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

print ""
print "----------------------------------------------------------------"
print "---------------- Se ha terminado la simulacion! ----------------"
print "----------------------------------------------------------------"
print "Analisis de resultados: "
print "----------------------------------------------------------------"
print "(a) Tiempo de falla esperado del sistema: %0.2f horas" % problema(esperanza, numero_simulaciones, maquinas_funcionando, maquinas_repuesto)
