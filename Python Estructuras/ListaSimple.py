import NodoLista
Nodo = NodoLista
import subprocess
class ListaSimple():
	
	def __init__(self):
		self.__Primero = None
		self.__Ultimo = None

	def getVacio(self):
		if self.__Primero == None:
			return True

	def setNodoAlInicio(self,Informacion):
		Nuevo = Nodo.NodoLista(Informacion)
		if self.getVacio() == True:
			self.__Primero = self.__Ultimo = Nuevo
		else:
			Nuevo.PSiguiente = self.__Primero
			self.__Primero = Nuevo

	def setNodoAlFinal(self, Informacion):
		Nuevo = Nodo.NodoLista(Informacion)
		if self.getVacio() == True:
			self.__Primero = self.__Ultimo = Nuevo
		else:
			self.__Ultimo.PSiguiente = Nuevo
			self.__Ultimo = Nuevo

	def EliminarPrimero(self):
		if self.getVacio()==True:
			print ("Lista Vacia")
		elif self.__Primero == self.__Ultimo:
			self.__Primero = None
			self.__Ultimo = None
			print("Elemento Eliminado")
		else:
			Temporal = self.__Primero
			self.__Primero = self.__Primero.PSiguiente
			Temporal = None	
			print ("Elemento Eliminado")

	def EliminarNodo(self,PosicionDato):
		Temp=self.__Primero
		Posicion=0;
		while Posicion!=PosicionDato-1:
			Temp=Temp.PSiguiente
			Posicion +=1

		Temp.setSiguiente(Temp.getSiguiente().getSiguiente())


	def EliminarUltimo (self):
		if self.getVacio()== True:
			print ("Lista Vacia")
		elif self.__Primero == self.__Ultimo:
			self.__Primero = None
			self.__Ultimo = None
			print("Elemento Eliminado")
		else:
			Validar = True
			Temporal = self.__Primero
			while(Validar):
				if Temporal.PSiguiente == self.__Ultimo:
					Temporal2 = self.__Ultimo
					self.__Ultimo = Temporal
					Temporal2 = None	
					Validar = False
					print ("Elemento Eliminado")
				else:
					Temporal= Temporal.PSiguiente

	def  getNodoPrimero(self):
		if self.getVacio()==True:
			return("Lista Vacia")

		else:
			return	self.__Primero

	def  getNodoUltimo(self):
		if self.getVacio()==True:
			return("Lista Vacia")

		else:
			return	self.__Ultimo

          
	def ImprimirLista(self):
		if self.getVacio()==True:
			print ("Lista Vacia")
		else:
			Validar= True
			Temporal = self.__Primero
			while(Validar):
				print	(Temporal.getDato())
				if Temporal == self.__Ultimo:
					Validar= False
				else:
					Temporal = Temporal.PSiguiente

	def Grafico(self):
		Archivo = open("C:\Graficos EDD\ListaSimple.txt","w")
		Archivo.write("digraph Lista_Simple { rankkdir=LR \n")

		Temporal = self.__Primero
		while Temporal!=self.__Ultimo:
			if Temporal == self.__Primero:
				Archivo.write(str(Temporal.getDato()))
			else:
				Archivo.write("->" + str(Temporal.getDato()))
			Temporal = Temporal.PSiguiente
		#if Temporal == self.__Ultimo:

			#Archivo.write("->"+str(self.__Ultimo)+"}")				
		Archivo.write("}")
		#subprocess.Popen("dot -Tpng C:\Graficos EDD\ListaSimple.txt -o C:\Graficos EDD\ListaSimple.png")
	
	def Buscar(self, Dato):
		Temp = self.__Primero
		Posicion = 0
		if self.getVacio() == True:
			return str("Lista Vacia")
		else:
			while Temp !=self.__Ultimo:
				if Temp.getDato()==Dato:
					return "Dato se encuentra en el Indice "+str(Posicion)
					
				
				Temp = Temp.PSiguiente
				Posicion = Posicion +1
			if Temp.getDato()==Dato:
				return "Dato se encuentra en el Indice "+str(Posicion)
				

			return "No se encontro el Dato" 

