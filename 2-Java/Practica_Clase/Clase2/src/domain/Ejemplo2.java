package domain;

import java.text.SimpleDateFormat;
import java.time.Period;
import java.util.Date;

public class Ejemplo2 {
    public static void main(String[] args) {
        
        Date fecha = new Date();
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");
        String format = formatter.format(fecha);
        System.out.println(format);
        
//        Period period = Period.between (fecha, weekLater );
//        Integer daysElapsed = period.getDays ();
    }
}
