
package domain;

import java.util.Scanner;

public class Ejemplo3 {
    public static void main(String[] args) {
        Scanner datos = new Scanner(System.in);
        int[] edad = new int[3];
        int numero = 0;
        
        while (numero <= 2){
            System.out.println("Digite su edad: ");
            edad[numero] = datos.nextInt();
            numero = numero + 1;
            
        }
        System.out.println("Termino");
        for (numero = 0; numero  <= 2; numero++) {
            System.out.println("Las edades son: " + edad[numero]);
            
        }
    }
}
