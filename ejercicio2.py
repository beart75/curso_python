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

"""ejercicio 1
#Conseguir una lista con los primos entre dos numeros (ejemplo, entre 4 y 12 ---> [5, 7, 11])
#Conseguir una sucesion de Fibonacci para un numero n de terminos (ejemplo, para n=6 --->  [1, 1, 2, 3, 5, 8])
#Comprobar si un numero es palindromico, y si lo es, sumar sus cifras (ejemplo, 12321 ---> 9)
#Validador de email. Validar que un diccionario de usuario con email tiene un email correcto (ejemplo@ejemplo.com es valido)
#Validador de contraseña. Validar que un usuario ha introducido una contraseña con:
#Al menos 1 mayuscula
#Al menos 1 minuscula
#Al menos 1 caracter especial
#Al menos 1 numero
#Minimo 12 caracteres de tamaño
"""
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

#ValidaPW("beatkjdMgkajdjghadjhgadais")

def romano_a_decimal(romano: str) -> int:
   valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} #DICCINARIO
   decimal = 0
   prev_value = 0
  
   for char in romano:  #  Para iterar 
       value = valores[char]
       if value < prev_value:
           decimal -= value
       else:
           decimal += value
       prev_value = value
  
   return decimal
 
romano = input("Introduce un número romano: ")
decimal = romano_a_decimal(romano)
print(f"El número decimal es: {decimal}")


