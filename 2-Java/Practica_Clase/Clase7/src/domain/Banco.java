package domain;

public class Banco {
    //ATRIBUTOS
    private double saldoCuenta;
    private final int numCuenta;
    private boolean estado;
    
    //CONSTRUCTOR - SOBRECARGA
    public Banco(double saldoCuenta, int numCuenta) {
        this.saldoCuenta = saldoCuenta;
        this.numCuenta = numCuenta;
        this.estado = false;
    }

//    public Banco(double saldoCuenta) {
//        this.saldoCuenta = saldoCuenta;
//    }
//    
//    public Banco(){
//        
//    }
    
    // GET Y SET
    public double getSaldoCuenta() {
        return saldoCuenta;
    }

    public void setSaldoCuenta(double saldoCuenta) {
        this.saldoCuenta = this.saldoCuenta + saldoCuenta;
    }

    public int getNumCuenta() {
        return numCuenta;
    }
  
    //METODO
    public boolean retiros(double valorRetirar){
        if (valorRetirar <= this.saldoCuenta){
            this.saldoCuenta = this.saldoCuenta - valorRetirar;
            estado = true;
            return estado;
        }
        else{
            return estado;
        }

    }
    // TO STRING
    @Override
    public String toString() {
        return "Banco{" + "saldoCuenta=" + saldoCuenta + ", numCuenta=" + numCuenta + '}';
    }
    
    
    
    
}
