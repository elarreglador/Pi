#!/usr/bin/python3.8

# Calcular el valor de Pi utilizando las series de Gregory-Leibniz
#
# Pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + ...

from datetime import datetime

aproximacion = 0
divisor = 1
i = 1

while True:
	aproximacion = aproximacion + (4/divisor) - (4/(divisor+2))
	if i % 100000000 == 0 or i == 1:
		print ( str(datetime.now()) )
		print ("Valor de Pi " + str(i) + " ** 3.14159265358979323 **")
		print ("aproximacion " + str(i) + " : " + str(aproximacion) )
		print ("*****************************************")
	divisor = divisor + 4
	i = i + 1
