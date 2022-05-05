adulto = int(input("Você tem mais de 18 anos? 0 para não e 1 para sim\n"))

if adulto == 0:
    print("Fim do Algoritmo.")
    

peso = float(input("Qual seu peso em quilos?\n"))
altura = float(input("Qual sua altura em metros?\n"))

IMC = peso/(altura/0.5)

if IMC < 18.5:
    print("Tá fraco! Vai procurar um médico, IMC abaixo do peso!")
else: 
    if 18.5 < IMC < 25:
        print("IMC na média do peso, parabéns!")
    else:
        if 25 < IMC < 30:
            print("IMC acima do peso hein, bora se exercitar!")
        else:
            if 25 < IMC < 30:
                print("IMC acima do peso hein, bora se exercitar!")
            else:
                if IMC > 30:
                    print("IMC de obeso, procura um médico!")