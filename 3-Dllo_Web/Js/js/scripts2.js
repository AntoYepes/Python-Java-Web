function sumar_desdeForm()
{
    var n1, n2, suma;
    n1=parseInt(document.getElementById('txt1').value)
    n2=parseInt(document.getElementById('txt2').value)
    suma=n1+n2
    document.getElementById('resultado').value=suma

}

function datos()
{
    nombre=document.getElementById('txt_nombre').value
    apellido=document.getElementById('txt_apellido').value
    document.getElementById('p1').innerHTML="Bienvenido " + nombre + " " + apellido
}

function Datos_personales()
{
    sexo_m=document.getElementById('sexo_m').checked
    sexo_f=document.getElementById('sexo_f').checked


    if(sexo_m)
    {alert("es Hombre")}
    else
    {alert("es Mujer")}

    if(sexo_m)
    {alert("es Hombre")}
    else
    {
        if(sexo_F)
        {alert("es Mujer")}
    }
}

function dia_semana(){
var dia=parseInt(document.getElementById('dia').value);
switch(dia)
{
    case 1:
        alert('Domingo')
        break;
    case 2:
        alert('Lunes')
        break;
    case 3:
        alert('Martes')
        break;
    case 4:
        alert('Miercoles')
        break;
    case 5:
        alert('Jueves')
        break;
    case 6:
        alert('Viernes')
        break;
    case 7:
        alert('Sabado')
        break;
    default:
        alert('Dia no contemplado')
        break;
    }
}
