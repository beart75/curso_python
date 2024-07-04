# Crear una baraja y barajarla
import random

class Carta:
    def __init__(self, valor, figura):
        self.valor = valor
        self.figura = figura

    def __str__(self):
        return f"{self.valor} de {self.figura}"

class Baraja:
    figuras = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']

    def __init__(self):
        self.cartas = [Carta(valor, figura) for figura in self.figuras for valor in self.valores]

    def barajar(self):
        random.shuffle(self.cartas)

    def mostrar(self):
        for carta in self.cartas:
            print(carta)

# Baraja original
baraja = Baraja()
print("Baraja original:\n")
baraja.mostrar()

print("\n\n")

# Barajada
baraja.barajar()
print("\nBaraja barajado:")
baraja.mostrar()