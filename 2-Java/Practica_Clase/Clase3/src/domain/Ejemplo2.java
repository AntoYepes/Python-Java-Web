package domain;

import java.util.Scanner;

public class Ejemplo2 {
    public static void main(String[] args) {
        Scanner dato_in = new Scanner(System.in);
        int numero1;
        System.out.println("Ingrese num de 1-7");
        try{
        numero1 = dato_in.nextInt();
        
        switch(numero1){
            case 1:
                System.out.println("Domingo");
                break;
            case 2:
                System.out.println("Lunes");
                break;
            case 3:
                System.out.println("Martes");
                break;
            case 4:
                System.out.println("Miercoles");
                break;
            case 5:
                System.out.println("Jueves");
                break;
            case 6:
                System.out.println("Viernes");
                break;
            case 7:
                System.out.println("Sabado");
                break;
            default:
                System.out.println("Error");
                        
            }
        }
        catch(Exception e){
            System.out.println("Error en dato");
        }
        finally{
            dato_in.close();
        }
    }
}
