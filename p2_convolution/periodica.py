import numpy
import matplotlib.pyplot as plt
import sys

from graficar import graficar

def convolucion_periodica(sh,osh,sg,osg):
	signal_h = sh
	signal_g = sg
	origin_signal_h = int(osh)
	origin_signal_g= int(osg)
	muestras_signal_h = signal_h.split(",")
	muestras_signal_g = signal_g.split(",")

	print(muestras_signal_h)
	print(muestras_signal_g)

	# Tamaño de las muestras
	tam_muestras_h = len(muestras_signal_h)
	tam_muestras_g = len(muestras_signal_g)
	# El tamaño de la matriz A que debemos formar con cualquiera de las muestras es cuadrada, su tamaño n*n, donde n= la suma del tamaño de las dos muestras -1
	tam_matriz = (tam_muestras_h + tam_muestras_g)-1

	matriz_a = numpy.zeros((tam_matriz,tam_matriz))
	matriz_b = numpy.zeros((tam_matriz,1))
	matriz_r = numpy.zeros((tam_matriz,1))
	# La posicion del origen  que tendra la matriz resultante sera
	# la suma de las posiciones antes de la posicion de origen de ambas muestras + 1
	position_origin_final = 1
	for i in range(0, tam_muestras_h):
		if i < origin_signal_h-1:
			position_origin_final += 1
	for i in range(0, tam_muestras_g):
		if i < origin_signal_g-1:
			position_origin_final += 1
	# Llenado de matrices
	if tam_muestras_h >= tam_muestras_g:
		print("Se realizara la convolución de h(x)*g(x)")
		for col in range(0,tam_matriz):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_h and col == 0:
					matriz_a[fil,col] = muestras_signal_h[fil]
				elif fil > tam_muestras_h and col == 0:
					matriz_a[fil,col] = 0
				elif col > 0 and fil == 0:
					matriz_a[fil,col] = matriz_a[tam_matriz-1,col-1]
				elif col > 0 and fil > 0:
					matriz_a[fil,col] = matriz_a[fil-1 ,col-1]
		for col in range(0,1):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_g and col == 0:
					matriz_b[fil,col] = muestras_signal_g[fil]
				elif fil > tam_muestras_g and col == 0:
					matriz_b[fil,col] = 0
		array_res = []
		# multiplicacion de matrices
		for r in range(0,tam_matriz):									#elementos en la matriz prefinal
			for c in range(0,1):										#filas, de un elemento cada una
				for k in range(0,tam_matriz):							#elementos en la matriz prefinal
					matriz_r[r,c] += matriz_a[r,k] *  matriz_b[k,c]
					array_res.append(matriz_a[r,k] *  matriz_b[k,c])
		print("h(x)*g(x)= ")
		#print(array_res)
	else:
		print("Se realizara la convolución de g(x)*h(x)")
		for col in range(0,tam_matriz):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_g and col == 0:
					matriz_a[fil,col] = muestras_signal_g[fil]
				elif fil > tam_muestras_g and col == 0:
					matriz_a[fil,col] = 0
				elif col > 0 and fil == 0:
					matriz_a[fil,col] = matriz_a[tam_matriz-1,col-1]
				elif col > 0 and fil > 0:
					matriz_a[fil,col] = matriz_a[fil-1 ,col-1]
		for col in range(0,1):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_h and col == 0:
					matriz_b[fil,col] = muestras_signal_h[fil]
				elif fil > tam_muestras_h and col == 0:
					matriz_b[fil,col] = 0
		array_res = []
		# multiplicacion de matrices
		for r in range(0,tam_matriz):								
			for c in range(0,1):									
				for k in range(0,tam_matriz):
					matriz_r[r,c] += matriz_b[r,k] *  matriz_a[k,c]
		print("g(x)*h(x)= ")
	print(matriz_r)
	print("l="+str(len(matriz_r)))

	#Matriz de periodicidad

	tam_matrizrF1 = len(matriz_r) 	#cantidad de elementos en el periodo
	while tam_matrizrF1%tam_muestras_g != 0:	#revisa que el tamaño del perdiodo entre en partes iguales 
		tam_matrizrF1+=1

	matriz_rF1 = numpy.zeros((tam_matrizrF1,1))	
	for r in range(0, len(matriz_r)):	#agrega ceros de ser necesario para la separacion de tam_muestras_g
				for c in range(0, 1):
					matriz_rF1[r, c] = matriz_r[r, c]

	array_rF = []
	for r in range(0, len(matriz_rF1)):	
				for c in range(0, 1):
					array_rF.append(matriz_rF1[r,c])
	print("arrayceros")
	print(array_rF)

	divs = int(tam_matrizrF1/tam_muestras_g)
	print("divs="+str(divs))
	matriz_rF = numpy.zeros((divs,1))
	array_F = []
	cont = 0
	while int(len(muestras_signal_g)) >= (cont):	#operaciones
		aux = 0
		for r in range(cont,len(array_rF),tam_muestras_g):
			print(r)
			aux += array_rF[r]
		array_F.append(aux)
		cont +=1
	print("array")
	print(array_F)

	matriz_F = numpy.zeros((int(len(muestras_signal_g)),1))	#solo toma los valores necesarios 
	for r in range(0, len(matriz_F)):	
				for c in range(0, 1):
					matriz_F[r, c] = array_F[r]
	print("secuencia resultante")				
	print(matriz_F)
	origen = position_origin_final
	while  origen > len(matriz_F):
		origen -=len(matriz_F)

	#print("Con origen en la posición: "+str(origen))
	print("Con origen en la posición: "+str(origen) + " con dato: " + str(matriz_F[origen-1,0]))

	graficar(matriz_F, origen, muestras_signal_h, origin_signal_h, muestras_signal_g, origin_signal_g, 1)

# 3,5,-1,.5,4,0,11
# 2
# -1,0,2,5
# 4
