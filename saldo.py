sal = int(input("Por favor, insira o valor do seu salário: "))
achq = int(input("Por favor, insira o valor de seu primeiro cheque emitido: "))
bchq = int(input("Por favor, insira o valor de seu segundo cheque emitido: "))

achqimp = achq*0.0038
bchqimp = bchq*0.0038

imp = achqimp+bchqimp

div = (achqimp+bchqimp)-sal
saldo = div+sal

print("\n\nSeus dividendos são no valor de",div*-1,"reais")
print("Os impostos sobre seus dividendos são no valor de",imp,"reais")
print("Seu saldo restante é de", saldo)
