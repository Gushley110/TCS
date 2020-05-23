import numpy
import matplotlib.pyplot as plt

def graficar(matriz_r, origen, h, origenH, g, origenG, tipo=0):

	if(tipo == 2):
		tamanio = len(matriz_r)
	else:
		tamanio = matriz_r.shape[0]

	hLin = numpy.zeros(len(h))
	gLin = numpy.zeros(len(g))
	for i in range(len(h)):
		hLin[i] += float(h[i])

	for i in range(len(g)):
		gLin[i] += float(g[i])

	inicio = -1*origen+1
	final = inicio + tamanio - 1

	if(tipo == 1 or tipo == 2):
		print("Tipo != 0")
		if(tipo == 2):
			print("Tipo 2")

			tamanio = len(matriz_r)
			convolucion = matriz_r
			final = len(matriz_r) - 1

			k = 0
			convolucion = numpy.zeros(3*tamanio)
			print("Tamanio, ",len(convolucion))
			for i in range(3):
				for j in range(tamanio):
					convolucion[k] += matriz_r[j]
					k+=1

			x = numpy.linspace(0-origen+1, 3*tamanio-origen, 3*tamanio, endpoint=True)
			print("----------------------------------------")
			print("De ",0-origen+1," a ", 3*tamanio-origen-1)

		else:
			print("Tipo 1")
			k = 0
			convolucion = numpy.zeros(3*tamanio)
			print("Tamanio, ",len(convolucion))
			for i in range(3):
				for j in range(tamanio):
					convolucion[k] += matriz_r[j][0]
					k+=1
			x = numpy.linspace(0-origen+1, 3*tamanio-origen, 3*tamanio, endpoint=True)
			print("De ",0," a ", tamanio*3)
			print("------------------")
			print("Valores: ", convolucion, " Origen: ", origen)
			print("------------------")

	else:
		convolucion = numpy.zeros(tamanio)
		x = numpy.linspace(inicio, final, tamanio, endpoint=True)
		for i in range(tamanio):
			convolucion[i] += matriz_r[i][0]

		print("Tipo: ",type(convolucion))



	#if tipo < 0:
	#	tamanio = matriz_r.shape[0]
	#	convolucion = numpy.zeros(tamanio)
	#	for i in range(tamanio):
	#		convolucion[i] += matriz_r[i][0]
	#else:
	#	tamanio = len(matriz_r)
	#	convolucion = matriz_r

	#print(convolucion)
	#inicio = -1*origen+1
	#if tipo < 0:
	#	final = inicio + matriz_r.shape[0] - 1
	#else:
	#	final = len(matriz_r) - 1
	#print("Inicio: ",inicio, " Final: ",final)


	print(hLin)
	inicioH = -1*origenH+1
	finalH = inicioH + len(h) - 1
	print("Inicio: ",inicioH, " Final: ",finalH)

	print(gLin)
	inicioG = -1*origenG+1
	finalG = inicioG + len(g) - 1
	print("Inicio: ",inicioG, " Final: ",finalG)

	hX = numpy.linspace(inicioH, finalH, len(h), endpoint=True)
	gX = numpy.linspace(inicioG, finalG, len(g), endpoint=True)

	fig, (senialesOriginales, convoGrafica) = plt.subplots(2)

	senialesOriginales.grid(True)
	convoGrafica.grid(True)

	if(tipo==0):
		convoGrafica.set_title("Convolución finita")
	elif(tipo==1):
		convoGrafica.set_title("Convolución periódica")
	else:
		convoGrafica.set_title("Convolución circular")

	senialesOriginales.stem(hX, hLin, 'r', markerfmt='ro')
	senialesOriginales.stem(gX, gLin, 'b', markerfmt='bo')
	senialesOriginales.set_title('Funciones originales')
	convoGrafica.stem(x, convolucion, 'g', markerfmt='go')

	for i,j in zip(x, convolucion):
		convoGrafica.annotate(str(j), xy=(i,j))


	plt.show()
