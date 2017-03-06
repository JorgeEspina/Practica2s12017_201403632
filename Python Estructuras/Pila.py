import subprocess
import NodoPila
NPila = NodoPila
class Pila():
	
# Ultimo que entra , Primero que sale.
	def  __init__ (self):
		self.Inicio = None
		self.Dato = None

	def Apilar(self,x):
		Nuevo = NPila.NodoPila(x)
		if self.Inicio == None:
			Nuevo.Siguiente=None
			self.Inicio = Nuevo
		else:
			Nuevo.Siguiente = self.Inicio
			self.Inicio = Nuevo

	def Desapilar(self):
		Temporal = self.Inicio.Dato
		self.Inicio=self.Inicio.Siguiente
		return Temporal
	

	def MostrarPila(self):
		Temporal = self.Inicio
		while Temporal != None:
			print(Temporal.Dato)
			Temporal = Temporal.Siguiente

	def Grafico(self):
		Archivo = open("C:\Graficos EDD\Pila.txt","w")
		Archivo.write("digraph Pila_EDD{ rankkdir=LR \n")
		Temporal = self.Inicio
		while Temporal!=None:
			if Temporal == self.Inicio:
				Archivo.write(str(Temporal.Dato))
			else:
				Archivo.write("->" + str(Temporal.Dato))
			Temporal = Temporal.Siguiente
		Archivo.write("}")
		



