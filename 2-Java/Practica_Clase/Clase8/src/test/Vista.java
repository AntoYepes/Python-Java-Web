
package test;

import domain.Producto;
import domain.Tienda;
import java.util.Scanner;

public class Vista {
    public static int opc;
    public static Scanner teclado = new Scanner(System.in);
    public static Producto producto;
    public static Tienda tienda1;
    
    public static void main(String[] args) {
        while(true){
            System.out.println("1. Crear productos \n 2. Crear vendedor \n 3. Vender \n 4. Mostrar todas las ventas \n 5. Mostrar vendedor con mayor ventas \n 6. Mostrar ventas de un vendedor \n 7.Mostrar ventas con tarjeta de credito \n 8. Salir \n Seleccionar opcion: ");
            opc = teclado.nextInt();
            switch(opc){
                case 1:
                    carga_productos();
                    break;
                case 2:
                    break;
                case 3:
                    break;
                case 4:
                    break;
                case 5: 
                    break;
                case 6:
                    break;
                case 7:
                    break;
                case 8:
                    System.exit(0);
                default:
                    System.out.println("Error");
                    break;
            }
        }
    }
    public static void carga_productos(){
        System.out.println("Digite codigo: ");
        int codigo = teclado.nextInt();
        
        System.out.println("Ingresa descripcion del producto: ");
        String descripcion = teclado.next();
        
        System.out.println("Digite valor: ");
        Double precio = teclado.nextDouble();
        
        producto = new Producto(codigo, descripcion, precio);
        
        tienda1 = new Tienda();
        tienda1.AgregarProductos(producto);
    }
}
