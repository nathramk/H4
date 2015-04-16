#programa que diga si eres oven, adulto o abuelo
#entrada
edad=input("ingrese su edad: ")
#proceso
if edad<18 and edad<=18:
    r="usted es joven"
else:
    if edad>18 and edad<=60:
        r="usted es adulto"
    else:
        r="usted es mayor de edad"
#salida
print r
