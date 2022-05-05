sexo = int(input("Informe seu sexo: 1 para Feminino, 2 para Masculino ou 3 para Não Informar\n"))
if sexo == 3:
    print("FIm do Algoritmo.")
else:
    altura = float(input("Qual a sua altura em metros?\n"))

if sexo == 1:
    peso = (62.1*altura)-44.7
    print("No sexo feminino, seu peso ideal é:",peso)

if sexo == 2:
    peso = (72.7*altura)-58
    print("No sexo masculino, seu peso ideal é:",peso)