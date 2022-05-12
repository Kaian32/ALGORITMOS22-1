idade = int(input("Qual sua idade?\n"))

if idade>=18:
    print("Você pode votar e tirar sua carteira de habilitação!")
elif idade<16:
    print("Você não pode votar nem tirar a carteira de habilitação.")
else:
    print("Você pode votar, mas nao pode tirar a carteira de habilitação.")