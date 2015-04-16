#entrada
nombre=raw_input("ingrese nombre: ")
#proceso
id(3)
nombre=3
#salida
print id(nombre)

#programa que diga si es par o impar un numero
#entrada
numero=input("ingrese un numero: ")
#proceso
if numero%2==0: 

    r="par"
else:
    r="inpar"
#salida
print r

#programa que diga si es mayor o menor un numero
#entrada
a=input("ingrese un numero: ")
b=input("ingrese un numero: ")
#proceso
if a==b:
    r="%s es igual %s"%(a,b)
else:
    if a<b:
        r="%s es menor que %s"%(a,b)
    else:
        r="%s es mayor que %s"%(a,b)
#salida
print r

#programa que diga si la edad es mayor o menor
#entrada
edad=input("ingrese su edad: ")
#proceso
if edad>0 and edad<=18:
    r="usted es joven" 
else:
    if edad>19 and edad<=60:
        r="usted es adulto" 
    else:
        r="usted es anciano" 
#salida
print r


