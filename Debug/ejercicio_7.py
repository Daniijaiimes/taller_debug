
"""
PUNTO 7: NUMERO PERFECTO

ENTRADA:
- Dos numeros enteros entre 1 y 10000.

PROCESO:
- Crear una funcion para comprobar si un numero es perfecto.
- Inicializar la suma de los divisores propios en 0.
- Recorrer los numeros desde 1 hasta antes del numero ingresado.
- Comprobar cuales numeros son divisores propios.
- Sumar los divisores propios encontrados.
- Un numero es perfecto si la suma de sus divisores propios
  es igual al numero ingresado.
- Realizar dos llamadas a la funcion.

SALIDA:
- Mostrar si el primer numero es perfecto.
- Mostrar si el segundo numero es perfecto.
"""


# PROCESO: FUNCION PARA COMPROBAR NUMERO PERFECTO
def numero_perfecto(n):
    suma = 0

    for d in range(1, n):
        if n % d == 0:
            suma = suma + d

    if suma == n:
        return True
    else:
        return False


# ENTRADA
numero1 = int(input("Ingrese el primer numero (1-10000): "))
numero2 = int(input("Ingrese el segundo numero (1-10000): "))


# PROCESO Y SALIDA
resultado1 = numero_perfecto(numero1)
resultado2 = numero_perfecto(numero2)

print("Numero", numero1, "perfecto:", resultado1)
print("Numero", numero2, "perfecto:", resultado2)
