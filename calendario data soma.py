#brainfuck total, incompleto, kudos pra quem fez a livraria de datetime#
dia = int(input("Insira o dia:\n"))
mes = int(input("Insira o mês:\n"))
ano = int(input("Insira o ano:\n"))

soma = int(input("Quantos dias você quer somar a essa data?\n"))

valordata = 0
mesdias = 0
anodias = 0

#o inicio de uma nova tentativa, transformando a data em uma unidade única
if mes==1:
    mesdias = 0
elif mes==2:
    mesdias= 31
elif mes==3:
    mesdias = 59
elif mes==4:
    mesdias = 90
elif mes==5:
    mesdias = 120
elif mes==6:
    mesdias = 151
elif mes==7:
    mesdias = 181
elif mes==8:
    mesdias = 212
elif mes==9:
    mesdias = 243
elif mes==10:
    mesdias = 273
elif mes==11:
    mesdias = 304
elif mes==12:
    mesdias = 334

valordata = dia+mesdias

print(valordata)

#segue abaixo a versão inicial do meu plano#

#dia_e_soma = dia+soma

#if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10:
    #dias_restantes=31-dia
    #if soma>dias_restantes:
        #dia = dia_e_soma-31
        #mes = mes+1
        #print(dia,mes,ano)
    #else:
        #print(dia_e_soma,mes,ano)
#elif mes==2:
    #dias_restantes=28-dia
#elif mes==4:
    #dias_restantes=29-dia
#elif mes==12:
    #dias_restantes=31-dia
    #if soma>dias_restantes:
        #dia = dia_e_soma-31
        #mes = 1
        #ano = ano+1
        #print(dia,mes,ano)
    #else:
        #print(dia_e_soma,mes,ano)
#else:
    #dias_restantes=30-dia

#print(dias_restantes, dia_e_soma)