#oo clases

class Animal:
    vida = True
    hambre = True

    def __init__(selt, genero, raza): #atributo de clase
        selt.genero =  genero
        selt.hambre = True
        selt.raza = raza

    def ataque_basico(self):
        print(f"{self.nombre} ha atacado!")

instancia = Animal("M", "Perro")
print(f" {instancia.raza} - {instancia.hambre}")
instancia.hambre = False #atributo de instancia
print(f" {instancia.raza} - {instancia.hambre}")
instancia2 = Animal("M", "gato")
print(f" {instancia2.raza} - {instancia2.hambre}")

print(f" {instancia.raza} - {instancia.hambre}")
instancia.hambre = False #atributo de instancia
print(f" {instancia.raza} - {instancia.hambre}")
instancia2 = Animal("M", "gato")
print(f" {instancia2.raza} - {instancia2.hambre}")

