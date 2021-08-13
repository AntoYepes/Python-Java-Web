package domain;

import java.util.Scanner;

public class Ejemplo2 {
    public static void main(String[] args) {
        Scanner dato = new Scanner(System.in);
        int dato1 = 0, dato2 = 0, resultado = 0;
        
        System.out.println("Digite num1: ");
        dato1 = dato.nextInt();
        
        System.out.println("Digite num2: ");
        dato2 = dato.nextInt();
        
        System.out.println("Suma: " + Sumar(dato1, dato2));
    }
    
    static int Sumar(int a, int b){
        return a + b;
    }
}
