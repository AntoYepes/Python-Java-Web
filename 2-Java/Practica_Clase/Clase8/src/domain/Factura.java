
package domain;

import java.util.ArrayList;

public class Factura {
    private int numero;
    private Fecha fecha;
    private Vendedor vendedor;
    private FormaPago formapago;
    private ArrayList<DetalleFactura> detallefactura;
    private double totalVenta;

    public Factura(int numero, Fecha fecha, Vendedor vendedor, FormaPago formapago, ArrayList<DetalleFactura> detallefactura, double totalVenta) {
        this.numero = numero;
        this.fecha = fecha;
        this.vendedor = vendedor;
        this.formapago = formapago;
        this.detallefactura = detallefactura;
        this.totalVenta = totalVenta;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public Fecha getFecha() {
        return fecha;
    }

    public void setFecha(Fecha fecha) {
        this.fecha = fecha;
    }

    public Vendedor getVendedor() {
        return vendedor;
    }

    public void setVendedor(Vendedor vendedor) {
        this.vendedor = vendedor;
    }

    public FormaPago getFormapago() {
        return formapago;
    }

    public void setFormapago(FormaPago formapago) {
        this.formapago = formapago;
    }

    public ArrayList<DetalleFactura> getDetallefactura() {
        return detallefactura;
    }

    public void setDetallefactura(ArrayList<DetalleFactura> detallefactura) {
        this.detallefactura = detallefactura;
    }

    public double getTotalVenta() {
        return totalVenta;
    }

    public void setTotalVenta(double totalVenta) {
        this.totalVenta = totalVenta;
    }
    
    
    
}
