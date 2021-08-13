package domain;

import java.util.Scanner;

public class Array {

    public static int i, j;

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int[] datos = new int[3];
        int largo = datos.length;
        System.out.print("\nTotal posiciones de vector datos: " + largo);
        for (i = 0; i <= 2; i++) {    // i++  =   i = i + 1

            System.out.print("ingresar datos al vector posicion: [" + i + "] : ");
            datos[i] = teclado.nextInt();
        }
        System.out.println("\n Termino el Cargue de Información !!!!! ");

        for (j = 0; j < datos.length; j++) {
            System.out.println("La información Posicion [" + j + "] :" + datos[j]);
        }
    }
}
