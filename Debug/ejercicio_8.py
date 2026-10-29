
"""
PUNTO 8: RESERVA DE DOS SALAS PARA EL MISMO GRUPO

ENTRADA:
- Capacidad y ocupacion de la sala 1.
- Capacidad y ocupacion de la sala 2.
- Cantidad de personas del grupo.

PROCESO:
- Crear una funcion para calcular los cupos libres de una sala.
- Crear una funcion para elegir la sala adecuada.
- Calcular los cupos libres de ambas salas.
- Verificar si el grupo cabe en cada sala.
- Si el grupo cabe en ambas salas, elegir la que deje menos
  cupos libres despues de la reserva.
- Si hay empate, elegir la sala 1.
- Si el grupo no cabe en ninguna sala, retornar 0.

SALIDA:
- Mostrar la sala elegida.
- Si no hay sala disponible, mostrar "Sin sala".
"""


# PROCESO: FUNCION PARA CALCULAR CUPOS LIBRES
def cupos_libres(capacidad, ocupacion):
    return capacidad - ocupacion


# PROCESO: FUNCION PARA ELEGIR LA SALA
def elegir_sala(capacidad1, ocupacion1, capacidad2, ocupacion2, grupo):
    libres1 = cupos_libres(capacidad1, ocupacion1)
    libres2 = cupos_libres(capacidad2, ocupacion2)

    sala1 = libres1 >= grupo
    sala2 = libres2 >= grupo

    if sala1 and sala2:
        sobrantes1 = libres1 - grupo
        sobrantes2 = libres2 - grupo

        if sobrantes1 <= sobrantes2:
            return 1
        else:
            return 2

    elif sala1:
        return 1

    elif sala2:
        return 2

    else:
        return 0


# ENTRADA
capacidad1 = int(input("Ingrese la capacidad de la sala 1: "))
ocupacion1 = int(input("Ingrese la ocupacion de la sala 1: "))

capacidad2 = int(input("Ingrese la capacidad de la sala 2: "))
ocupacion2 = int(input("Ingrese la ocupacion de la sala 2: "))

grupo = int(input("Ingrese la cantidad de personas del grupo: "))


# PROCESO Y SALIDA
resultado = elegir_sala(
    capacidad1, ocupacion1,
    capacidad2, ocupacion2,
    grupo
)

if resultado == 0:
    print("Retorno:", resultado, "- Sin sala")
else:
    print("Sala elegida:", resultado)
