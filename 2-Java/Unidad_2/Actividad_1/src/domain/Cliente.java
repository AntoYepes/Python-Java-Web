package domain;

public class Cliente {
    //Atributos
    private String nombre;
    private int cedula;
    private String sexo;
    private int edad;
    
    //Constructor
    public Cliente(String nombre, int cedula, String sexo, int edad){
        this.nombre = nombre;
        this.cedula = cedula;
        this.sexo = sexo;
        this.edad = edad;
 
    }

    public Cliente() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    public String getNombre() {
        return nombre;
    }

    public int getCedula() {
        return cedula;
    }

    public String getSexo() {
        return sexo;
    }

    public int getEdad() {
        return edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCedula(int cedula) {
        this.cedula = cedula;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    public String comprar(){
        return "Comprar";
    }
    
    public String loliar(){
        return "Ha visitado el Centro Comercial";
    }
}
