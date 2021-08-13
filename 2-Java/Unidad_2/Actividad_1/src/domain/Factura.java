package domain;

public class Factura {
    //Atributos
    private int noRegistro;
    private String fecha;
    private double valorTotal;
    private int noProductos;
    private double pago;
    
    //Constructor
    public Factura(int noRegistro, String fecha, double valorTotal, int noProductos, double pago){
        this.noRegistro = noRegistro;
        this.fecha = fecha;
        this.valorTotal = valorTotal;
        this.noProductos = noProductos;
        this.pago = pago;
    }
    
    // get y set
    public int getNoRegistro(){
        return noRegistro;
    }
    
    public String getFecha(){
        return fecha;
    }
    
    public double getValorTotal(){
        return valorTotal;
    }
    
    public int getNoProductos(){
        return noProductos;
    }
    
    public double getPago(){
        return pago;
    }
    
    public void setNoRegistro(int noRegistro){
        this.noRegistro = noRegistro;
    }
    
    public void setFecha(String fecha){
        this.fecha = fecha;
    }
    
    public void setValorTotal(double valorTotal ){
        this.valorTotal = valorTotal;
    }
    
    public void setProductos(int noProductos){
        this.noProductos = noProductos;
    }
    public void setPago(double pago){
        this.pago = pago;
    }
    
    public double valorTotalPagar(double valorTotal){
        double valorIva = valorTotal * 19 /100;
        double valorTotalPagar = valorIva + valorTotal;
        return valorTotalPagar;
    }
    
}
