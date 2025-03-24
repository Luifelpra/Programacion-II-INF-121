import math

def getDiscriminante(a, b, c):
    return b**2 - 4*a*c

def getRaiz1(a, b, c):
    discriminante = getDiscriminante(a, b, c)
    if discriminante < 0:
        return None
    return (-b + math.sqrt(discriminante)) / (2*a)

def getRaiz2(a, b, c):
    discriminante = getDiscriminante(a, b, c)
    if discriminante < 0:
        return None
    return (-b - math.sqrt(discriminante)) / (2*a)

def respuesta(a, b, c):
    discriminante = getDiscriminante(a, b, c)
    if discriminante > 0:
        r1 = getRaiz1(a, b, c)
        r2 = getRaiz2(a, b, c)
        print(f"La ecuación tiene dos raíces {r1:.6f} y {r2:.6f}")
    elif discriminante == 0:
        r1 = getRaiz1(a, b, c)
        print(f"La ecuación tiene una raíz {r1:.0f}")
    else:
        print("La ecuación no tiene raíces reales")

valores = [(1.0, 3, 1), (1, 2.0, 1), (1, 2, 3)]

for a, b, c in valores:
    respuesta(a, b, c)
