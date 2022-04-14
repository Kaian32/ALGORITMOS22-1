pao = float(input("Insira a quantidade de pães vendidos: "))
broa = float(input("Insira a quantidade de broas vendidas: "))

pval = pao*0.50
bval = broa*1.50

total = pval+bval

poup = total*0.10

vfinal = total-poup

print("A padaria vendeu",pao,"pães e",broa,"broas","tendo um lucro total de",total,"reais,","desse valor,",poup,"reais vão para a poupança, deixando o dinheiro restante em",vfinal,"reais")