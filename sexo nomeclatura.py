sexo = int(input("Qual seu sexo? Digite 0 para masculino, 1 para feminino e 2 caso prefira não informar.\n"))

if sexo == 2:
    print("FIm do algoritmo.")
    exit()

id = int(input("Qual sua idade?\n"))

if sexo == 0:
    if id<12:
        nome = "menino"
    elif id<24:
        nome = "rapaz"
    else:
        nome = "homem"
    print("Você tem",id,"e é um",nome,".")


if sexo == 1:
    if id<12:
        nome = "menina"
    elif id<24:
        nome = "moça"
    else:
        nome = "mulher"
    print("Você tem",id,"e é uma",nome,".")