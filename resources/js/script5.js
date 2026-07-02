function cambiaMensaje(){

    document.getElementById("titulo").innerHTML="Cambia por esto ";
}


function saludame(){
    let nombre = document.getElementById("nombre").value;

    console.log(nombre);

    document.getElementById("mensaje").innerHTML="hola Bienvenido "+nombre;

}