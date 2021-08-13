package clase5;

import java.util.Scanner;
public class Clase5 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int numero1 = 0, numero2 = 0, resultado = 0;
        System.out.println("Metodo de sumas");
        System.out.println("Ingrese el primero numero a evaluar por mertodo de sumas: ");
        numero1 = teclado.nextInt();
        System.out.println("Ingrese el segundo numero a evaluar por metodo de sumas: ");
        numero2 = teclado.nextInt();
        for (int i = 0; i < numero1; i++) {
            resultado += numero2;
            
        }
        System.out.println("Resultado: " + resultado);
        teclado.close();
    }
    
}
