import time
a=0
a2=0
while a<100:
    a+=1
    a2+=a
    time.sleep(0.5)
    print(a)
print("A soma de todos estes números resulta em:",a2)