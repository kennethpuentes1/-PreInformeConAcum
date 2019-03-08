numero_1=0
print("Vamos a determinar el numero mas grande frente a otros 4 que usted define")
for x in range (0,5):
    num=int(input("ingrese Su numero: "))
    if x==0:
        mayor=num
    else:
        if num>mayor:
            mayor=num

print("El numero mayor entre los anteriores numeros es: " + str(mayor))