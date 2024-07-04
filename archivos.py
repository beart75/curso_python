"""
Clase 4: Archivos


"""
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

creaContraseña()
print("CONTRASEÑA INTRODUCIDA")
ln = leeContraseña()
print(f"Tu contraseña es {ln}")

