import random

personas = 20
cola = 0

serv1 = True
serv2 = True
serv3 = True
serv4 = True
cont_serv1 = 0
cont_serv2 = 0
cont_serv3 = 0
cont_serv4 = 0

for i in range(personas):

	print "VUELTA NUMERO %d" % (i)

	# Primero observamos si los servidores estan libre

	if serv1 == True:
		serv1 = False
		cont_serv1 = i
		if 0 < cola :
			cola = cola - 1
			print "	(Serv1) Estatus de la cola, servidor ocupado: %i" %(cola)

	elif serv2 == True:
		serv2 = False
		cont_serv2 = i
		if 0 < cola:
			cola = cola - 1
			print "	(Serv2) Estatus de la cola, servidor ocupado: %i" %(cola)

	elif serv3 == True:
		serv3 = False
		cont_serv3 = i
		if 0 < cola:
			cola = cola - 1
			print "	(Serv3) Estatus de la cola, servidor ocupado: %i" %(cola)

	elif serv4 == True:
		serv4 = False
		cont_serv4 = i
		if 0 < cola:
			cola = cola - 1
			print "	(Serv4) Estatus de la cola, servidor ocupado: %i" %(cola)

	else:
		# Manejamos la Cola
		print "En la cola inicial hay: %d" % (cola)
		if cola < 6:
			cola = cola + 1;
		else:
			resp = random.random()

			if 6 <= cola and cola <= 8:
				if  resp > 0.20 :
					cola = cola + 1

			elif 9 <= cola and cola <= 10:
				if  resp > 0.40:
					cola = cola + 1

			elif 11 <= cola and cola <= 14:
				if resp	> 0.60:
					cola = cola + 1

			elif 15 <= cola:
				if resp > 0.80:
					cola = cola + 1

			print "El porcentaje es: %f" % (resp)
	
	print "Estatus de la cola final hay: %d" % (cola)

	# Tiempo de los Servidores
	print "	Estado de los servidores Inicial (vuelta %d): " %(i)
	print "		Servidor 1:  %r, Con un tiempo de : %d" % (serv1,cont_serv1)
	print "		Servidor 2:  %r, Con un tiempo de : %d" % (serv2,cont_serv2)
	print "		Servidor 3:  %r, Con un tiempo de : %d" % (serv3,cont_serv3)
	print "		Servidor 4:  %r, Con un tiempo de : %d" % (serv4,cont_serv4)

	if (i - cont_serv1 == 4):
		serv1 = True
		print "ENTRE 1"
	elif (i - cont_serv2 == 4):
		serv2 = True
		print "ENTRE 2"
	elif (i - cont_serv3 == 4):
		serv3 = True
		print "ENTRE 3"
	elif (i - cont_serv2 == 4):
		serv4 = True
		print "ENTRE 4"
	
	print "	Estado de los servidores Final (vuelta %d): " %(i)
	print "		Servidor 1:  %r, Con un tiempo de : %d" % (serv1,cont_serv1)
	print "		Servidor 2:  %r, Con un tiempo de : %d" % (serv2,cont_serv2)
	print "		Servidor 3:  %r, Con un tiempo de : %d" % (serv3,cont_serv3)
	print "		Servidor 4:  %r, Con un tiempo de : %d" % (serv4,cont_serv4)
	print "\n"