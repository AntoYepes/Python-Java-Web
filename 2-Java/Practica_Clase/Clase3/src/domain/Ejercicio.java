package domain;

import java.util.Scanner;

public class Ejercicio {
    public static void main(String[] args) {
        Scanner dato_in = new Scanner(System.in);
        int edad = 0, promedio = 0;
        String nombre = "";
        
        for(int j=1; j <= 3; j++){
            System.out.println("Ingrese el nombre: ");
            nombre = dato_in.nextLine();
            System.out.println("Ingrese la edad: ");
            edad = dato_in.nextInt();
            promedio += edad;
            
        }
        System.out.println("El promedio es: " + promedio/3);
    }
    
    
    
}
