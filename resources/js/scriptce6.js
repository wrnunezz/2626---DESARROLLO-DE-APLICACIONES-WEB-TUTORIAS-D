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
});*/

/*const campo = document.getElementById('nombre');const
mensajeError =
document.getElementById('mensajeError');campo.addEventListener('input', () => { if (campo.value.length < 3) {
mensajeError.textContent = 'El nombre es demasiado corto'; } else {
mensajeError.textContent = ''; // Limpiar el mensaje si la validación es
exitosa }});*/
/*

const correoInput = document.getElementById('correo');
const mensajeError = document.getElementById('mensajeError');
correoInput.addEventListener('input', () => {
const correo = correoInput.value;
const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!regex.test(correo)) {
mensajeError.textContent = 'Correo inválido';
} else {
mensajeError.textContent = ''; // Limpiar mensaje de error si el correo es válido
}
});*/

const contraseñaInput = document.getElementById('contraseña');
const mensajeError = document.getElementById('mensajeError');
contraseñaInput.addEventListener('input', () => {
const contraseña = contraseñaInput.value;
// Verificar longitud mínima de 8 caracteres
if (contraseña.length < 8) {
mensajeError.textContent = 'La contraseña debe tener al menos 8 caracteres';
}
// Verificar si contiene caracteres especiales
else if (!/[!@#$%^&*(),.?":{}|<>]/.test(contraseña)) {
mensajeError.textContent = 'La contraseña debe incluir al menos un carácter especial';
}
else {
mensajeError.textContent = ''; // Limpiar mensaje de error si la contraseña es válida
}
});