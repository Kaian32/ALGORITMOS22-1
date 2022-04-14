sbase = float(input("Por favor, insira seu salário base: "))
grat = float(sbase*0.05)
imp = float(sbase*0.07)

salario = sbase+grat-imp

print("\nSeu salário base é de:",sbase,"reais","\nSua gratificação é de:",grat,"reais","\nSeu imposto sobre seu salário é de:",imp,"reais","\n\nSeu salário final é de:",salario,"reais")