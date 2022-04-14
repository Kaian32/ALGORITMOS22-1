saldo = 0.0
sal = float(input("Por favor, insira o valor do seu salário: "))
achq = float(input("Por favor, insira o valor de seu primeiro cheque emitido: "))
bchq = float(input("Por favor, insira o valor de seu segundo cheque emitido: "))

achqimp = achq*0.0038
bchqimp = bchq*0.0038

imp = achqimp+bchqimp
div = (achqimp+bchqimp)+(achq+bchq)
saldo = sal-div
#saldo = div+sal

print("\n\nSeus dividendos são no valor de",div,"reais")
print("Os impostos sobre seus dividendos são no valor de",imp,"reais")
print("Seu saldo restante é de", saldo)
