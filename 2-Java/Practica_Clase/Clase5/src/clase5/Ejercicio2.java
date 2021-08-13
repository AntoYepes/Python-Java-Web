package clase5;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int mayor = 0, menor = 0;
        System.out.println("Ingrese la cantidad de sueldos a ingresar: ");
        int tamaño = teclado.nextInt();
        int sueldo[] = new int[tamaño];
        
        System.out.println("BIENVENIDO \n");
        for (int i = 0; i < tamaño; i++) {
            System.out.println("Ingrese la cantidad: ");
            sueldo[i] = teclado.nextInt();
            if(sueldo[i] >= mayor){
                mayor = sueldo[i];
            }else{
                menor = sueldo[i];
            }
        }
        System.out.println("Termino el proceso!!!");
        System.out.println("El mayor es: " + mayor);
        System.out.println("El menor es: " + menor);
    }
}

