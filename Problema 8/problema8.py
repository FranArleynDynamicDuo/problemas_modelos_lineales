# Problema *
from problema8_aleatorio import *

vendedor = 5
nro_autos = 0
comision = [0] * 5

print "\n"
for i in range(vendedor):
	nro_autos = random_autos_vendidos()

	print "EL vendedor %d vendio %d carros: " % (i,nro_autos)
	for j in range(nro_autos):
		tipo_auto = random_tipo_autos()
		
		if tipo_auto == "Compacto":
			comision[i] = comision[i] + 250

		elif tipo_auto == "Mediano":
			comision_mediano = random_tipo_autos_mediano()
			comision[i] = comision[i] + comision_mediano

		elif tipo_auto == "Lujo":
			comision_lujo = random_tipo_autos_lujo()
			comision[i] = comision[i] + comision_lujo

	print "  Por una comision total de %d" % (comision[i])

print "\n"
comision = sum(comision) / len(comision)
print "La comision promedio de un vendedor es de : %d" % (comision)
print "\n"