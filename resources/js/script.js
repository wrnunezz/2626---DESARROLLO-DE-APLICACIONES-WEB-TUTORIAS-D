function saludar() {
            alert("hola bienvenido")
        }


function mostrarResultado() {
    let nombre =document.getElementById("nombres").value;
    console.log("estoy probando " +nombre);
    document.getElementById("result").textContent= "hola que tal " + nombre + " Bienvenido";



}

function validarEdad() {

    let edad = document.getElementById("edad").value;

    if (edad > 18){

        document.getElementById("resultado").textContent= "Eres mayor de edad y tu edad es " +edad ; 
    } else {
        document.getElementById("resultado").textContent="menor de edad"
    }

}


function CalculaAnioNacimiento(){
    let edadTotal=document.getElementById("edadTotal").value
    console.log("ver que viene"+edadTotal)
    let anioActual=2026

    let anioNacio= anioActual -edadTotal

    document.getElementById("mostrarResultado").textContent= "Naciste en el año "+  anioNacio;

}