l=[]
lim=int(input("Digite o limite:"))
numero = 2
print ("Primos:")
while numero <=lim:
    i = numero -1
    while i > 1:
        if numero % i == 0:
           break
        i=i-1
    else:
        l.append(numero)
    numero=numero+1
print(l)