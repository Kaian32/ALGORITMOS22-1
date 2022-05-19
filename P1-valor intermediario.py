# Aluno: Kaian Vinicius Rodrigues Pereira #

a = int(input("Por favor, insira o valor A\n"))
b = int(input("Por favor, insira o valor B\n"))
c = int(input("Por favor, insira o valor C\n"))

if a==b or a==c or b==c:
    print("Um dos números digitados é igual a outro inserido!\nInsira três números inteiros diferentes e tente novamente.")
    exit()

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
    print(a,"é o número intermediário dentre os três digitados,")
elif b!=primeiro and b!=ultimo:
    print(b,"é o número intermediário dentre os três digitados,")
elif c!=primeiro and c!=ultimo:
    print(c,"é o número intermediário dentre os três digitados,")