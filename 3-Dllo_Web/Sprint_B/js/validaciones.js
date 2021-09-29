function validar_nombreUsuario(string)
{
    var myRegxp = /^([a-zA-Z0-9_-]){3,9}$/
    usuario = document.getElementById('in_usuario').value
    if(myRegxp.test(usuario) == false)
    {return false}
    else
    {return true}

    // if(usuario.search(myRegxp))
    // {return false}
    
}



function validar_contrasena(string)
{
    var myRegxp = /^([a-zA-Z0-9]){6,}$/
    contrasena = document.getElementById('in_contrasena').value
    if(myRegxp.test(contrasena) == false)
    {return false}
    else
    {{return true}}
}

module.exports.validar_nombreUsuario = validar_nombreUsuario
module.exports.validar_contrasena = validar_contrasena



