
import java.util.ArrayList;

public class Aseguradora {
    // ATRIBUTOS
    private ArrayList<Empleado> empleados = new ArrayList<>();

    // CONSTRUCTOR
    public Aseguradora() {
//        this.empleados = new ArrayList<>();
    }
    
    // GET AND SET
    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }
    
    // METODOS
    public static double liquidarPrestaciones(Empleado empleado, int diasTrabajados){
        double prima, cesantias, interes_cesantias, vacaciones, total, salario, salario_dev;
        int min_doble = 908526 * 2;
        int aux_trasnp = 106454;
        salario = (double)empleado.getSalario();
        salario_dev = salario;
        
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
    
    public static double liquidarSegSocial(Empleado empleado, int diasTrabajados){
        double salud, pension, riesgosLaborales, salario_conv;
        salario_conv = (double)empleado.getSalario();
        salud = (salario_conv / 30) * diasTrabajados * 0.085;
        pension = (salario_conv / 30) * diasTrabajados * 0.12;
        riesgosLaborales = (salario_conv / 30) * diasTrabajados*  0.00522;
        return (salud +  pension + riesgosLaborales);
    }
    
    public static double liquidarNomina(Empleado empleado, int diasTrabajados){
        double salario, salario_dev, salud, pension;
        double min_doble = 908526 * 2;
        double aux_trasnp = 106454;
        salario = (double)empleado.getSalario();
        salario_dev = salario;
       
        if (1810050 <= min_doble){ 
            salario_dev = salario_dev + aux_trasnp;
        }
        salud = ((salario / 30) * diasTrabajados) * 0.04;
        pension = ((salario / 30) * diasTrabajados) * 0.04;
        return (((salario_dev / 30) * diasTrabajados) - salud - pension);
        
    }
    
    public static double liquidarParafiscales(Empleado empleado, int diasTrabajados){
        double salario_dev, compens_flia, icbf, sena;
        salario_dev = (double)empleado.getSalario();
        compens_flia = (((salario_dev / 30) * diasTrabajados) * 0.04);
        icbf = (((salario_dev/ 30) * diasTrabajados) * 0.03);
        sena = (((salario_dev / 30) * diasTrabajados) * 0.02);
        return (compens_flia + icbf + sena);
    }
    
    
}
