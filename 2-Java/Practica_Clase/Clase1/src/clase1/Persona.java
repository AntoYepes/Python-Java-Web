package clase1;

import java.util.Scanner;

public class Persona {
    public static void main(String[] args) {
        Scanner dato = new Scanner(System.in);
        System.out.println("Ingrese el nombre: ");
        String nombre = dato.nextLine();
  
        System.out.println("Ingrese el Documento: ");
        int numDoc = dato.nextInt();
  
        System.out.println("Ingresa el sueldo mensual: ");
        double sueldoMensual = dato.nextDouble();
      
        System.out.println("Ingresa los dias trabajados: ");
        double diasTrabajados = dato.nextDouble();
        
        double valorDia = sueldoMensual/30;
        double pagaTrabajadores = (sueldoMensual / 30) * 10;
        
        System.out.println("Nombre: " + nombre + "\n" + "Documento: " + numDoc + "\n" + "Sueldo Mensual: " + sueldoMensual + "\n " + "Dias trabajados: " + diasTrabajados + "\n" + "Valor dia: " + valorDia + "\n" + "Pago trabajador: " + pagaTrabajadores);
        
    }
}
