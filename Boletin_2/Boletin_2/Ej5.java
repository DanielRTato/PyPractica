import java.util.Scanner;

public class Ej5 {
    public static void main(String[] args) {


        Scanner teclado = new Scanner(System.in);
        System.out.print("Introduce millas marinas");
        int marinas = teclado.nextInt();
        int conversion = 1852;
        System.out.println("La cantidad de millas marinas:  " + marinas * conversion + " metros");

        teclado.close();





    }
}
