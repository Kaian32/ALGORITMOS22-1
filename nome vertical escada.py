nome = input("Por favor, insira seu nome:\n")
nome = nome.upper()
nomelist = list(nome)
contletras = len(nomelist)
contador = 0
letralist = list()

while contletras != contador:
    print(nome,"possui",contletras,"letras.\n")
    for letra in nomelist:
        letralist.append(letra)
        letrasoma = "".join(letralist)
        print(letrasoma)
        contador += 1