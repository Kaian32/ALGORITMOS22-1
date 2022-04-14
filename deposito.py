dep = int(input("Por favor, insira o valor de seu depósito: "))
juros = (0.1225)
rend = int(dep*(juros*12))
rendb = rend-dep

print("\nSeu depósito é de:",dep,"reais","\nA taxa anual de juros, no momento, é de:",juros*100,"%","\n\nSeu rendimento bruto em 12 meses será:",rendb, "reais","\nSeu rendimento após 12 meses será de:",rend,"reais", )