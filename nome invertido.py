nomeinput = input("Por favor, insira seu nome:\n") #input do nome a ser invertido
nomeinput = nomeinput.upper() #deixando o nome em caps
nomelist = list(nomeinput) #fazendo uma lista a partir do input
nomeinv = nomelist[::-1] #invertendo os nomes, fazendo a lista andar para tras
nomeinv = "".join(nomeinv) #juntando a lista invertida
print(nomeinv) #print do nome invertido