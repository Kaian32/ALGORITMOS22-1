nome = input("Por favor, insira seu nome:\n")
nomelist = list(nome)
contletras = len(nomelist)
contador = 0

while contletras != contador:
    print(nome,"possui",contletras,"letras.\n")
    for letra in nomelist:
        print(letra)
        contador += 1