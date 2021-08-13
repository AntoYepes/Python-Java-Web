package domain;

import java.util.Scanner;

public class Ejercicio2 {
    public static String[] genero = new String[4];
    public static int[] edad = new int[4];
    
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int contadorMasc = 0, contadorFemenino = 0, contadorOtros = 0, sumaEdad = 0;
        double promedioEdad = 0;
        for (int i = 0; i < genero.length-1; i++) {
            System.out.println("Ingrese el genero de la persona" + (i + 1) + "(M o F): ");
            genero[i] = teclado.next();
            System.out.println("Ingrese la edad de la persona " + (i + 1) + ": ");
            edad[i] = teclado.nextInt();
            sumaEdad += edad[i];
            if (genero[i].equals("F")){
                contadorFemenino += 1;
            }else if (genero[i].equals("M")){
                contadorMasc += 1;
            }else{
                contadorOtros += 1;
            }
        
        }
        promedioEdad = sumaEdad / genero.length;
        System.out.println("El promedio es: " + promedioEdad);
        System.out.println("Femenino: " + contadorFemenino + "Maculino: " + contadorMasc + "Otros:" + contadorOtros);
    }
}
