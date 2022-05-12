from xml.etree.ElementTree import C14NWriterTarget


sal = float(input("Qual o seu salário?\n"))
c1 = float(input("Qual o valor da primeira conta?\n"))
c2 = float(input("Qual o valor da segunda conta?\n"))

resto = sal-(c1+(c1*0.02)+c2+(c2*0.02))

print("Após o pagamento das dívidas, a quantidade de dinheiro que sobrará de seu salário é:",resto,"reais.")