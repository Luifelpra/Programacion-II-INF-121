//3. Crea una clase Coche con marca, modelo y velocidad
//    a)Agrega un método acelerar () que aumente la velocidad en 10
//    b)Agrega un método frenar () que disminuya la velocidad en 5
//    c)Crea dos coches, aceléralos, frénalos y muestra sus velocidadesclass Coche:
public class Coche {
    private String marca;
    private String modelo;
    private int velocidad;
    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = 0;
    }
    public void acelerar() {
        velocidad += 10;
    }
    public void frenar() {
        velocidad = Math.max(0, velocidad - 5);
    }
    public void mostrarVelocidad() {
        System.out.printf("%s %s: Velocidad actual = %d km/h%n", marca, modelo, velocidad);
    }
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Ford", "Mustang");
        
      
        coche1.acelerar();
        coche2.acelerar();
        coche2.acelerar(); 
        
        coche1.frenar();
        coche2.frenar();
        
        coche1.mostrarVelocidad();
        coche2.mostrarVelocidad();
    }
}
