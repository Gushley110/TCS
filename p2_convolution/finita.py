# -*- coding:utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import sys
from graficar import graficar

def convolucion_finita(sh,osh,sg,osg):
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
					temp_fraccion = muestras_signal_h[fil].split("/")
					print("Temporal 1")
					print(temp_fraccion)
					if len(temp_fraccion) == 2:
						matriz_a[fil,col] = float(temp_fraccion[0])/float(temp_fraccion[1])
					else:
						matriz_a[fil,col] = float(muestras_signal_h[fil])
				elif fil > tam_muestras_h and col == 0:
					matriz_a[fil,col] = 0
				elif col > 0 and fil == 0:

					matriz_a[fil,col] = float(matriz_a[tam_matriz-1,col-1])
				elif col > 0 and fil > 0:
					matriz_a[fil,col] = matriz_a[fil-1 ,col-1]
		for col in range(0,1):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_g and col == 0:
					temp_fraccion = muestras_signal_g[fil].split("/")
					print("Temporal 2")
					print(temp_fraccion)
					if len(temp_fraccion) == 2:
						matriz_b[fil,col] = float(temp_fraccion[0])/float(temp_fraccion[1])
					else:
						matriz_b[fil,col] = muestras_signal_g[fil]
				elif fil > tam_muestras_g and col == 0:
					matriz_b[fil,col] = 0
		# multiplicacion de matrices
		for r in range(0,tam_matriz):
			for c in range(0,1):
				for k in range(0,tam_matriz):
					matriz_r[r,c] += float(matriz_a[r,k]) *  float(matriz_b[k,c])
		print("h(x)*g(x)= ")
		# print(array_res)
	else:
		print("Se realizara la convolución de g(x)*h(x)")
		for col in range(0,tam_matriz):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_g and col == 0:
					temp_fraccion = muestras_signal_g[fil].split("/")
					print("Temporal 1")
					print(temp_fraccion)
					if len(temp_fraccion) == 2:
						matriz_a[fil,col] = float(temp_fraccion[0])/float(temp_fraccion[1])
					else:
						matriz_a[fil,col] = float(muestras_signal_g[fil])
				elif fil > tam_muestras_g and col == 0:
					matriz_a[fil,col] = 0
				elif col > 0 and fil == 0:
					matriz_a[fil,col] = float(matriz_a[tam_matriz-1,col-1])
				elif col > 0 and fil > 0:
					matriz_a[fil,col] = float(matriz_a[fil-1 ,col-1])
		for col in range(0,1):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_h and col == 0:
					temp_fraccion = muestras_signal_h[fil].split("/")
					print("Temporal 1")
					print(temp_fraccion)
					if len(temp_fraccion) == 2:
						matriz_b[fil,col] = float(temp_fraccion[0])/float(temp_fraccion[1])
					else:
						matriz_b[fil,col] = float(muestras_signal_h[fil])
				elif fil > tam_muestras_h and col == 0:
					matriz_b[fil,col] = 0
		# multiplicacion de matrices
		for r in range(0,tam_matriz):
			for c in range(0,1):
				for k in range(0,tam_matriz):
					matriz_r[r,c] += float(matriz_a[r,k]) *  float(matriz_b[k,c])
		print("g(x)*h(x)= ")

	print(matriz_r)
	print("Con origen en la posición: "+str(position_origin_final) + "con dato: " + str(matriz_r[position_origin_final-1,0]))

	graficar(matriz_r, position_origin_final, muestras_signal_h, origin_signal_h, muestras_signal_g, origin_signal_g, tipo=0)
