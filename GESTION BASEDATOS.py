#GESTION BASEDATOS


#Base de datos de usuario y contraseña

#Validador de contraseña
"""



"""

class Usuario:
    activado = True
    def __init__(self, nombre, contraseña): #atributo de clase
        selt.nombre =  nombre
        selt.activado = True
        selt.contraseña = contraseña

    def activarUsuario(self):
        print(f"¡{self.nombre} ha sido activado!")



instancia = Usuario("Beart", "123ABC")


ArchivoPw ="contraseña.txt"

def creaContraseña():
    pw = input("Introduce tu contraseña: ")
    archivo = open(ArchivoPw, "w")  # Modo de escritura
    archivo.write(pw)
    archivo.close() 

def leeContraseña():
    archivo = open(ArchivoPw, "r")  # Modo de read
    linea = archivo.readline()
    archivo.close() 
    return linea
def CreaUsuario():
    usuario = input("Introduce tu nombre de usuario: ")

creaContraseña()
print("CONTRASEÑA INTRODUCIDA")
ln = leeContraseña()
print(f"Tu contraseña es {ln}")

