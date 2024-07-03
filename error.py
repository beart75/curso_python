# Crear un error para un objeto que se ha agotado en un ecommerce
almacen = {
    "Lechuga": 10
 }

class ObjetoAgotado(Exception):
    pass

class Carrito:
    def __init__(self):
        self.items = []

    def comprar(self, item: str):
        cantidad = almacen[item]
        if cantidad < 1:
            raise ObjetoAgotado ("no hay")
        self.items.append(item)

carro = Carrito()
carro.comprar("Lechuga")
print(carro.items)