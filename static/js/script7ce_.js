document.addEventListener("DOMContentLoaded", function () {

    const navbar = document.querySelector("#navbarPrincipal");
    const topButton = document.querySelector("#topButton");
    const formulario = document.querySelector("#formularioContacto");

    /* =========================================
       ANIMACIONES AOS
    ========================================== */

    if (typeof AOS !== "undefined") {

        AOS.init({

            duration: 850,
            once: true,
            offset: 80

        });

    }

    /* =========================================
       NAVBAR Y BOTÓN VOLVER ARRIBA
    ========================================== */

    function actualizarScroll() {

        if (navbar) {

            navbar.classList.toggle(
                "scrolled",
                window.scrollY > 60
            );

        }

        if (topButton) {

            topButton.style.display =
                window.scrollY > 400
                    ? "block"
                    : "none";

        }

    }

    window.addEventListener(
        "scroll",
        actualizarScroll
    );

    actualizarScroll();

    /* =========================================
       SCROLL SUAVE
    ========================================== */

    document
        .querySelectorAll('a[href^="#"]')
        .forEach(function (enlace) {

            enlace.addEventListener(
                "click",
                function (event) {

                    const selector =
                        enlace.getAttribute("href");

                    if (
                        !selector ||
                        selector === "#"
                    ) {

                        return;

                    }

                    const destino =
                        document.querySelector(selector);

                    if (destino) {

                        event.preventDefault();

                        destino.scrollIntoView({

                            behavior: "smooth",
                            block: "start"

                        });

                        const menu =
                            document.querySelector(
                                "#menuPrincipal"
                            );

                        if (
                            menu &&
                            menu.classList.contains("show")
                        ) {

                            bootstrap.Collapse
                                .getOrCreateInstance(menu)
                                .hide();

                        }

                    }

                }
            );

        });

    /* =========================================
       BOTÓN VOLVER ARRIBA
    ========================================== */

    if (topButton) {

        topButton.addEventListener(
            "click",
            function () {

                window.scrollTo({

                    top: 0,
                    behavior: "smooth"

                });

            }
        );

    }

    /* =========================================
       VALIDACIÓN DEL FORMULARIO
    ========================================== */

    if (formulario) {

        formulario.addEventListener(
            "submit",
            function (event) {

                event.preventDefault();

                const nombre =
                    document
                        .querySelector("#nombre")
                        .value
                        .trim();

                const correo =
                    document
                        .querySelector("#correo")
                        .value
                        .trim();

                const telefono =
                    document
                        .querySelector("#telefono")
                        .value
                        .trim();

                const asunto =
                    document
                        .querySelector("#asunto")
                        .value;

                const mensaje =
                    document
                        .querySelector("#mensaje")
                        .value
                        .trim();

                if (
                    !nombre ||
                    !correo ||
                    !telefono ||
                    !asunto ||
                    !mensaje
                ) {

                    alert(
                        "Por favor, complete todos los campos."
                    );

                    return;

                }

                const correoValido =
                    /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

                if (!correoValido.test(correo)) {

                    alert(
                        "Ingrese un correo electrónico válido."
                    );

                    return;

                }

                alert(

                    "Gracias, " +
                    nombre +
                    ". Hemos recibido su solicitud de " +
                    asunto.toLowerCase() +
                    "."

                );

                formulario.reset();

            }
        );

    }

});