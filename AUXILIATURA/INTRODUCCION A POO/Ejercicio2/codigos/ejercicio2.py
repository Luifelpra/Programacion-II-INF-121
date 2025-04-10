#2. Crea una clase Empleado con nombre y sueldo
#  a) Agrega un método para calcular el sueldo anual
#  b) Agrega un método para aplicar un aumento del 10%
#  c) Crea dos empleados y muestra sus sueldos antes y después del aumento
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def sueldoanual(self):
        return self.sueldo * 12
    
    def aplicaraumento(self):
        self.sueldo *= 1.10
    
    def mostrardatos(self):
        print(f"Empleado: {self.nombre}")
        print(f"Sueldo mensual: ${self.sueldo:.2f}")
        print(f"Sueldo anual: ${self.sueldoanual():.2f}")
        print("------------------------")

empleado1 = Empleado("Luis Prada", 2500)
empleado2 = Empleado("Alejandro Altamirano", 3200)

print("=== Antes del aumento ===")
empleado1.mostrardatos()
empleado2.mostrardatos()

empleado1.aplicaraumento()
empleado2.aplicaraumento()

print("\n=== Después del aumento ===")
empleado1.mostrardatos()
empleado2.mostrardatos()
