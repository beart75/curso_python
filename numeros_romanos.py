romanos = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman2int(romval):
    total = 0
    prev = 0
    contador = 0
    
    for letra in romval[::-1]:
        valor = romanos[letra]
        print(f"siguiente es {letra} = {valor} y anterior {prev} ")
        total += valor if valor >= prev else -valor
        prev = valor
        if (valor ==prev):
            contador +=1
    if contador > 4:
        print("no es un numero romano valido")
        return "ERROR"
    else:
        return total

#tests = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "XIV", "CXC", "MIM"]

test = str.upper(input("Ingrese un numero romano: "))

#comprobar que es un numero romano correcto
# Si un símbolo romano está seguido de un símbolo mayor, réstale su valor al resultado.
#FALTA ESTA COMPROBACION

print(f"{test} es {roman2int(test)}")