import MatrizDispersa
#import Dominio
#import Letra
MD = MatrizDispersa
MATRIZ = MD.MatrizDispersa()
#LD = Dominio
#LDominio = LD.Dominio()
#LL = Letra
#LLetra = LL.Letra()


MATRIZ.MatrizDispersa("a","anabella","hotmail.com")
MATRIZ.MatrizDispersa("m","marco","gmail.com")
MATRIZ.MatrizDispersa("m","monica","gmail.com")
MATRIZ.MatrizDispersa("m","mono","gmail.com")

MATRIZ.MatrizDispersa("j","javier","outlook.com")

MATRIZ.MatrizDispersa("a","amy","yahoo.com")
MATRIZ.MatrizDispersa("j","jorge","yahoo.com")

MATRIZ.MatrizDispersa("m","morales","yahoo.com")
MATRIZ.MatrizDispersa("p","pedro","yahoo.com")
MATRIZ.MatrizDispersa("p","pablo","yahoo.com")

print("-----------Listado de Letras-----------")
MATRIZ.DesplegarLetras()
print("-----------Listado de Dominios-----------")
MATRIZ.DesplegarDominio()
print("------------Listado de Produndidad de Letras------------------")
MATRIZ.DesplegarDatosL("a")
MATRIZ.DesplegarDatosL("j")
MATRIZ.DesplegarDatosL("m")
MATRIZ.DesplegarDatosL("p")
print("------------Listado de Produndidad de Dominios------------------")
MATRIZ.DesplegarDatosD("gmail.com")
MATRIZ.DesplegarDatosD("outlook.com")
MATRIZ.DesplegarDatosD("yahoo.com")
MATRIZ.DesplegarDatosD("hotmail.com")