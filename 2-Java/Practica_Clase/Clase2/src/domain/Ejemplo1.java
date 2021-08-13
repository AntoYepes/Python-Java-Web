package domain;

import java.util.Scanner;

public class Ejemplo1 {
    // dar en numero 1-7 y decir el dia de la semana
    public static void main(String[] args) {
        System.out.println("Ingrese un numero: ");
        Scanner dato_in = new Scanner(System.in);
   
        try
        {
            int numero = dato_in.nextInt();
            
            if(numero == 1){
                System.out.println("Domingo");
            }
            else if(numero == 2){
                System.out.println("Lunes");
            }
            else if(numero == 3){
                System.out.println("Martes");
            }
            else if(numero == 4){
                System.out.println("Miercoles");
            }
            else if(numero == 5){
                System.out.println("Jueves");
            }
            else if(numero == 6){
                System.out.println("Viernes");
            }
            else if(numero == 7){
                System.out.println("Sabado");
            }
            else{
                System.out.println("Error");
            }
        }
    catch(Exception e){
        System.out.println("Ingrese un numero del 1-7!");
    }     
    }
}
