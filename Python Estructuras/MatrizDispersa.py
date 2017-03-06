from NodoMatrizDispersa import NodoMatrizDispersa
"""import Letra
import Dominio 
LD = Dominio
LLDominio = LD.Dominio()
LL = Letra
LLLetra = LL.Letra()"""

class MatrizDispersa():

	def __init__(self):
#-------- Apuntadores -----------------
		self.Primero = None
		self.Ultimo = None 
		self.AbajoI = None
		self.AbajoU = None
#---------Apuntadores Dominio----------
		self.InicioDom = None
		self.FinDom = None
#----------Apuntadores Letra-----------
		self.InicioLet = None
		self.FinLet =None

	def Split(self,Informacion):
		Temporal = Informacion.split("@")
		Nombre = Temporal[0]		
		Dominio = Temporal[1]	
		LetraInicial = Nombre[:1]
		self.MatrizDispersa(LetraInicial,Nombre,Dominio)

	def MatrizDispersa(self, Letra,Informacion,Dominio):
		LLetra = self.getExiste(Letra)
		LDominio = self.getExisteD(Dominio)

		if LLetra == False and LDominio == False:
			Nuevo = NodoMatrizDispersa(Informacion, Dominio)
			self.AddLetra(Letra)
			self.AddDominio(Dominio)
			TemporalLetra = self.BuscarLetra(Letra)
			TemporalLetra.Derecha = Nuevo
			Nuevo.Izquierda = TemporalLetra
			TemporalDominio = self.BuscarDominio(Dominio)
			TemporalDominio.Abajo = Nuevo
			Nuevo.Abajo = None
			Nuevo.Derecha = None

		if LLetra == False and LDominio == True:
			Nuevo= NodoMatrizDispersa(Informacion,Dominio)
			self.AddLetra(Letra)
			TemporalLetra = self.BuscarLetra(Letra)
			TemporalLetra.Derecha =Nuevo
			Nuevo.Izquierda = TemporalLetra
			Nuevo.Derecha = None	
			self.addEnDominio(Dominio,Nuevo)

		if LLetra == True and LDominio == False:
			Nuevo = NodoMatrizDispersa(Informacion,Dominio)
			self.AddDominio(Dominio)
			TemporalDominio = self.BuscarDominio(Dominio)
			TemporalDominio.Abajo = Nuevo
			Nuevo.Abajo = None
			Nuevo.Arriba = TemporalDominio
			self.AddEnLetra(Letra,Nuevo)

		if LLetra == True and LDominio == True:
			Nuevo = NodoMatrizDispersa(Informacion,Dominio)
			TemporalLetra = self.BuscarLetra(Letra)
			self.BusquedaDatosXLetra(TemporalLetra,Nuevo)

	def BusquedaDatosXLetra(self,NodoLetra,Nuevo):
		Letra = NodoLetra
		Letra = Letra.getDerecha()
		while Letra != None:
			if Letra.getDominio() == Nuevo.getDominio():
				self.IngresarEnProfundidad(Letra,Nuevo)
				break	
			Letra = Letra.getDerecha()
		if Letra == None:
			self.AddEnLetra(NodoLetra.getInformacion(),Nuevo)
			self.addEnDominio(Nuevo.getDominio(),Nuevo)

	def IngresarEnProfundidad(self,Letra,Nodo):
		Actual = Nodo
		TemporalCabecera = Letra
		TemporalCabecera1 = TemporalCabecera.getProfundidadSiguiente()

		if TemporalCabecera1 == None:
			TemporalCabecera.profsig = Actual
			Actual.ProfundidadAnterior = TemporalCabecera
			Actual.ProfundidadSiguiente= None
		else:
			Temp = TemporalCabecera1
			TemporalCabecera.ProfundidadSiguiente = Actual
			Actual.ProfundidadAnterior = TemporalCabecera
			Actual.ProfundidadSiguiente = Temp

	def getExisteD(self,Letra):
		Parametro = False
		Temporal = self.InicioDom
		while Temporal != None:
			if Temporal.getInformacion() == Letra:
				Parametro = True
				return Parametro
				break
			else:
				Temporal = Temporal.getSiguiente()

		return Parametro

	def getVacioDominio(self):
		return self.InicioDom ==None
	

	def AddDominio(self,Dominio):
		resp = self.getExiste(Dominio)

		if resp == False:
			if self.getVacioDominio():
				self.InicioDom = NodoMatrizDispersa(Dominio,"---")
				self.InicioDom.Siguiente = None
			else:
				Temporal = self.InicioDom

				while Temporal != None:

					if Temporal.getInformacion() >Dominio and Temporal.getSiguiente() == None:
						Temporal1 = Temporal
						Actual = NodoMatrizDispersa(Dominio,"---")
						self.InicioDom = Actual
						Actual.Siguiente = Temporal1
						Temporal1.Anterior = Actual
						Temporal1.Siguiente = None
						break
					elif Temporal.getInformacion() >Dominio and Temporal.Siguiente.getInformacion() > Dominio:
						Temporal1 = Temporal
						Actual = NodoMatrizDispersa(Dominio,"---")
						self.InicioDom = Actual
						Actual.Siguiente = Temporal1
						Temporal1.Anterior = Actual
						break
						
					elif Temporal.getInformacion() < Dominio and Temporal.getSiguiente() == None:
						Actual = NodoMatrizDispersa(Dominio,"---")
						Temporal.Siguiente = Actual
						Actual.Anterior = Temporal
						Actual.Siguiente = None
						break


					elif Temporal.getInformacion() < Dominio and Temporal.Siguiente.getInformacion()>Dominio:
						Temporal1 = Temporal 
						Temporal2 = Temporal.Siguiente
						Actual = NodoMatrizDispersa(Dominio,"---")
						Temporal1.Siguiente =Actual
						Actual.anterior = Temporal1
						Actual.Siguiente = Temporal2
						Temporal2.Anterior = Actual
						break
					else:
						Temporal = Temporal.getSiguiente()

	def DesplegarDominio(self):
		Temporal = self.InicioDom
		while Temporal != None:
			print(Temporal.getInformacion())
			Temporal = Temporal.getSiguiente()



	def BuscarDominio(self, Dominio):
		Parametro = NodoMatrizDispersa("No se Encontro el Dominio","")
		Temporal = self.InicioDom
		while Temporal != None:
			if Temporal.getInformacion() == Dominio:
				Parametro = Temporal
			
			Temporal = Temporal.getSiguiente()

			if Temporal == self.InicioDom:
				Temporal = None				
		return Parametro
	
	def DesplegarDatosD(self,Dominio):
		Temp = self.BuscarDominio(Dominio)
		Concatenado ="Listado de Produndidad de Dominio " + Dominio +":"
		print("La Listado del Dominio " + Dominio + " es:")
		Temp = Temp.getAbajo()
		while Temp != None:
			print(Temp.getInformacion())
			Concatenado=Concatenado + " " + Temp.getInformacion() + "--"
			Temporal = Temp
			Temporal = Temporal.getProfundidadSiguiente()
			while  Temporal != None:
				print(Temporal.getInformacion())				
				Concatenado=Concatenado + " " + Temporal.getInformacion() + "--"
				Temporal = Temporal.getProfundidadSiguiente()
			Temp = Temp.getAbajo()		
		return Concatenado

	def addEnDominio(self,Dominio,Dato):
		Temp = self.BuscarDominio(Dominio)
		Temporal = Temp.getAbajo()

		while Temporal != None:

					if Temporal.getInformacion() > Dato.getInformacion() and Temporal.getAbajo() == None:
						Temporal1 = Temporal
						Temp.Abajo = Dato
						Dato.Abajo = Temporal1
						Temporal1.Arriba = Dato
						Temporal1.Abajo = None
						break
					elif Temporal.getInformacion() >Dato.getInformacion() and Temporal.Abajo.getInformacion() > Dato.getInformacion():
						Temporal1 = Temporal
						Temp.Abajo = Dato
						Dato.Abajo = Temporal1
						Temporal1.Arriba = Dato
						break
						
					elif Temporal.getInformacion()< Dato.getInformacion() and Temporal.getAbajo() == None:
						Temporal.Abajo = Dato
						Dato.Arriba = Temporal
						Dato.Abajo = None
						break


					elif Temporal.getInformacion() < Dato.getInformacion() and Temporal.getAbajo().getInformacion()>Dato.getInformacion():
						Temporal1 = Temporal 
						Temporal2 = Temporal.getAbajo()
						Temporal1.Abajo = Dato
						Dato.Arriba = Temporal1
						Dato.Abajo = Temporal2
						break
					else:
						Temporal = Temporal.getAbajo()

	def getExiste(self,Letra):
		Parametro = False
		Temporal = self.InicioLet
		while Temporal != None:
			if Temporal.getInformacion() == Letra:
				Parametro = True
				return Parametro
				break
			else:
				Temporal = Temporal.getSiguiente()

		return Parametro

	def getVacioLetras(self):
		return self.InicioLet ==None

	def AddLetra(self,Letra):
		resp = self.getExiste(Letra)

		if resp == False:
			if self.getVacioLetras():
				self.InicioLet = NodoMatrizDispersa(Letra,"---")
				self.InicioLet.Siguiente = None
			else:
				Temporal = self.InicioLet

				while Temporal != None:

					if Temporal.getInformacion()  >Letra and Temporal.getSiguiente() == None:
						Temporal1 = Temporal
						Actual = NodoMatrizDispersa(Letra,"---")
						self.InicioLet = Actual
						Actual.Siguiente = Temporal1
						Temporal1.Anterior = Actual
						Temporal1.Siguiente = None
						break
					elif Temporal.getInformacion()  >Letra and Temporal.getSiguiente().getInformacion()  > Letra:
						Temporal1 = Temporal
						Actual = NodoMatrizDispersa(Letra,"---")
						self.InicioLet = Actual
						Actual.Siguiente = Temporal1
						Temporal1.Anterior = Actual
						break
						
					elif Temporal.getInformacion() < Letra and Temporal.getSiguiente() == None:
						Actual = NodoMatrizDispersa(Letra,"---")
						Temporal.Siguiente = Actual
						Actual.Anterior = Temporal
						Actual.Siguiente = None
						break


					elif Temporal.getInformacion() < Letra and Temporal.getSiguiente().getInformacion()>Letra:
						Temporal1 = Temporal 
						Temporal2 = Temporal.getSiguiente()
						Actual = NodoMatrizDispersa(Letra,"---")
						Temporal1.Siguiente =Actual
						Actual.Anterior = Temporal1
						Actual.Siguiente = Temporal2
						Temporal2.Anterior = Actual
						break
					else:
						Temporal = Temporal.getSiguiente()

	def DesplegarLetras(self):
		Temporal = self.InicioLet
		while Temporal != None:
			print(Temporal.getInformacion())
			Temporal = Temporal.getSiguiente()
	


	def BuscarLetra(self, letra):
		Parametro = NodoMatrizDispersa("No se encontro la letra","")
		Temporal = self.InicioLet
		while Temporal != None:
			if Temporal.getInformacion() == letra:
				Parametro = Temporal
			
			Temporal = Temporal.getSiguiente()

			if Temporal == self.InicioLet:
				Temporal = None				
		return Parametro


	def DesplegarDatosL(self,Letra):
		Parametro = self.BuscarLetra(Letra)
		print("La listado con letra "+ Letra +" es:")
		Concatenado ="Listado de Produndidad de  " + Letra +":"
		Parametro = Parametro.getDerecha()
		while Parametro != None:
			print(Parametro.getInformacion())
			Concatenado=Concatenado + " " + Parametro.getInformacion() + "--"
			Temporal = Parametro
			Temporal = Temporal.getProfundidadSiguiente()
			while  Temporal != None:
				print(Temporal.getInformacion())
				Concatenado=Concatenado + " " + Parametro.getInformacion() + "--"
				Temporal = Temporal.getProfundidadSiguiente()
					
			Parametro = Parametro.getDerecha()
		return Concatenado

	def AddEnLetra(self,Letra,ValorAux):
		Parametro = self.BuscarLetra(Letra)
		Temporal = Parametro.getDerecha()

		while Temporal != None:

					if Temporal.Dominio > ValorAux.Dominio and Temporal.getDerecha() == None:
						Temporal1 = Temporal
						Parametro.Derecha = ValorAux
						ValorAux.Derecha = Temporal1
						Temporal1.Izquierda = ValorAux
						Temporal1.Derecha = None
						break
					elif Temporal.Dominio >ValorAux.Dominio and Temporal.getDerecha().getInformacion() > ValorAux.getInformacion():
						Temporal1 = Temporal
						Parametro.Derecha = ValorAux
						ValorAux.Derecha = Temporal1
						Temporal1.Izquierda = ValorAux
						break
						
					elif Temporal.Dominio < ValorAux.Dominio and Temporal.getDerecha() == None:
						Temporal.Derecha = ValorAux
						ValorAux.Izquierda = Temporal
						ValorAux.Derecha = None
						break


					elif Temporal.Dominio < ValorAux.Dominio and Temporal.getDerecha().Dominio>ValorAux.Dominio:
						Temporal1 = Temporal 
						Temporal2 = Temporal.getDerecha()
						Temporal1.Derecha = ValorAux
						ValorAux.Izquierda = Temporal1
						ValorAux.Derecha = Temporal2
						Temporal2.Izquierda = ValorAux
						break
					else:
						Temporal = Temporal.getDerecha()
