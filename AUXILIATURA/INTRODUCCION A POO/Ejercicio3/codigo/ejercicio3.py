#3.Crea una clase Coche con marca, modelo y velocidad
#    a) Agrega un método acelerar () que aumente la velocidad en 10
#    b) Agrega un método frenar () que disminuya la velocidad en 5
#    c) Crea dos coches, aceléralos, frénalos y muestra sus velocidadesclass Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    
    def acelerar(self):
        self.velocidad += 10
    
    def frenar(self):
        self.velocidad = max(0, self.velocidad - 5)
    
    def mostrar_velocidad(self):
        print(f"{self.marca} {self.modelo}: Velocidad actual = {self.velocidad} km/h")

coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")

coche1.acelerar()
coche2.acelerar()
coche2.acelerar() 

coche1.frenar()
coche2.frenar()

coche1.mostrar_velocidad()
coche2.mostrar_velocidad()
