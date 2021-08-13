package domain;

import java.util.Scanner;

public class Ejemplo3 {
    public static void main(String[] args) {
        //Operador ternario
        String estado = "";
        Scanner dato_in = new Scanner(System.in);
        int edad = 0;
        
        System.out.println("Digite su edad");
        edad = dato_in.nextInt();
        estado = (edad >= 18) ? "Mayor de edad" : "Menor de edad";
        System.out.println("estado = " + estado);
    }
}
