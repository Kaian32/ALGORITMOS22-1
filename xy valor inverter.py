x = float(input("Insira o valor X:\n"))
y = float(input("Insira o valor Y:\n"))

if (x+y)*0.30>500:
   x1 = x
   y1 = y
   x = y
   y = x1
   print("Os valores de X e Y são, respectivamente",x,"e",y)

else:
    if x>y:
        print ("O menor valor entre X e Y é",y)
    else:
        print ("O menor valor entre X e Y é",x)
