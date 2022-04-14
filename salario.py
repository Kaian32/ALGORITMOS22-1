sbase = int(input("Por favor, insira seu salário base: "))
grat = int(sbase*0.05)
imp = int(sbase*0.07)

salario = sbase+grat-imp

print("\nSeu salário base é de:",sbase,"reais","\nSua gratificação é de:",grat,"reais","\nSeu imposto sobre seu salário é de:",imp,"reais","\n\nSeu salário final é de:",salario,"reais")