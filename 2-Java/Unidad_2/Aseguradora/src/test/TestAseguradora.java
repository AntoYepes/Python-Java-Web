package test;

import domain.Aseguradora;

public class TestAseguradora {
    public static void main(String[] args) {
        Aseguradora total = new Aseguradora();
        System.out.println(total.liquidarPrestaciones(1810050, 152));
        System.out.println(total.liquidarSegSocial(1810050, 152));
    }
}
