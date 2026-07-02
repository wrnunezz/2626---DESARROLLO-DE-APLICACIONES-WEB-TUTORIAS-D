

const formulario= document.getElementById("formRegistro");
const mensaje = document.getElementById("mensaje");


formulario.addEventListener("submit", function(event){
 
    event.preventDefault();
    let nombre = document.getElementById("nombre").value.trim();
    let descripcion = document.getElementById("descripcion").value;
    let categoria = document.getElementById("categoria").value;
    console.log(nombre,descripcion,categoria);

    if (nombre==""){
        mensaje.innerHTML=`<div class="alert alert-danger">
    Lllene el campo 
</div>`;
    }

    mensaje.innerHTML= `<div class="alert alert-info">
    Guardado correctamente
</div>`;



});