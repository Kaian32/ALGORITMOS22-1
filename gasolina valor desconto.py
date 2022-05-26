liq = input("Digite A para álcool e G para gasolina\n")
if liq=="a":
    liq="A"
elif liq=="g":
    liq="G"
else:
    print("Insira um tipo correto!")
    exit()

lit = float(input("Quantos litros?\n"))

if liq=="A":
    if lit>20:
        val=(lit*6.50)*0.95
    else:
        val=(lit*5.50)*0.97
    print("O valor total a ser pago é:",val)

if liq=="G":
    if lit>20:
        val=(lit*6.50)*0.94
    else:
        val=(lit*5.50)*0.96
    print("O valor total a ser pago é:",val)