var modulos=["python", "Java", "Js", "Css"]
var text=""
for(i=0;i<modulos.length;i++)
{
    // alert(modulos[i])
    text+=modulos[i] + "<br>"
    document.getElementById('iterador_for').innerHTML=text

}

i=0
var num=""
while(i<10)
{
    num+="#"+i + "<br>"
    i++
    document.getElementById('iterador_while').innerHTML=num
}