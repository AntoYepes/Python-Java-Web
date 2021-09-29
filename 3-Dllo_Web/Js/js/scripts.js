// var num1, num2, total
//     num1 = 5
//     num2 = 9
//     total = num1 + num2

//     decimal = 2021.3
//     string_simple = 'LOVE YOU '
//     string_doble = "Hola lindoo :3 "

//     verdadero = true
//     falso = false
//     nulos = null

//     // alert(total)
    // alert(typeof verdader)
    // alert(typeof decimal)
    // alert(string_simple+ "" + string_doble )

    // document.write(string_doble)
    // document.write(string_simple)

function Nombre()
{   Nombre='Antonia'
    Apellido='Yepes'
    alert(Nombre + Apellido)
}

function Retorno_suma()
{   num1 = 5
    num2 = 9
    total = num1 + num2
    document.getElementById('parrafo_modificado').innerHTML=total
}
// alert('El resultado de la suma es: ' +  Retorno_suma())

function Borrar()
{   
    document.getElementById('parrafo_modificado').innerHTML="."

}