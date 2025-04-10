#1. Crea una clase Persona con nombre, edad y ciudad
#   a)Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
#   b)Crea tres personas y muestra su saludo
#   c)Agrega un método para verificar si es mayor de edad
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def saludo(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")
    
    def mayordeedad(self):
        return self.edad >= 18

persona1 = Persona("Juan", 25, "La Paz")
persona2 = Persona("María", 17, "Santa Cruz")
persona3 = Persona("Carlos", 30, "Cochabamba")
persona1.saludo()
persona2.saludo()
persona3.saludo()
print(f"{persona1.nombre} es mayor de edad: {persona1.mayordeedad()}")
print(f"{persona2.nombre} es mayor de edad: {persona2.mayordeedad()}")
print(f"{persona3.nombre} es mayor de edad: {persona3.mayordeedad()}")
