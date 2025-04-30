from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
    
    @abstractmethod
    def calcularprecio(self):
        pass
    
    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.calcularprecio():.1f}"


class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
    
    def calcularprecio(self):
        return 100.0


class Platea(Boleto):
    def __init__(self, numero, diasanticipacion):
        super().__init__(numero)
        self.diasanticipacion = diasanticipacion
    
    def calcularprecio(self):
        if self.diasanticipacion >= 10:
            return 50.0
        else:
            return 60.0


class Galeria(Boleto):
    def __init__(self, numero, diasanticipacion):
        super().__init__(numero)
        self.diasanticipacion = diasanticipacion
    
    def calcularprecio(self):
        if self.diasanticipacion >= 10:
            return 25.0
        else:
            return 30.0