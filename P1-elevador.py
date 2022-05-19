# Aluno: Kaian Vinicius Rodrigues Pereira #
capacidade = float(input("Qual a capacidade máxima, em quilos, do elevador?\n"))
p5p = float(input("Qual o peso, em quilos, das 5 pessoas que entraram no elevador?\n"))

if p5p>capacidade:
    print("O elevador não pode subir, excesso no limite de peso.")
else:
    print("O elevador pode subir!")