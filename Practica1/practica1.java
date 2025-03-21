import java.lang.Math;

public class Punto {
    private double x;
    private double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double[] coord_Cartesianas() {
        return new double[]{x, y};
    }

    public double[] coord_Polares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.atan2(y, x);
        return new double[]{r, theta};
    }

    @Override
    public String toString() {
        return "Punto(x=" + x + ", y=" + y + ")";
    }

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println(p);                      
        System.out.println(java.util.Arrays.toString(p.coord_Cartesianas())); 
        System.out.println(java.util.Arrays.toString(p.coord_Polares())); 
    }
}
