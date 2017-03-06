class NodoLista(object):
	def __init__(self,Informacion = None):
		self.__Dato=Informacion
		self.__PSiguiente = None

	def getSiguiente(self):
		return self.__PSiguiente

	def getDato(self):
		return self.__Dato

	def setSiguiente(self,nodo):
		self.__PSiguiente = nodo

