package test;

import domain.Cliente;

public class Test {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("Lia", 98,"F", 98);
        cliente.setNombre("Antonia");
        cliente.setCedula(123);
        cliente.setEdad(24);
        
        System.out.println("Nombre: " + cliente.getNombre() + "\n" + "Cedula: " + cliente.getCedula() + "\n" + "Edad: " + cliente.getEdad());
    }
    
}
