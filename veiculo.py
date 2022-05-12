fab = float(input("Qual o valor de fábrica do veículo?\n"))
dist = float(input("Qual o percentual de lucro do revendedor?\n"))
imp = float(input("Qual o percentual dos impostos?"))

pfin = fab+(fab*(dist/100))+(fab*(imp/100))

print("O preço final do veículo é",pfin,"reais.\n")
