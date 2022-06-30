data = input("Por favor, insira a data de nascimento no formato dd/mm/aaaa.\n")
datalist = list(data.split("/"))

print(datalist)

mes = datalist[1]
if mes == "01":
    mes = "Janeiro"
elif mes == "02":
    mes = "Fevereiro"
elif mes == "03":
    mes = "Março"
elif mes == "04":
    mes = "Abril"
elif mes == "05":
    mes = "Maio"
elif mes == "06":
    mes = "Junho"
elif mes == "07":
    mes = "Julho"
elif mes == "08":
    mes = "Agosto"
elif mes == "09":
    mes = "Setembro"
elif mes == "10":
    mes = "Outubro"
elif mes == "11":
    mes = "Novembro"
elif mes == "12":
    mes = "Dezembro"

print("A data de nascimente em extenso é:", datalist[0], "de", mes, "de", datalist[2])