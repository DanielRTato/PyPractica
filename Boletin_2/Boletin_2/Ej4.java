import java.util.Scanner;

public class Ej4 {
    public static void main(String[] args) {

        double primero, segundo;

        Scanner teclado = new Scanner(System.in);
        System.out.print("Introduce el primer numero:");
        primero = teclado.nextDouble();
        System.out.print("Introduce el segundo numero:");
        segundo = teclado.nextDouble();

        System.out.println("El resultado de la suma es: " + (primero +segundo));
        System.out.println("El resultado de la resta es: " + (primero -segundo));
        System.out.println("El resultado de la multiplicacion es: " + (primero *segundo));
        System.out.println("El resultado de la division es: " + (primero/segundo));

        teclado.close();
    }
}
