package domain;

import java.util.Scanner;
import domain.Banco;

public class Principal {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        Banco persona1 = null;
        
        while(true){
            System.out.println("1. Crear cuenta");
            System.out.println("2. Consignar");
            System.out.println("3. Retirar");
            System.out.println("4. Consultar saldo");
            System.out.println("5. Salir");
            
            System.out.println("Seleccione opcion: ");
            int opc = teclado.nextInt();
            
            switch(opc){
                case 1:
                    System.out.println("Numero de cuenta:");    
                    int cuenta = teclado.nextInt();
                    System.out.println("Valor a consignar para crear cuenta: ");
                    double valor = teclado.nextDouble();
                    persona1 = new Banco(valor, cuenta);
                    break;
                    
                case 2:
                    System.out.println("Digite valor a consignar:");
                    double valor1 = teclado.nextDouble();
                    persona1.setSaldoCuenta(valor1);
                    break;
                    
                case 3:
                    System.out.println("Di");
                    
                case 4:
                    System.out.println("Su saldo es: " + persona1.getSaldoCuenta());
                    break;
                           
            }
        }
        
    
    }
}
