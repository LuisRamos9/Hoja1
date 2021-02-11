print("Hola de trabajo 1")
print("Ejerncicio No.1")
x = int(input("Ingrese un número entero "))
if x>=0:
    for i in range (x):
        for j in range(i+1):
            print("*", end="") 
        print(" ")
else:
    print("Tienes que ingresar un número entero")
print("Ejericio No.2")
n = int (input("Ingrese un número entero "))
cont=0 
if n>1:
    for i in range(2,n):
        x=n%i
        if x==0:
            cont+=1
    if cont==0:
        print ("Es un número primo")
    else:
        print ("No es un número primo")
else:
    print( "No es un número primo")