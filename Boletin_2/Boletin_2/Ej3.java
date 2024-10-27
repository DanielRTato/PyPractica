import java.util.Scanner;

public class Ej3 {
    public static void main(String[] args) {

        double cambio, euros, dolares;
        Scanner entradaTeclado;
        entradaTeclado = new Scanner(System.in);
        System.out.println("Rate de cambio?");
        cambio = entradaTeclado.nextDouble();
        System.out.println("Cantidad de euros? ");
        euros = entradaTeclado.nextDouble();
        dolares = euros / cambio;
        System.out.println(dolares + " Dolares de cambio, por " + euros + " Euros.");






    }
}
