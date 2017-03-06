class NodoMatrizDispersa():

	def __init__(self,Informacion,Dominio):
		self.Informacion = Informacion
		self.Dominio = Dominio
		self.Siguiente = None
		self.Anterior = None		
#-----------Apuntadores-------------------------
		self.Derecha= None
		self.Izquierda = None	
		self.Arriba = None
		self.Abajo = None
#-----------Apuntadores profundida -------------
		
		self.ProfundidadSiguiente = None
		self.ProfundidadAnterior  = None

#-----------Metodos setting and getting---------

	def getInformacion(self):
		return self.Informacion

	def setInformacion(self,Dato):
		self.Informacion = Dato

	def getDominio(self):
		return self.Dominio

	def setDominio(self,Dato):
		self.Dominio = Dato

	def getSiguiente(self):
		return self.Siguiente

	def setSiguiente(self,Dato):
		self.Siguiente = Dato

	def getAnterior(self):
		return self.Anterior

	def setAnterior(self,Dato):
		self.Dominio = Dato

	def getArriba(self):
		return self.Arriba

	def setArriba(self,Dato):
		self.Arriba = Dato

	def getAbajo(self):
		return self.Abajo

	def setAbajo(self,Dato):
		self.Abajo = Dato

	def getDerecha(self):
		return self.Derecha

	def setDerecha(self,Dato):
		self.Derecha = Dato

	def getIzquierda(self):
		return self.Izquierda

	def setIzquierda(self,Dato):
		self.Izquierda = Dato

	def getProfundidadSiguiente(self):
		return self.ProfundidadSiguiente

	def setProfundidadSiguiente(self,Dato):
		self.ProfundidadSiguiente = Dato

	def getProfundidadAnterior(self):
		return self.ProfundidadAnterior

	def setProfundidadAnterior(self,Dato):
		self.ProfundidadAnterior = Dato




