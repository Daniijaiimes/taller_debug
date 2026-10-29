
"""
PUNTO 5: COMPROBAR MULTIPLOS EN AMBAS DIRECCIONES

ENTRADA:
- Dos numeros enteros.

PROCESO:
- Crear una funcion para comprobar si un numero es multiplo de otro.
- Si el divisor es cero, devolver False.
- Si el residuo de la division es cero, devolver True.
- Realizar la comprobacion en ambas direcciones.

SALIDA:
- Mostrar si el primer numero es multiplo del segundo.
- Mostrar si el segundo numero es multiplo del primero.
"""

# PROCESO: FUNCION PARA COMPROBAR MULTIPLOS
def es_multiplo(numero, divisor):
    if divisor == 0:
        return False

    if numero % divisor == 0:
        return True
    else:
        return False


# ENTRADA
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

# PROCESO Y SALIDA
resultado1 = es_multiplo(numero1, numero2)
resultado2 = es_multiplo(numero2, numero1)

print(numero1, "multiplo de", numero2, ":", resultado1)
print(numero2, "multiplo de", numero1, ":", resultado2)
