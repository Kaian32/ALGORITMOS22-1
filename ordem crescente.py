a = float(input("Insira o valor A:\n"))
b = float(input("Insira o valor B:\n"))
c = float(input("Insira o valor C:\n"))

if a>b and a>c:
    primeiro = a

if b>a and b>c:
    primeiro = b

if c>a and c>b:
    primeiro = c

if a<b and a<c:
    ultimo = a

if b<a and b<c:
    ultimo = b

if c<a and c<b:
    ultimo = c

if a!=primeiro and a!=ultimo:
    print("A ordem crescente deste três valores é a seguinte:",ultimo, a, primeiro)
elif b!=primeiro and b!=ultimo:
    print("A ordem crescente deste três valores é a seguinte:",ultimo, b, primeiro)
elif c!=primeiro and c!=ultimo:
    print("A ordem crescente deste três valores é a seguinte:",ultimo, c, primeiro)