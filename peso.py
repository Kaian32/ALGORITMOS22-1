from pickletools import float8


prato = float(input("QUal o peso do prato em gramas? "))
peso = float(input("Qual o peso total do prato com a comida em gramas? "))

vprato = (prato/1000)*45
vpeso = (peso/1000)*45

valor = vpeso-vprato

print("O valor a ser pago é de",valor,"reais")