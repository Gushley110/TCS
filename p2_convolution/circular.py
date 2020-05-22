# -*- coding:utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import sys

from graficar import graficar

def convolucion_circular(sh,osh,sg,osg):
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

	# Asigna el periodo de acuerdo a la longitud de las en tradas
	periodo_h = tam_muestras_h
	periodo_g = tam_muestras_g

	# La posicion del origen  que tendra la matriz resultante sera
	# la suma de las posiciones antes de la posicion de origen de ambas muestras + 1
	position_origin_final = 1
	for i in range(0, tam_muestras_h):
		if i < origin_signal_h-1:
			position_origin_final += 1
	for i in range(0, tam_muestras_g):
		if i < origin_signal_g-1:
			position_origin_final += 1

	# variables para la operacion 2
	op_a = []
	op_b = []
	op_r = []

	# vaiables operacion de multiplicación
	op_multi = [] #este tiene dentro arreglos
	op_res = []
	if periodo_h >= periodo_g:
		print("Se realizara la convolución de h(x)*g(x)")
		# crea el arreglo para la operacion de multiplicacion
		for i in range(0,tam_muestras_g):
			op_multi.append([])
		for i in range(0,tam_muestras_g):
			# Agrega 0's a la izquierda del arreglo para las sumas
			if i > 0:
				for j in range(0,i):
					op_multi[i].append(0.0)
			for j in range(0,tam_muestras_h):
				op_multi[i].append(float(muestras_signal_h[j])*float(muestras_signal_g[i]))
			# Agrega 0's a la derecha del arreglo para las sumas
			for j in range(0,periodo_g-(i+1)):
				op_multi[i].append(0.0)
		print(op_multi)
		# Crear el arreglo de la operacion resultante y  Realiza las sumas del arreglo de multiplicaciones
		for i in range(0,(tam_muestras_g+tam_muestras_h)-1):
			op_res.append(0.0)
		print(op_res)
		for i in range(0,len(op_res)):
			for j in range(0,len(op_multi)):
				op_res[i] = op_res[i] + op_multi[j][i]
		print("h(x)*g(x)= ")
		print(op_res)
		#Despues parte el arreglo tomando el numero del periodo mas grande y agregandole tantos 0's como sea necesario al que quedo mas pequeño
		for i in range(0,len(op_res)):
			if i<periodo_h:
				op_a.append(op_res[i])
			else:
				op_b.append(op_res[i])
		for i in range(0,len(op_a)-len(op_b)):
			op_b.append(0.0)
		# Realiza la suma
		print(op_a)
		print(op_b)
		for i in range(0,periodo_h):
			op_r.append(op_a[i] + op_b[i])
		print(op_r)
		print("h(x)*g(x)= ")
	else:
		print("Se realizara la convolución de g(x)*h(x)")
		# crea el arreglo para la operacion de multiplicacion
		for i in range(0,tam_muestras_h):
			op_multi.append([])
		for i in range(0,tam_muestras_h):
			# Agrega 0's a la izquierda del arreglo para las sumas
			if i > 0:
				for j in range(0,i):
					op_multi[i].append(0.0)
			for j in range(0,tam_muestras_g):
				op_multi[i].append(float(muestras_signal_g[j])*float(muestras_signal_h[i]))
			# Agrega 0's a la derecha del arreglo para las sumas
			for j in range(0,periodo_h-(i+1)):
				op_multi[i].append(0.0)
		print(op_multi)
		# Crear el arreglo de la operacion resultante y  Realiza las sumas del arreglo de multiplicaciones
		for i in range(0,(tam_muestras_g+tam_muestras_h)-1):
			op_res.append(0.0)
		print(op_res)
		for i in range(0,len(op_res)):
			for j in range(0,len(op_multi)):
				op_res[i] = op_res[i] + op_multi[j][i]
		print("g(x)*h(x)= ")
		print(op_res)
		#Despues parte el arreglo tomando el numero del periodo mas grande y agregandole tantos 0's como sea necesario al que quedo mas pequeño
		for i in range(0,len(op_res)):
			if i<periodo_g:
				op_a.append(op_res[i])
			else:
				op_b.append(op_res[i])
		for i in range(0,len(op_a)-len(op_b)):
			op_b.append(0.0)
		# Realiza la suma
		print(op_a)
		print(op_b)
		for i in range(0,periodo_g):
			op_r.append(op_a[i] + op_b[i])
		print(op_r)
		print("g(x)*h(x)= ")

	graficar(op_r, position_origin_final, muestras_signal_h, origin_signal_h, muestras_signal_g, origin_signal_g, tipo=2)
