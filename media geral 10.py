import time
cont = 0
med = 0
a = 0
a2 = 0
while cont < 10:
    a += 1
    a2 += a
    time.sleep (0.2)
    print(a)
    print (a2)
    cont+=1
    print("\n")

time.sleep (0.2)
med = (a2/cont)
print ("A média geral entre esses números é:", med)

    