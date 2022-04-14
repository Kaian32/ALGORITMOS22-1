nome = input("Por favor, informe seu nome: ")
curso = input("Por favor, informe seu curso: ")
anonasc = input("Em qual ano você nasceu? ")
filhos = input("Você tem quantos filhos? ")
rg = input("Informe seu RG: ")
salario = input("Qual seu salário? ")

print("Seu nome é", nome, ", Você atualmente está no curso", curso, ", Nasceu em", anonasc, ", Tem", filhos, "filhos", "Seu número de RG é", rg, "e você possui um salário de", salario, "reais.")

ativo = bool(int(input("Você está ativo? Digite 0 caso não esteja ou 1 caso esteja:")))
#print (ativo)
if (ativo):

    print("Você está ativo! Parabéns!")
else:
    print("Infelizmente, você não está ativo!")