import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros):
    media = promedio(numeros)
    suma_diferencias = sum((x - media) ** 2 for x in numeros)
    return math.sqrt(suma_diferencias / (len(numeros) - 1))

numeros = list(map(float, input("Ingrese 10 números separados por espacios: ").split()))
if len(numeros) != 10:
    print("Error: Debe ingresar exactamente 10 números.")
else:
    media = promedio(numeros)
    desvio = desviacion(numeros)
    print(f"El promedio es {media:.2f}")
    print(f"La desviación estándar es {desvio:.5f}")
