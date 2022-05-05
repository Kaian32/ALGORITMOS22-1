from calendar import c


a = int(input("Valor A: "))
b = int(input("Valor B: "))

if a == b:
    c = a+b
    print("A soma entre A e B resulta em",c)
else:
    c = a*b 
    print("A multiplicação entre A e B resulta em",c)
