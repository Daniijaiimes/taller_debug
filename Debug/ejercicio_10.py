
"""
PUNTO 10: REPOSICION CON MINIMO Y CAPACIDAD MAXIMA

ENTRADA:
- Existencias actuales.
- Cantidad minima requerida.
- Capacidad maxima permitida.
- Tamano del lote.

PROCESO:
- Crear una funcion para comprobar si se necesita reponer.
- Crear una funcion para calcular los lotes necesarios.
- Crear una funcion para calcular el pedido.
- Solo se repone cuando las existencias son menores que el minimo.
- Calcular el faltante y los lotes necesarios para cubrirlo.
- Si el pedido supera la capacidad maxima, devolver -1.
- Si no se necesita reponer, devolver 0.

SALIDA:
- Mostrar si se necesita reponer.
- Mostrar la cantidad que se debe pedir.
- Si el pedido no cabe en la capacidad, mostrar un mensaje de imposibilidad.
"""

# PROCESO: FUNCION PARA COMPROBAR SI SE NECESITA REPONER
def necesita_reponer(existencias, minimo):
    return existencias < minimo


# PROCESO: FUNCION PARA CALCULAR LOS LOTES NECESARIOS
def lotes_necesarios(faltante, lote):
    if faltante % lote == 0:
        return faltante // lote
    else:
        return faltante // lote + 1


# PROCESO: FUNCION PARA CALCULAR EL PEDIDO
def calcular_pedido(existencias, minimo, capacidad, lote):
    if not necesita_reponer(existencias, minimo):
        return 0

    faltante = minimo - existencias
    lotes = lotes_necesarios(faltante, lote)
    pedido = lotes * lote

    if existencias + pedido > capacidad:
        return -1

    return pedido


# ENTRADA
existencias = int(input("Ingrese las existencias actuales: "))
minimo = int(input("Ingrese la cantidad minima: "))
capacidad = int(input("Ingrese la capacidad maxima: "))
lote = int(input("Ingrese el tamano del lote: "))


# PROCESO Y SALIDA
necesita = necesita_reponer(existencias, minimo)
pedido = calcular_pedido(existencias, minimo, capacidad, lote)

print("Necesita:", necesita)

if pedido == -1:
    print("Retorno: -1")
    print("No cabe el pedido")
elif pedido == 0:
    print("Pedido:", pedido)
    print("No necesita reponer")
else:
    print("Pedido:", pedido)
