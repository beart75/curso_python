#GESTION BASEDATOS


#Base de datos de usuario y contraseña

#Validador de contraseña
"""

SIN ACABAR

"""

class Usuario:
    activado = True
    def __init__(self, nombre, contraseña): #atributo de clase
        selt.nombre =  nombre
        selt.activado = True
        selt.contraseña = contraseña

    def activarUsuario(self):
        print(f"¡{self.nombre} ha sido activado!")

ArchivoPw ="contraseña.txt"

def guardaContraseña(pw):
    archivo = open(ArchivoPw, "w")  # Modo de escritura
    archivo.write(pw)
    archivo.close() 

def leeContraseña():
    archivo = open(ArchivoPw, "r")  # Modo de read
    linea = archivo.readline()
    archivo.close() 
    return linea

def ValidaPW(pw):
    estado = True
    isMayus = False
    isMinus = False
    isSpecial = False 
    cadena ="!·$%&/()=?¿^*¨:;,@#\/+-'?¿[]{}" # CREAR UN DICCIONARIO ??
    isNumber = False
    if len(pw) < 12:
        estado = False
        print("contraseña de menos de 12 caracteres")
    else:
        for caracter in pw:
            if caracter.isdigit():
                isNumber = True
            else:
                isNumber = False
                print("Sin numero")
        for caracter in pw:
            if caracter.isupper():
                isMayus = True
            else:
                isMayus = False
        print(f"{caracter} is  {isMayus}.")     
        for caracter in pw:
            if caracter.islower():
                isMinus = True
            else:
                isMinus = False
                print("Sin minuscula")
        print(f"{caracter} is  {isMinus}.")
        for caracter in pw:
            for letra in cadena:
                if pw.find(letra) > 0:
                    isSpecial = True
                    print("Tiene caracter especial.")
        if isMayus == True and isMinus == True and isSpecial == True and isNumber == True:
            estado = True
        else:
            estado = False
    return estado        
 

def CreaUsuario():
    usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña ")
    if ValidaPW(contraseña):
        guardaContraseña(contraseña)


instancia = Usuario("Beart", "123ABC")

print("CONTRASEÑA INTRODUCIDA")
ln = leeContraseña() # si es la misma que la guardada , puedes pasar
print(f"Tu contraseña es {ln}")

