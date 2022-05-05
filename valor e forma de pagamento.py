valor = float(input("Qual o valor do produto na etiqueta?\n"))
fpag = int(input("Qual a condição de pagamento? 1 para à vista, 2 para à vista no cartão de crédito, 3 para parcelado em duas vezes e 4 para pareclado em três vezes\n"))

if fpag == 1:
    resultado = valor - (valor*0.15)
    print("O valor a ser pago é:",resultado,"Reais.")
else:
    if fpag == 2:
        resultado = valor - (valor*0.10)
        print("O valor a ser pago é:",resultado,"Reais.")
    else:
        if fpag == 3:
            resultado = valor
            parcela = resultado/2
            print("O valor a ser pago é:",resultado,"Reais, pagando",parcela,"Reais por mês.")
        else:
            if fpag == 4:
                resultado = valor + (valor*0.10)
                parcela = resultado/3
                print("O valor a ser pago é:",resultado,"Reais, pagando",parcela,"Reais por mês.")
