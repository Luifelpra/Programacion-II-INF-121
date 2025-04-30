from abc import ABC, abstractmethod
import math

class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color: str = "negro"):
        self.color = color
    
    def setColor(self, color: str) -> None:
        self.color = color
    
    def getColor(self) -> str:
        return self.color
    
    def toString(self) -> str:
        return f"Figura color {self.color}"
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str = "negro"):
        super().__init__(color)
        self.lado = lado
    
    def area(self) -> float:
        return self.lado ** 2
    
    def perimetro(self) -> float:
        return 4 * self.lado
    
    def comoColorear(self) -> str:
        return "Colorear los cuatro lados"
    
    def toString(self) -> str:
        return f"Cuadrado de lado {self.lado}, {super().toString()}"

class Circulo(Figura):
    def __init__(self, radio: float, color: str = "negro"):
        super().__init__(color)
        self.radio = radio
    
    def area(self) -> float:
        return math.pi * (self.radio ** 2)
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.radio
    
    def toString(self) -> str:
        return f"Círculo de radio {self.radio}, {super().toString()}"