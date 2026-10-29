
"""
PUNTO 4: NUMEROS ABUNDANTES

ENTRADA:
- Rango inicial.
- Rango final.

PROCESO:
- Recorrer todos los numeros del rango.
- Buscar los divisores propios de cada numero.
- Sumar los divisores propios.
- Si la suma es mayor que el numero, es abundante.

SALIDA:
- Mostrar la lista de numeros abundantes encontrados.
"""

# ENTRADA
inicio = int(input("Ingrese el rango inicial: "))
final = int(input("Ingrese el rango final: "))

# PROCESO
abundantes = []

if inicio > final:
    print("Error: el rango inicial no puede ser mayor que el final.")
else:
    for numero in range(max(1, inicio), final + 1):
        suma = 0

        for divisor in range(1, numero):
            if numero % divisor == 0:
                suma = suma + divisor

        if suma > numero:
            abundantes.append(numero)

    # SALIDA
    print("Numeros abundantes entre", inicio, "y", final, ":")
    print(abundantes)
