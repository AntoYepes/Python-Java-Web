
public class Aseguradora {
    
    public static double liquidarPrestaciones(int salario, int diasTrabajados){
        double prima, cesantias, interes_cesantias, vacaciones, totalPagar;
        
        prima = ((salario * diasTrabajados) / 360);
        cesantias = ((salario * diasTrabajados) / 360);
        interes_cesantias = cesantias * 0.12; 
        vacaciones = ((salario * diasTrabajados) / 720);
        totalPagar = Math.ceil(prima + cesantias + interes_cesantias + vacaciones);
        
        return totalPagar;
    }

}
