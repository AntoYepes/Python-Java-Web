
package domain;

import java.util.ArrayList;

public class Tienda {
    private int nit;
    private String nombre;
    private ArrayList<Producto> listaProducto;
    private ArrayList<Vendedor> listaVendedor;
    private ArrayList<Factura> listaFactura;
    private ArrayList<FormaPago> listaFormaPago;
    
    
    public Tienda(){
        this.listaProducto = new ArrayList<Producto>();
        this.listaVendedor = new ArrayList<Vendedor>();
        this.listaFactura = new ArrayList<Factura>();
        this.listaFormaPago = new ArrayList<FormaPago>(); 
    }

    public Tienda(int nit, String nombre, ArrayList<Producto> listaProducto, ArrayList<Vendedor> listaVendedor, ArrayList<Factura> listaFactura, ArrayList<FormaPago> listaFormaPago) {
        this.nit = nit;
        this.nombre = nombre;
        this.listaProducto = listaProducto;
        this.listaVendedor = listaVendedor;
        this.listaFactura = listaFactura;
        this.listaFormaPago = listaFormaPago;
    }

    public void AgregarProductos(Producto pro){
        listaProducto.add(pro);
    }
    
    public int getNit() {
        return nit;
    }

    public void setNit(int nit) {
        this.nit = nit;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public ArrayList<Producto> getListaProducto() {
        return listaProducto;
    }

    public void setListaProducto(ArrayList<Producto> listaProducto) {
        this.listaProducto = listaProducto;
    }

    public ArrayList<Vendedor> getListaVendedor() {
        return listaVendedor;
    }

    public void setListaVendedor(ArrayList<Vendedor> listaVendedor) {
        this.listaVendedor = listaVendedor;
    }

    public ArrayList<Factura> getListaFactura() {
        return listaFactura;
    }

    public void setListaFactura(ArrayList<Factura> listaFactura) {
        this.listaFactura = listaFactura;
    }

    public ArrayList<FormaPago> getListaFormaPago() {
        return listaFormaPago;
    }

    public void setListaFormaPago(ArrayList<FormaPago> listaFormaPago) {
        this.listaFormaPago = listaFormaPago;
    }
    
    
}
