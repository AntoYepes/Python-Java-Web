package calculadora;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Calculadora {
    public static double ingresoDatos(){
        Scanner ingreso = new Scanner(System.in);
        System.out.println("Ingresa el numero: ");
        double a = ingreso.nextDouble();
        return a;
    }
    public static void main(String[] args) {
        // TODO code application logic here
        boolean salir = false;
        while (!salir) {
            System.out.println("1. Suma" +  "\n" + "2. Resta" + "\n" + "3. Multiplicación" + "\n"+ "4. División" +  "\n" + "5. Residuo" + "\n" + "6. Salir");

            try{
                double value = ingresoDatos();
                int opcion = (int)value;
                switch(opcion){
                    case 1:
                        double a = ingresoDatos();
                        double  b = ingresoDatos();
                        double suma = a + b;
                        System.out.println("La suma es = " + suma);
                        break;
                    case 2:
                        double c = ingresoDatos();
                        double d = ingresoDatos();
                        double resta = c - d;
                        System.out.println("La resta es = " + resta);
                        break;
                    case 3:
                        double e = ingresoDatos();
                        double f = ingresoDatos();
                        double multiplicacion = e * f;
                        System.out.println("La multiplicacion es = " + multiplicacion);
                        break;
                    case 4:
                        double g = ingresoDatos();
                        double h = ingresoDatos();
                        double division = g / h;
                        System.out.println("La division es = " + division);
                        break;
                    case 5:
                        double i = ingresoDatos();
                        double j = ingresoDatos();
                        double residuo = i % j;
                        System.out.println("El residuo es = " + residuo);
                        break;
                    case 6:
                        salir = true;
                        break;
                    default:
                        break;
                        
                }
            } catch (InputMismatchException e){
                System.out.println("Error, Ingresa un número ");
            }
        }
    }
}
