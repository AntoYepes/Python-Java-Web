package domain;

import java.util.Scanner;

public class Ejemplo1 {
    // Sentencias de control
    public static void main(String[] args) {
        Scanner dato_in = new Scanner(System.in);
        
        //Defino 2 variables
        int numero1, numero2;
        //Inicializo los numeros
        numero1 = 0;
        numero2 = 0;
        
        System.out.println("Digite numero1: ");
        numero1 = dato_in.nextInt();
        System.out.println("Digite numero2: ");
        numero2 = dato_in.nextInt();
        
        if (numero1 > numero2){
            System.out.println("El numero " + numero1 +  "es mayor que " + numero2);
        }
        else if(numero1 == numero2){
                System.out.println("El numero " + numero1 + " es igual a " + numero2);
        }
        else if(numero1 < numero2){
            System.out.println("El numero " + numero1 + " es menor que " + numero2);
        }
    }
}

