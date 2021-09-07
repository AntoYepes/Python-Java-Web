/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Flia Barón Quimbaya
 */

import java.util.ArrayList;
import java.util.Arrays;

public class Paseo {
    private ArrayList<Paseo> lstPaseo = new ArrayList();
    private int Id;
    private String Nombre;
    private int DistanciaMetros;
    
    public Paseo(int _Id, String _Nombre, int _DistanciaMetros) {
        this.Id = Id;
        this.Nombre = Nombre;
        this.DistanciaMetros = DistanciaMetros;
                
    }
    
    public int getId() {
        return Id;        
    }
  
    public String getNombre() {
        return Nombre;
    }
    
    public int getDistanciaMetros() {
        return DistanciaMetros;
    }
    
    public void setDistanciaMetros(int DistanciaMetros) {
        this.DistanciaMetros = DistanciaMetros;
    }
    
    public static ArrayList<Paseo> VerPaseosDisponibles(Paseo[] paseos, double presupuesto) {
        double presupuesto;
        
        double CostoPaseo = 0;
        Paseo paseo = new Paseo(0, null, 0);
        
        if (paseos != null){
            for (Paseo p: paseos)
            {
                if (p != null) {
                    if(p.DistanciaMetros > 0)
                    {
                    CostoPaseo = ((p.getDistanciaMetros()/1000)) * 375000);
                    if (CostoPaseo < presupuesto )
                    {
                        paseo.setId(p.Id);
                        paseo.setNombre(p.Nombre);
                        paseo.SetDistanciaMetros(p.Distancia)Metros);
                        lstPaseo.add(paseo);
                    }
                    }
                }
                else {
                    return lstPaseo;
                }
            }    
                
        }
        else {
            return lstPaseo;
        }
        return lstPaseo;
    }
    public static void main(String []args) {
        
        Paseo p1 = new Paseo(1, "Caso 1", 10000);
        Paseo p2 = new Paseo( 2, "Caso 2", 1500);
        Paseo p3 = new Paseo(3, "Caso 3", 0);
        
        Paseo[] obj = new Paseo[3];
        obj[0] = p1;
        obj[1] = p2;


    }
    
    
        
  
    
}
