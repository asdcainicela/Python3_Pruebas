"""
En esta tarea, se te pide crear un programa en Python que cuente desde 1 hasta un número límite ingresado por el usuario.
El programa debe utilizar un bucle while para llevar a cabo el conteo y mostrar los números en orden ascendente.
Una vez que se alcance el número límite, el programa debe imprimir "Conteo completado".
 
Instrucciones: 
    Solicita al usuario que ingrese un número entero positivo como límite para el conteo.
    Inicializa una variable llamada contador en 1.
    Utiliza un bucle while para realizar el conteo desde 1 hasta el número límite ingresado por el usuario.
    En cada iteración del bucle, muestra el valor actual de contador en la pantalla.
    Después de imprimir el número actual, incrementa el valor de contador en 1 para pasar al siguiente número.
    Cuando el valor de contador alcance o supere el número límite ingresado por el usuario, el bucle while debe detenerse.
    Imprime "Conteo completado" para indicar que el conteo ha terminado.
"""

limConteo = int(input("Ingrese el número límite de conteo: "))
contador = 1
suma = 0
while contador <= limConteo:
    print(contador)
    suma+= contador
    contador+=1
    
print("la suma total es: ", suma)
