package domain;

import java.util.Scanner;
import domain.Operaciones;

public class Ejemplo1 {
    public static void main(String[] args) {
        Scanner dato = new Scanner(System.in);
        int dato1 = 0, dato2 = 0, resultado = 0;
        
        System.out.println("Digite num1: ");
        dato1 = dato.nextInt();
        
        System.out.println("Digite num2: ");
        dato2 = dato.nextInt();
        
        Operaciones operacion1 = new Operaciones(dato1, dato2);
        System.out.println("Suma: " + operacion1.Suma());
        System.out.println("Otra suma: " + operacion1.getTOTAL());
        
        operacion1.setNUMERO1(500);
        operacion1.setNUMERO2(600);
        System.out.println("Nueva suma: " + operacion1.Suma());
        
        
        System.out.println(operacion1.toString());
    }
    
}
