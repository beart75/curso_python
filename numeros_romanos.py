romanos = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman2int(romval):
    total = 0
    prev = 0
    for letra in romval[::-1]:
        valor = romanos[letra]
        total += valor if valor >= prev else -valor
        prev = valor

    return total

#tests = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "XIV", "CXC", "MIM"]

test = input("Ingrese un numero romano: ")
#comprobar que es un numero romano correcto
# Si un símbolo romano está seguido de un símbolo mayor, réstale su valor al resultado.
print(f"{test} es {roman2int(test)}")