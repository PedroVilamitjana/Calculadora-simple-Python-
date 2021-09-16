#CONDICIONES (USANDO SEGUN CASO)
# voy a crear una calculadora simple.

#Inicio del programa.
from math import * # Agrego la carperta de matematica.
bandera = False; #con esto deternimo si se puedo ejecutar o no ciertas acciones. (Bandera = 0).

#Pido los dos valores.
x = float(input("Ingrese un numero x: "));
y = float(input("Ingrese un numero y: "));

#Muestro los casos

print("Caso 1 : Suma de los dos numeros. (El primero mas el segundo)");
print("Caso 2 : Resta de los dos numeros.(El primero menos el segundo )");
print("Caso 3 : Multiplicar los dos numeros. (El primero por el segundo)");
print("Caso 4 : Dividir los dos numeros. (El primero Sobre el segundo)");
print("Caso 5 : Potencia (El primero a elevado a la sengunda).");
print("Caso 6 : Logaritmo del primero.");

opcion = int(input("Ingrese la opcion: ")); #opcion va hacer aquella que determine la expresion para cada caso donde se cumpla.

if (opcion == 1):
    z = x + y;
    print(x , "+" , y);
elif (opcion == 2):
    z = x - y;
    print(x ,"-", y);
    
elif (opcion == 3):
    z = x * y;
    print(x ,"x", y);
    
elif (opcion == 4 and (y != 0)): # En el caso de que "y" sea distinto de CERO, se pueda efectuar la divicion. 
    z = x/y;
    print(x ,"/", y);
elif(opcion == 4 and (y == 0)):
    print("El denominador es igual a cero.");
    print("No se puede hacer la divicion.");
    bandera = True;
    
elif (opcion == 5):
    z = pow(x,y);
    print(x,"^",y);
    
elif(opcion == 6 and (x != 0) and (x > 0)): 
    z = log(x);
    print("Log", x);
    
elif(opcion == 6 and (x == 0)and (x <= 0)):
    print("No se puede efectuar el Logaritmo.");
    print("El primer numero es igual o menor a cero.");
    bandera = True; #Con badera TRUE me indica que no puedo hacer el logaritmo. 
else: 
    print("Opcion desconocida. ");
#se escribe el resulado en otra condicion.
if(opcion < 7 and bandera == False ):
    print("El resultado es: ", z); #Esto se hizo para ahorrar codigo, en todas las opc sea la misma variable. Modulizar

    

