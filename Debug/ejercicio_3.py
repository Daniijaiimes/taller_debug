
"""
PUNTO 3: NUMEROS NARCISISTAS (ARMSTRONG)

ENTRADA:
- Varios numeros enteros mayores que cero.
- Cero o un numero negativo para terminar.

PROCESO:
- Contar la cantidad de digitos del numero.
- Elevar cada digito a la potencia de la cantidad de digitos.
- Sumar los resultados.
- Comparar la suma con el numero original.

SALIDA:
- Indicar si el numero es narcisista o no.
"""

# ENTRADA
while True:
    numero = int(input("Ingrese un numero positivo (0 o negativo para terminar): "))

    if numero <= 0:
        print("Programa terminado.")
        break

    # PROCESO
    digitos = str(numero)
    cantidad = len(digitos)
    suma = 0

    for digito in digitos:
        suma = suma + int(digito) ** cantidad

    # SALIDA
    if suma == numero:
        print(numero, "es un numero narcisista.")
    else:
        print(numero, "no es un numero narcisista.")
