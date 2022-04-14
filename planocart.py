p1x = float(input("Qual o valor X do primeiro ponto? "))
p1y = float(input("Qual o valor Y do primeiro ponto? "))

p2x = float(input("\nQual o valor X do segundo ponto? "))
p2y = float(input("Qual o valor Y do segundo ponto? "))

dist = ((p2x-p1x)**2+(p2y-p1y)**2)**0.5

print("A distância entre esses dois ponto é",dist)