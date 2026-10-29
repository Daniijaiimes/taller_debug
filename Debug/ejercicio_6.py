
"""
PUNTO 6: ANIO BISIESTO

ENTRADA:
- Dos años enteros entre 1 y 9999.

PROCESO:
- Crear una funcion para comprobar si un año es bisiesto.
- Un año es bisiesto si es divisible por 400.
- Tambien es bisiesto si es divisible por 4 y no es divisible por 100.
- Realizar la comprobacion para ambos años.
- Comparar los resultados para saber si ambos años comparten
  la misma condicion de bisiesto.

SALIDA:
- Mostrar si el primer año es bisiesto.
- Mostrar si el segundo año es bisiesto.
- Mostrar si ambos años tienen la misma condicion.
"""

# PROCESO: FUNCION PARA COMPROBAR ANIO BISIESTO
def es_bisiesto(anio):
    if anio < 1 or anio > 9999:
        return False

    if anio % 400 == 0:
        return True
    elif anio % 4 == 0 and anio % 100 != 0:
        return True
    else:
        return False


# ENTRADA
anio1 = int(input("Ingrese el primer anio (1-9999): "))
anio2 = int(input("Ingrese el segundo anio (1-9999): "))


# PROCESO Y SALIDA
resultado1 = es_bisiesto(anio1)
resultado2 = es_bisiesto(anio2)

misma_condicion = resultado1 == resultado2

print("Anio", anio1, "bisiesto:", resultado1)
print("Anio", anio2, "bisiesto:", resultado2)
print("Misma condicion:", misma_condicion)
