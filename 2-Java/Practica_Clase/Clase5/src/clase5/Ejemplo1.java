
package clase5;

import java.util.Scanner;

public class Ejemplo1 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Digite el numero de personas: ");
        int tamaño = teclado.nextInt();
        
        String nombre[] = new String[tamaño];
        int edad[] = new int[tamaño];
                
        System.out.println("¡¡¡BIENVENIDOS!!! \n");
        for (int i = 0; i < tamaño; i++) {
            System.out.println("Digite nombre: ");
            nombre[i] = teclado.next();
            System.out.println("Digite edad: ");
            edad[i] = teclado.nextInt();
        }
        System.out.println("\n Termino proceso de insertar \n");
        for (int j = (tamaño - 1); j >= 0; j--) {
            System.out.println("LOS DATOS DE POSICION [" + j + "] es Nombre: " + nombre[j] + ", Edad: " + edad[j]);
        }
    }
}
