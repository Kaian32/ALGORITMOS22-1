a = int(input("Por favor, insira o valor A\n"))
b = int(input("Por favor, insira o valor B\n"))
c = int(input("Por favor, insira o valor C\n"))
d = int(input("Por favor, insira o valor D\n"))
e = int(input("Por favor, insira o valor E\n"))

if a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e:
    print("Um dos números digitados é igual a outro inserido!\nInsira cinco números inteiros diferentes e tente novamente.")
    exit()

if a>b and a>c and a>d and a>e:
    primeiro = a

if b>a and b>c and b>d and b>e:
    primeiro = b

if c>a and c>b and c>d and c>e:
    primeiro = c

if d>a and d>b and d>c and d>e:
    primeiro = d

if e>a and e>b and e>c and e>d:
    primeiro = e

print("O maior valor è:",primeiro)

