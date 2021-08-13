
package clase5;

import java.util.Scanner;

public class Division {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int numero1 = 0, numero2 = 0, cociente = 0, residuo = 0;
        System.out.println("Metodo Restas Division");
        System.out.println("Ingrese el primer numero: ");
        numero1 = teclado.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        numero2 = teclado.nextInt();
        if (numero1 >= numero2){
            residuo = numero1 - numero2;
            cociente++;
            numero1 -= numero2;
        }
        else{
            residuo = numero2;
        }
        System.out.println("La division es= cociente: " + cociente + ",  residuo: " + residuo );
    }   
}
