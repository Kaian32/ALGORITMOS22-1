# Aluno: Kaian Vinicius Rodrigues Pereira #
sal = float(input("Qual o seu salário?\n"))
if sal > 1100:
    aumento = sal*0.10
    salaum = sal+aumento
    print("Funcionário, seu aumento será de 10%, ou seja,",aumento,"reais, levando ao seu novo salário total de",salaum,"reais.")
else:
    aumento = sal*0.15
    salaum = sal+aumento
    print("Funcionário, seu aumento será de 15%, ou seja,",aumento,"reais, levando ao seu novo salário total de",salaum,"reais.")