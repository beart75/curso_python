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

print(" ------------- VALIDADOR DE emails--------")

emails = {
        "paula" : {
            "email":"paulitabonita13@outlook.com",
            "activo": True
        },
        "carlos" : {
            "email":"cager87mail.com",
            "activo": False
        },
        "paula" : {
            "email":"lady_rainbow_vlc@yahoo.com",
            "activo": True
        }

}
#esta activo (con colecciones)
for nombre, datos in emails.items():
    email = datos["email"]
    activo = datos["activo"]
    if activo:
        print(f" email de  {nombre} ACTIVO ")
    else:
        print(f" email de  {nombre} NO ESTA ACTIVO ")
    #es email
    if email.find("@") > 0:
        print(f" email de  {nombre} tiene @ ")
    else:
        print(f" email de  {nombre} NO TIENE @ ")

    if email.find(".") > 0:
        print(f" email de  {nombre} tiene . ")
    else:
        print(f" email de  {nombre} NO tiene . ")

        print(" ------------- VALIDADOR DE CONTRASEÑAS--------")
