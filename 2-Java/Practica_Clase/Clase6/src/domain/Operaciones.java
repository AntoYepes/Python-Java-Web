package domain;

public class Operaciones {
    //ATRIBUTOS
    private int NUMERO1;
    private int NUMERO2;
    private int TOTAL;
    
    //CONSTRUCTOR
    public Operaciones(int NUMERO1, int NUMERO2) {
        this.NUMERO1 = NUMERO1;
        this.NUMERO2 = NUMERO2;
        this.TOTAL = 0;
    }
    
    //METODOS GET Y SET

    public int getNUMERO1() {
        return NUMERO1;
    }

    public void setNUMERO1(int NUMERO1) {
        this.NUMERO1 = NUMERO1;
    }

    public int getNUMERO2() {
        return NUMERO2;
    }

    public void setNUMERO2(int NUMERO2) {
        this.NUMERO2 = NUMERO2;
    }

    public int getTOTAL() {
        return TOTAL;
    }

    public void setTOTAL(int TOTAL) {
        this.TOTAL = TOTAL;
    }
    
    //METODO PARA LA OPERACION
    public int Suma(){
        this.TOTAL =  this.NUMERO1 + this.NUMERO2;
        return this.TOTAL;
    }

    @Override
    public String toString() {
        return "Operaciones{" + "TOTAL=" + TOTAL + '}';
    }
    
}
