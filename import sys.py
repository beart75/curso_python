#datos de la version del archivo python, 
# # Librería estandar: sys - Es un módulo que permite manejar el interprete y extraer información de este.

import sys
data = sys.argv[1:]
usuario, contraseña = data
with open("contraseña.txt", "w") as archivo:
    archivo.write(f"Usuario:    {usuario}\n")
    archivo.write(f"contraseña:    {contraseña}\n")
    print("se ha guardado todo")