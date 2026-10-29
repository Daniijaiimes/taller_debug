
"""
PUNTO 2: NUMEROS PERFECTOS

ENTRADA:
- Numeros enteros mayores que 2.
- Un numero negativo para terminar.

PROCESO:
- Buscar los divisores propios del numero.
- Sumar los divisores.
- Comparar la suma con el numero ingresado.
- Repetir hasta ingresar un numero negativo.

SALIDA:
- Indicar si el numero es perfecto o no.
"""

# ENTRADA
while True:
    numero = int(input("Ingrese un numero mayor que 2 (negativo para terminar): "))

    if numero < 0:
        print("Programa terminado.")
        break

    if numero <= 2:
        print("Error: ingrese un numero mayor que 2.")
        continue

    # PROCESO
    suma = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma = suma + divisor

    # SALIDA
    if suma == numero:
        print(numero, "es un numero perfecto.")
    else:
        print(numero, "no es un numero perfecto.")
