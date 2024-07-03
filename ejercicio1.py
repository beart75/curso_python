

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
