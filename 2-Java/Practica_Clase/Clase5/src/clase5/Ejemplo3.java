package clase5;

import java.util.Scanner;

public class Ejemplo3 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese el numero de columnas: ");
        int tamaño = teclado.nextInt();
        
        int[][] datos = new int[tamaño][tamaño];
        for (int f = 0; f < tamaño; f++) {
            for (int c = 0; c < tamaño; c++) {
                System.out.println("Ingrese los datos para posicion [" + f + ", " + c + "]");
                datos[f][c] = teclado.nextInt();
            }
        }
        System.out.println("\n Termino el proceso de cargue de datos!");
        for (int i = 0; i < tamaño; i++) {
            for (int j = 0; j < tamaño; j++) {
                System.out.println("Matriz: " + datos[i][j]);
                
            }
            
        }
    }
}
