/*=========================================
    PSICOLOGÍA PREMIUM
==========================================*/

document.addEventListener("DOMContentLoaded", function () {

    /*=========================================
        NAVBAR SCROLL
    ==========================================*/

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {

        if (window.scrollY > 60) {

            navbar.style.background = "#1E3A5F";
            navbar.style.padding = "10px 0";
            navbar.style.boxShadow = "0 5px 20px rgba(0,0,0,.15)";

        } else {

            navbar.style.background = "rgba(16,35,55,.65)";
            navbar.style.padding = "18px 0";
            navbar.style.boxShadow = "none";

        }

    });

    /*=========================================
        SCROLL SUAVE
    ==========================================*/

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            e.preventDefault();

            const destino = document.querySelector(this.getAttribute("href"));

            if (destino) {

                destino.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });

    /*=========================================
        ANIMACIÓN DE TARJETAS
    ==========================================*/

    const cards = document.querySelectorAll(".servicio");

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-12px) scale(1.03)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0) scale(1)";

        });

    });

    /*=========================================
        EFECTO EN IMÁGENES
    ==========================================*/

    const imagenes = document.querySelectorAll("img");

    imagenes.forEach(img => {

        img.addEventListener("mouseenter", () => {

            img.style.transform = "scale(1.03)";

        });

        img.addEventListener("mouseleave", () => {

            img.style.transform = "scale(1)";

        });

    });

    /*=========================================
        VALIDACIÓN DEL FORMULARIO
    ==========================================*/

    const formulario = document.querySelector("form");

    formulario.addEventListener("submit", function (e) {

        e.preventDefault();

        const nombre = formulario.querySelector("input:nth-child(1)").value.trim();
        const correo = formulario.querySelector("input:nth-child(2)").value.trim();
        const telefono = formulario.querySelector("input:nth-child(3)").value.trim();
        const mensaje = formulario.querySelector("textarea").value.trim();

        if (nombre === "" || correo === "" || telefono === "" || mensaje === "") {

            alert("Por favor complete todos los campos.");

            return;

        }

        const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!email.test(correo)) {

            alert("Ingrese un correo válido.");

            return;

        }

        alert("¡Gracias! Hemos recibido tu solicitud de cita.");

        formulario.reset();

    });

});


/*=========================================
    BOTÓN VOLVER ARRIBA
==========================================*/

const boton = document.createElement("button");

boton.innerHTML = "↑";

boton.id = "topButton";

document.body.appendChild(boton);

boton.style.position = "fixed";
boton.style.bottom = "100px";
boton.style.right = "25px";
boton.style.width = "50px";
boton.style.height = "50px";
boton.style.borderRadius = "50%";
boton.style.border = "none";
boton.style.background = "#1E3A5F";
boton.style.color = "white";
boton.style.fontSize = "22px";
boton.style.cursor = "pointer";
boton.style.display = "none";
boton.style.zIndex = "999";
boton.style.boxShadow = "0 8px 20px rgba(0,0,0,.25)";
boton.style.transition = ".3s";

window.addEventListener("scroll", function () {

    if (window.scrollY > 300) {

        boton.style.display = "block";

    } else {

        boton.style.display = "none";

    }

});

boton.addEventListener("click", function () {

    window.scrollTo({

        top: 0,
        behavior: "smooth"

    });

});


/*=========================================
    EFECTO DE ESCRITURA EN EL HERO
==========================================*/

const titulo = document.querySelector(".hero h1");

const texto = titulo.innerText;

titulo.innerHTML = "";

let i = 0;

function escribir() {

    if (i < texto.length) {

        titulo.innerHTML += texto.charAt(i);

        i++;

        setTimeout(escribir, 45);

    }

}

window.addEventListener("load", escribir);