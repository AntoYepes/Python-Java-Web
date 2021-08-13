package domain;

import java.util.Scanner;

public class Clase2 {
    public static void main(String[] args) {
        // PRIORIDADES
        //1- not
        //2- and
        //3- or
        String genero = "";
        System.out.println("Ingrese el genero M o H");
        Scanner dato_in = new Scanner(System.in);
        genero = dato_in.nextLine();
        if (genero.equals("M")){
            System.out.println("Sexo " + genero);
        }
        else{
            System.out.println("Sexo " + genero);
        }
    }
}

