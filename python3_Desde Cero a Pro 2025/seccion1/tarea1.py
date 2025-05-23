"""Problema: Calificación de Estudiantes
Descripción:
Eres un profesor y deseas crear un programa en Python para evaluar las calificaciones de los estudiantes. El programa debe solicitar al usuario que ingrese su calificación como un número decimal. Luego, debe mostrar un mensaje que refleje su rendimiento de acuerdo con ciertos criterios:

Si la calificación es igual o mayor a 90, mostrar "¡Felicidades! Has aprobado con una calificación sobresaliente."
Si la calificación es igual o mayor a 70 pero menor que 90, mostrar "Has aprobado satisfactoriamente."
Si la calificación es igual o mayor a 60 pero menor que 70, mostrar "Has aprobado, pero necesitas mejorar un poco."
Si la calificación es menor que 60, mostrar "Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación."

Instrucciones:

Usa input() para obtener la calificación como entrada y conviértela en un número de punto flotante.
Utiliza if, elif y else para verificar las condiciones y mostrar el mensaje correspondiente según la calificación ingresada.
Ejecuta el programa, proporciona una calificación y observa el mensaje resultante.

Este programa permite a los estudiantes comprender cómo se pueden tomar decisiones basadas en condiciones en Python y cómo personalizar mensajes en función de diferentes calificaciones."""

# Definición de la función para evaluar la calificación
def evaluar_calificacion(calificacion):
    if calificacion >= 90:
        return "¡Felicidades! Has aprobado con una calificación sobresaliente."
    elif calificacion >= 70:
        return "Has aprobado satisfactoriamente."
    elif calificacion >= 60:
        return "Has aprobado, pero necesitas mejorar un poco."
    else:
        return "Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación."


a= int(input("Ingrese su calificación: "))  # Solicitar la calificación al usuario

print(evaluar_calificacion(a))  # Llamar a la función y mostrar el resultado
# Fin del programa