//2. Crea una clase Empleado con nombre y sueldo
//  a) Agrega un método para calcular el sueldo anual
//  b) Agrega un método para aplicar un aumento del 10%
//  c) Crea dos empleados y muestra sus sueldos antes y después del aumento
public class Empleado {
    private String nombre;
    private double sueldo; 
    public Empleado(String nombre, double sueldo) {
        this.nombre = nombre;
        this.sueldo = sueldo;
    }
    public double SueldoAnual() {
        return sueldo * 12;
    }
    public void aplicarAumento() {
        sueldo *= 1.10;
    }
    public void mostrarDatos() {
        System.out.println("Empleado: " + nombre);
        System.out.printf("Sueldo mensual: $%.2f%n", sueldo);
        System.out.printf("Sueldo anual: $%.2f%n", SueldoAnual());
        System.out.println("------------------------");
    }    
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan Pérez", 2500);
        Empleado empleado2 = new Empleado("María García", 3200);
        
        System.out.println("=== Antes del aumento ===");
        empleado1.mostrarDatos();
        empleado2.mostrarDatos();
        
        empleado1.aplicarAumento();
        empleado2.aplicarAumento();
        
        System.out.println("\n=== Después del aumento ===");
        empleado1.mostrarDatos();
        empleado2.mostrarDatos();
    }
}
