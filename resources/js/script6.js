/*const emailInput = document.getElementById("email");
const feedback = document.getElementById("feedback");
emailInput.addEventListener("input", () => {
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (emailPattern.test(emailInput.value)) {
feedback.textContent = "Correo válido";
feedback.style.color = "green";
} else {
feedback.textContent = "Correo no válido";
feedback.style.color = "red";
}
})*/
/*
const campo = document.getElementById('nombre');
const mensajeError = document.getElementById('mensajeError');campo.addEventListener('input', () => { if (campo.value.length < 5) {
mensajeError.textContent = 'El nombre es demasiado corto'; } else {
mensajeError.textContent = ''; // Limpiar el mensaje si la validación es
exitosa }});
*/
const form =document.getElementById("formContraseña");
const contraseñaInput = document.getElementById('contraseña');
const repetirInput = document.getElementById('repetircontraseña');
const mensajeError = document.getElementById('mensajeError');

function validarContraseña(){
    mensajeError.style.color="red";
    const contraseña= contraseñaInput.value;
    const repetir=repetirInput.value;

    if (contraseña.length < 8) {
    mensajeError.textContent = 'La contraseña debe tener al menos 8 caracteres';
    return false;
    }

    if (!/[!@#$%^&*(),.?":{}|<>]/.test(contraseña)) {
    mensajeError.textContent = 'La contraseña debe incluir al menos un carácter especial';
    return false;
    }
    console.log(contraseña);
    console.log(repetir);
    if (contraseña !== repetir){
        mensajeError.textContent = 'Las contraseñas no Coinciden';
        return false;
    }

    mensajeError.style.color="green";
    mensajeError.textContent="Contraseña Valida";
    return true;

}

/**  evento  */
contraseñaInput.addEventListener('input', validarContraseña);
repetirInput.addEventListener("input",validarContraseña);

form.addEventListener("submit",function(event){
    event.preventDefault();
    if (validarContraseña()){
        alert("Formulario enviado correctamente")
    }
});
