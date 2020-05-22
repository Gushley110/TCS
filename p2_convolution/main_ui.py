# -*- coding:utf-8 -*-
# UI
import tkinter as tk
#from PIL import Image, ImageTk
# Dependencias
import numpy
import matplotlib.pyplot as plt
import sys
#Funciones propias
from finita import convolucion_finita
from periodica import convolucion_periodica
from circular import convolucion_circular
# Datos de prueba convolucion finita
# signal_h = "2,10,11,-5,4,3,7"
# origin_signal_h = 3
# signal_g = "3,0,-1,.5"
# origin_signal_g= 4
# Datos de prueba convolucion periodica
# signal_h = "2,3,2,3,2,3"
# origin_signal_h = 2
# signal_g = "-5,7,4,0,1"
# origin_signal_g= 4
# Datos de prueba convolucion circular
# signal_h = "-1,4,-1,4"
# origin_signal_h = 1
# signal_g = "3,6,2,3,6,2"
# origin_signal_g= 1

def realizar_convolucion_finita():
	print("Debug")
	print("h(x): %s\ng(x): %s" % (signal_h.get(), signal_g.get()))
	print("Origen h(x): %s & origen g(x): %s" % (origin_signal_h.get(), origin_signal_g.get()))
	convolucion_finita(signal_h.get(),origin_signal_h.get(),signal_g.get(),origin_signal_g.get())

def realizar_convolucion_periodica():
	print("Debug")
	print("h(x): %s\ng(x): %s" % (signal_h.get(), signal_g.get()))
	print("Origen h(x): %s & origen g(x): %s" % (origin_signal_h.get(), origin_signal_g.get()))
	convolucion_periodica(signal_h.get(),origin_signal_h.get(),signal_g.get(),origin_signal_g.get())

def realizar_convolucion_circular():
	print("Debug")
	print("h(x): %s\ng(x): %s" % (signal_h.get(), signal_g.get()))
	print("Origen h(x): %s & origen g(x): %s" % (origin_signal_h.get(), origin_signal_g.get()))
	convolucion_circular(signal_h.get(),origin_signal_h.get(),signal_g.get(),origin_signal_g.get())

if __name__== "__main__":
	frame = tk.Tk()

	#load = Image.open("assets/logoIPN.png")
	#render = ImageTk.PhotoImage(load)
	#img = tk.Label(frame, image=render)
	#img.image = render
	#img.place(x=0, y=0)

	frame.title("Práctica convolución discreta")
	tk.Label(frame, text="Convolución discreta", font=("Helvetica", 16)).grid(row=0,
											column=1)


	tk.Label(frame,text="Ingresa la señal h(x):").grid(row=1)
	tk.Label(frame,text="Ingresa la posición de origen de h(x):").grid(row=2)
	tk.Label(frame,text="Ingresa la señal g(x):").grid(row=3)
	tk.Label(frame,text="Ingresa la posición de origen de g(x):").grid(row=4)

	signal_h = tk.Entry(frame)
	origin_signal_h = tk.Entry(frame)
	signal_g = tk.Entry(frame)
	origin_signal_g = tk.Entry(frame)

	signal_h.grid(row=1, column=1)
	origin_signal_h.grid(row=2, column=1)
	signal_g.grid(row=3, column=1)
	origin_signal_g.grid(row=4, column=1)

	tk.Button(frame,
			text='Convolución finita',
			command=realizar_convolucion_finita).grid(row=1,
											column=2,
											sticky=tk.W,
											pady=4)

	tk.Button(frame,
			text='Convolución periódica',
			command=realizar_convolucion_periodica).grid(row=2,
											column=2,
											sticky=tk.W,
											pady=4)
	tk.Button(frame,
			text='Convolución circular',
			command=realizar_convolucion_circular).grid(row=3,
											column=2,
											sticky=tk.W,
											pady=4)
	tk.Button(frame,
			text='Salir',
			command=frame.quit).grid(row=4,
									column=2,
									sticky=tk.W,
									pady=4)
	tk.mainloop()
