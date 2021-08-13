package domain;

public class Producto {
    //Atributos
    private char tamaño;
    private String color;
    private float precio;
    private String marca;
    private int cantidad;
    
    //Constructor
    public Producto(char tamaño, String color, float precio, String marca, int cantidad){
        this.tamaño = tamaño;
        this.color = color;
        this.precio = precio;
        this.marca = marca;
        this.cantidad = cantidad;
    }

    public char getTamaño() {
        return tamaño;
    }

    public String getColor() {
        return color;
    }

    public float getPrecio() {
        return precio;
    }

    public String getMarca() {
        return marca;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setTamaño(char tamaño) {
        this.tamaño = tamaño;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setPrecio(float precio) {
        this.precio = precio;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }
    
}
