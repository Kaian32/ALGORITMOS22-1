a = float(input("Insira o valor A: "))
b = float(input("Insira o valor B: "))
c = float(input("Insira o valor C: "))

if a > b and a > c:
    print("A é o maior valor!")
else: 
    if b > a and b > c:
        print("B é o maior valor!")
    else: 
        if c > a and c > b:
            print("c é o maior valor!")