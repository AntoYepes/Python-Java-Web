package domain;

public class Aseguradora {
    //ATRIBUTOS
    private int salario;
    private int diasTrabajados;
    
    //CONSTRUCTORES
    public Aseguradora(){
        
    }

    public Aseguradora(int salario, int diasTrabajados) {
        this.salario = salario;
        this.diasTrabajados = diasTrabajados;
    }
    
    // GET Y SET DE ATRIBUTOS
    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }

    public int getDiasTrabajados() {
        return diasTrabajados;
    }

    public void setDiasTrabajados(int diasTrabajados) {
        this.diasTrabajados = diasTrabajados;
    }
    
    // METODOS
    public static double liquidarPrestaciones(int salario, int diasTrabajados){
        double prima, cesantias, interes_cesantias, vacaciones, total;
        int min_doble = 908526 * 2;
        int aux_trasnp = 106454;
        int salario_dev = salario;
        
        if (salario <= min_doble){ 
            salario_dev = salario_dev + aux_trasnp;
        }
        
        prima = ((salario_dev * diasTrabajados) / 360.0);
        cesantias = ((salario_dev * diasTrabajados) / 360.0);
        interes_cesantias = (cesantias * 0.12); 
        vacaciones = ((salario * diasTrabajados) / 720.0);
        total = (prima + cesantias + interes_cesantias + vacaciones);
        return total;
    }
    
    public static double liquidarSegSocial(int salario, int diasTrabajados){
        double salud, pension, riesgosLaborales, salario_conv;
        salario_conv = (double)salario;
        salud = (salario_conv / 30) * diasTrabajados * 0.085;
        pension = (salario_conv / 30) * diasTrabajados * 0.12;
        riesgosLaborales = (salario_conv / 30) * diasTrabajados*  0.00522;
        return (salud +  pension + riesgosLaborales);

    }
}
