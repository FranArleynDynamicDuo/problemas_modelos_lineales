#! /usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint, uniform
from collections import deque
from math import log, sqrt, fabs

def tiempo_de_falla():
	x = randint(1,100)*1.0/100.0
	if x == 1.0:
		x = 0.99	
	falla = - log(1-x)
	return round(falla,1)*10

def tiempo_de_reparacion():
	x = randint(1,100)*1.0/100.0
	if x == 1.0:
	    x = 0.99
	tiempo = - (log(1-x))/2
	return round(tiempo,1)*10