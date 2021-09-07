/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package domain;

import java.util.ArrayList;


/**
 *
 * @author Antonia
 */
public class Paseo {
    private static ArrayList<Paseo> lstPaseo = new ArrayList();
    private int Id;
    private String Nombre;
    private int DistanciaMetros;

    public Paseo(int Id, String Nombre, int DistanciaMetros) {
        this.Id = Id;
        this.Nombre = Nombre;
        this.DistanciaMetros = DistanciaMetros;
    }

    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public int getDistanciaMetros() {
        return DistanciaMetros;
    }

    public void setDistanciaMetros(int DistanciaMetros) {
        this.DistanciaMetros = DistanciaMetros;
    }
    
    public static ArrayList<Paseo> verPaseosDisponibles(Paseo[] paseos, double presupuesto){
        double costo_paseo;
        Paseo paseo = new Paseo(0, null, 0);
        if (paseo.getDistanciaMetros() > 0){
        costo_paseo = paseo.getDistanciaMetros() * 375.000;
        if (costo_paseo < presupuesto){
            lstPaseo.add(paseo);
            return lstPaseo;
        }
        
        }

    }
}
