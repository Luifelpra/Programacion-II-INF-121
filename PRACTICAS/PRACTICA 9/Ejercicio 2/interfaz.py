import random
from figuras import Cuadrado, Circulo, Coloreado

def main():
    figuras = []
  
    for _ in range(5):
        tipo = random.randint(1, 2)
        color = random.choice(["rojo", "azul", "verde", "amarillo", "negro"])
        size = random.uniform(1.0, 10.0)
        
        if tipo == 1:
            figuras.append(Cuadrado(size, color))
        else:
            figuras.append(Circulo(size, color))
    
  
    for i, figura in enumerate(figuras, 1):
        print(f"\nFigura {i}: {figura.toString()}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")
        
        if isinstance(figura, Coloreado):
            print(f"Método colorear: {figura.comoColorear()}")

if __name__ == "__main__":
    main()