package calculadora;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Calculadora2 {
    public static double sumar(double a, double b){
        return a + b;
    }
    public static double restar(double a, double b){
        return a - b;
    }
    public static double multiplicar(double a, double b){
        return a * b;
    }
    public static double dividir(double a, double b){
        return a / b;
    }
    public static double residuo(double a, double b){
        return a % b;
    }
    public static boolean esPrimo(int n){
        int divisores = 2, cont = 2;
        while (cont < n){
            if ( n % cont == 0){
                divisores++;
                break;
            }
            cont++;
        }
        return (divisores == 2);
    }
    public static void formulaEstudiante(){
        double a = ingresoDatos(), b = ingresoDatos(), c = ingresoDatos(), temp, x1, x2;
        temp = b*b-4*a*c;
        if (temp >=0){
            if (2*a != 0){
                x1 = -b - Math.sqrt(temp) / 2 * a;
                x2 = -b + Math.sqrt(temp) / 2 * a;
                System.out.println("Las raices son:");
                System.out.println("X1:" + x1);
                System.out.println("X2:" + x2);
            }
            else{
                System.out.println("Error division por cero");
            }
        }
        else{
            System.out.println("La raiz es negativa");
        }
    }
    public static double ingresoDatos(){
        Scanner ingreso = new Scanner(System.in);
        System.out.println("Ingresa el numero: ");
        double a = ingreso.nextDouble();
        return a;
    }
    
    public static void main(String[] args) {
        boolean salir = false;
        while (!salir) {
            System.out.println("1. Suma" +  "\n" + "2. Resta" + "\n" + "3. Multiplicación" + "\n"+ "4. División" +  "\n" + "5. Residuo" + "\n" + "6. No primo" + "\n" + "7.Formula Estudiante" + "\n" + "8. Salir");

            try{
                double value = ingresoDatos();
                int opcion = (int)value;
                switch(opcion){
                    case 1:
                        double a = ingresoDatos();
                        double  b = ingresoDatos();
                        double suma = sumar(a, b);
                        System.out.println("La suma es = " + suma);
                        break;
                    case 2:
                        double c = ingresoDatos();
                        double d = ingresoDatos();
                        double resta = restar(c, d);
                        System.out.println("La resta es = " + resta);
                        break;
                    case 3:
                        double e = ingresoDatos();
                        double f = ingresoDatos();
                        double multiplicacion = multiplicar(e, f);
                        System.out.println("La multiplicacion es = " + multiplicacion);
                        break;
                    case 4:
                        double g = ingresoDatos();
                        double h = ingresoDatos();
                        double division = dividir(g, h);
                        System.out.println("La division es = " + division);
                        break;
                    case 5:
                        double i = ingresoDatos();
                        double j = ingresoDatos();
                        double residuo = residuo(i, j);
                        System.out.println("El residuo es = " + residuo);
                        break;
                    case 6:
                        double x = ingresoDatos();
                        int valor = (int)x;
                        var primo = esPrimo(valor);
                        System.out.println("primo = " + primo);
                        break;
                    case 7:
                        formulaEstudiante();
                        break;
                    case 8:
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

