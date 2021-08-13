package domain;

import static domain.Ejemplo2.Sumar;
import java.util.Scanner;

public class Ejemplo3 {
    //Atributos
    public static int dato1 = 0;
    public static int dato2= 0;
    
    static int Sumar(){
        return dato1 + dato2;
    }
    
    public static void main(String[] args) {
        Scanner dato = new Scanner(System.in);
        
        System.out.println("Digite num1: ");
        dato1 = dato.nextInt();
        
        System.out.println("Digite num2: ");
        dato2 = dato.nextInt();
        
        System.out.println("Suma: " + Sumar());
    }
}
