#ejercicio2 """ conectar a una base de datos"""


#Pedir numeros hasta que se meta 0, y dar una lista con la suma digital de todos esos numeros
"""
suma_numeros()

def suma_numeros():
    print("SUMA NUMEROS")
    numero =0
    valor =0
    while True:
        valor = int(input("Pon un numero: "))
        numero =+ valor
        break
    print(numero)
    return numero
"""

traduccion = {
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C"

}

test1 = "ATCG"
test2 = "TAT"
test3 = "CCC"
test4 = "ATAGATCATADDCARAACCA"



#Conversion de ADN a ARN (complementario)
def ADNtoARN(test):

    resultado = test.replace("A","T")
    print(resultado)
    return resultado


#w= ADNtoARN(test1)


def eleva_cuadrado(string: str) -> list[int]:
    numeros =[]
    for caracter in string:
        if caracter.isdigit():
            print(caracter)

#eleva_cuadrado("os8dfois5")

def validaIP(cadena):
    x = cadena.split(".")
    for i in x:
        if int(i)>255:
            print(cadena + " INCORRECTO cada valor debe ser menor 255")
            return False

#validaIP("256.250.1.1")
