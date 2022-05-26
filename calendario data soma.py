#brainfuck total, incompleto, kudos pra quem fez a livraria de datetime#

dia = int(input("Insira o dia:\n"))
mes = int(input("Insira o mês:\n"))
ano = int(input("Insira o ano:\n"))

soma = int(input("Quantos dias você quer somar a essa data?\n"))

dia_e_soma = dia+soma

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10:
    dias_restantes=31-dia
    if soma>dias_restantes:
        dia = dia_e_soma-31
        mes = mes+1
        print(dia,mes,ano)
    else:
        print(dia_e_soma,mes,ano)
elif mes==2:
    dias_restantes=28-dia
elif mes==4:
    dias_restantes=29-dia
elif mes==12:
    dias_restantes=31-dia
    if soma>dias_restantes:
        dia = dia_e_soma-31
        mes = 1
        ano = ano+1
        print(dia,mes,ano)
    else:
        print(dia_e_soma,mes,ano)
else:
    dias_restantes=30-dia

print(dias_restantes, dia_e_soma)