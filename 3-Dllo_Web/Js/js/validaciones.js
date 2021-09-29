function validar_campos()
{
    var nombre=document.getElementById('txt_nombre').value
    var apellido=document.getElementById('txt_apellido').value
    // alt 94
    var patron=/^[A-Z]*$/
    if(nombre.search(patron))
    {
        alert('Solo caracteres en mayuscula')
    }
    if(apellido.search(patron))
    {
        alert('Solo caracteres en mayuscula')
    }
}