import subprocess
import NodoCola
NCola = NodoCola
class Cola():
	
	# Primero que entra ,Primero que sale
	def __init__(self):
		self.Inicio = None;
		self.Fin = None;
		self.Dato = None;

	def Encolar(self,x):
		Temp = NCola.NodoCola(x)
		if self.Inicio == None:
			self.Inicio = self.Fin =Temp
		
		else:			
			self.Fin.Siguiente = Temp
			Temp.Anterior=self.Fin
			self.Fin=Temp


	def ImprimirCola(self):
		Temporal = self.Inicio
		while Temporal!=None:
			print(Temporal.Dato)
			Temporal= Temporal.Siguiente


	def Desencolar(self):		
		Temporal = self.Inicio.Dato		
		self.Inicio=self.Inicio.Siguiente
		return Temporal

	def Grafico(self):
		Archivo = open("C:\Graficos EDD\Cola.txt","w")
		Archivo.write("digraph Cola_EDD{ rankkdir=LR \n")
		Temporal = self.Inicio
		while Temporal!=None:
			if Temporal == self.Inicio:
				Archivo.write(str(Temporal.Dato))
			else:
				Archivo.write("->" + str(Temporal.Dato))
			Temporal = Temporal.Siguiente
		#if Temporal == self.Fin:
		#		Archivo.write("->" + (Temporal.Dato) + "}" )
		Archivo.write("}")
		#subprocess.Popen("dot -Tjpeg  C:\Graficos EDD\Cola.txt -o C:\Graficos EDD\Cola.jpeg")
