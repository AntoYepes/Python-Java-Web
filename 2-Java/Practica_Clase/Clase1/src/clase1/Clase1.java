package clase1;

//import java.util.Scanner;
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
import javax.swing.JOptionPane;

public class Clase1 {

    public static void main(String[] args) {
        // IMPUTS y OUTPUTS
        //Crea un objt tipo Scanner
//        Scanner dato = new Scanner(System.in);
//        // Se realiza el ingreso de datos
//        System.out.println("Digite dato: ");
//        int number = dato.nextInt();
//        //Se realiza salida de Datos
//        System.out.println("El numero ingresado es: " + number);
        //.nextByte()
        //.nextShort()
        //.nextInt()
        //.nextLong()
        //.nextFloat()
        //.nextDouble()
        //.nextBoolean()
        //.nextLine()
        //.next()
    
//        BufferedReader dato = new BufferedReader(new InputStreamReader(System.in));
//        System.out.println("Digite su nombre: ");
//        String nombre = dato.readLine();
//        System.out.println("Bienvenid@: = " + nombre);
// 
//        System.out.println("Ingresa cadena: ");

//        BufferedReader dato = new BufferedReader(new InputStreamReader(System.in));
//        String valor = "";
//        int numero1 = 0;
//        try{
//            System.out.println("Digite el Numero: ");
//            valor = dato.readLine();
//            numero1 = Integer.parseInt(valor);
//            numero1 = numero1 + 100;
//            System.out.println("El resultado es: " + numero1);
//    }
//        catch(IOException | NumberFormatException mi_error){
//            System.out.println("Error" + mi_error.getMessage());

        //JOptionPane
        String valor = "";
        int numero = 0;
        valor = JOptionPane.showInputDialog("Digite su Nombre: ");
        numero = Integer.parseInt(valor);
        JOptionPane.showMessageDialog(null, "El resultado es: " + valor);
    }
}



