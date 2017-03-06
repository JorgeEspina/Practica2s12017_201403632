__author__ = "JorgeEspina"


from flask import Flask, request, Response
# Importar todas las clases
import Pila
import Cola
import ListaSimple
import MatrizDispersa
app = Flask("[EDD]Practica2")

MD = MatrizDispersa
MATRIZ = MD.MatrizDispersa()


# Declaraciones de las clases
Pil = Pila
P = Pil.Pila()

Col = Cola
C = Col.Cola()

ListSimple = ListaSimple
LS = ListSimple.ListaSimple()

# Envio de informacion

# Pila
@app.route('/Pila/Ingresar',methods=['POST']) 
def Apila():
	Parametro = str(request.form['Datos'])
	temp = P.Apilar(Parametro)
	P.Grafico()
	return temp
	

@app.route('/Pila/Desapilar',methods=['POST']) 
def Desapila():
	#Parametro = str(request.form['Datos'])
	return str(P.Desapilar())
	P.Grafico()

# Cola
@app.route('/Cola/Encolar',methods=['POST']) 
def Encola():
	Parametro = str(request.form['Datos'])
	temp = C.Encolar(Parametro)
	C.Grafico()
	return temp

@app.route('/Cola/Desencolar',methods=['POST']) 
def Desecola():
	return str(C.Desencolar())
	C.Grafico()

# Lista Simple
@app.route('/ListaSimple/IngresarNodo',methods=['POST']) 
def IngresarNodoLS():
	Parametro = str(request.form['Datos'])
	LS.setNodoAlFinal(Parametro)
	LS.Grafico()

@app.route('/ListaSimple/Buscar',methods=['POST']) 
def BuscarLS():
	Parametro = str(request.form['Datos'])
	return LS.Buscar(Parametro)

@app.route('/ListaSimple/Eliminar',methods=['POST']) 
def EliminarLS():
	Parametro = str(request.form['Datos'])
	LS.Eliminar(Parametro)

@app.route('/ListaSimple/ImprimirNodoLS',methods=['POST']) 
def ImprimirLS():
	Parametro = str(request.form['Datos'])
	LS.ImprimirLista(Parametro)

# Matriz Dispersa
@app.route('/MatrizDispersa/Agregar',methods=['POST']) 
def Agregar():
	Parametro = str(request.form['Datos'])
	MATRIZ.Split(Parametro)

@app.route('/MatrizDispersa/BuscarLetra',methods=['POST']) 
def BuscarL():
	Parametro = str(request.form['Datos'])
	return str(MATRIZ.DesplegarDatosL(Parametro))

@app.route('/MatrizDispersa/BuscarDominio',methods=['POST']) 
def BuscarDominio():
	Parametro = str(request.form['Datos'])
	return str(MATRIZ.DesplegarDatosD(Parametro))


"""@app.route("/")
def EDD():
	return "[ESTRUCTURAS DE DATOS] Practica 2 !"
"""
if __name__ == "__main__":
  app.run(debug=True)