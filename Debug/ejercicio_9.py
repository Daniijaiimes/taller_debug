
"""
PUNTO 9: COSTO DE ENVIO CON COBERTURA Y DESCUENTO

ENTRADA:
- Peso del paquete en kilogramos.
- Zona de envio (1 o 2).
- Valor de la compra en pesos.

PROCESO:
- Crear una funcion para comprobar si el envio tiene cobertura.
- La cobertura es valida si el peso es mayor que 0 y hasta 20 kg,
  y la zona es 1 o 2.
- Crear una funcion para calcular el costo inicial del envio.
- La tarifa base es de 5000 pesos en zona 1 y 8000 pesos en zona 2.
- Cada kilogramo por encima de 1 kg agrega 2000 pesos proporcionales.
- Crear una funcion para calcular el costo final.
- Si la compra es de al menos 100000 pesos, aplicar un descuento
  del 50 por ciento al costo inicial.
- Si no hay cobertura, retornar -1 sin aplicar descuentos.

SALIDA:
- Mostrar el costo final del envio.
- Si no hay cobertura, mostrar "Sin cobertura".
"""


# PROCESO: FUNCION PARA COMPROBAR COBERTURA
def cobertura(peso, zona):
    if peso > 0 and peso <= 20 and (zona == 1 or zona == 2):
        return True
    else:
        return False


# PROCESO: FUNCION PARA CALCULAR COSTO INICIAL
def costo_inicial(peso, zona):
    if zona == 1:
        base = 5000
    else:
        base = 8000

    recargo = 2000 * max(peso - 1, 0)

    costo = base + recargo

    return costo


# PROCESO: FUNCION PARA CALCULAR COSTO FINAL
def costo_final(peso, zona, compra):
    if not cobertura(peso, zona):
        return -1

    costo = costo_inicial(peso, zona)

    if compra >= 100000:
        costo = costo * 0.50

    return costo


# ENTRADA
peso = float(input("Ingrese el peso del paquete en kg: "))
zona = int(input("Ingrese la zona de envio (1 o 2): "))
compra = float(input("Ingrese el valor de la compra en pesos: "))


# PROCESO Y SALIDA
resultado = costo_final(peso, zona, compra)

if resultado == -1:
    print("Retorno:", resultado, "- Sin cobertura")
else:
    print("Costo:", resultado, "pesos")
