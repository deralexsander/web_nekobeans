function validarInicioSesion() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    var emailError = document.getElementById("emailError");
    var passwordError = document.getElementById("passwordError");

    
    
    document.getElementById("email").addEventListener("input",
function() {
    document.getElementById("emailError").textContent = "";
});

document.getElementById("password").addEventListener("input",
function() {
    document.getElementById("passwordError").textContent = "";
});
   
    



var hayErrores = false;

    if (email.trim() === "") {
        emailError.textContent = "Por favor, ingresa tu correo electrónico.";
        hayErrores = true;
    } else {
        emailError.textContent = "";
    }
    if (password.trim() === "") {
        passwordError.textContent = "Por favor, ingresa tu contraseña.";
        hayErrores = true;
    } else {
        passwordError.textContent = "";
    }

    
   
    return !hayErrores; // Si todas las validaciones son exitosas, devuelve true para enviar el formulario
}




// Verificar la longitud de la contraseña
    
function validarTrabajaConNosotros() {
    var nombre = document.getElementById("nombre").value;
    var apellido1 = document.getElementById("apellido1").value;
    var apellido2 = document.getElementById("apellido2").value;
    var carnet = document.getElementById("carnet").value;
    var fecha = document.getElementById("fecha").value;

    var rutInput = document.getElementById("rut");
    var nombreError = document.getElementById("nombreError");
    var apellido1Error = document.getElementById("apellido1Error");
    var apellido2Error = document.getElementById("apellido2Error");
    var rutError = document.getElementById("rutError");
    var carnetError = document.getElementById("carnetError");
    var fechaError = document.getElementById("fechaError");

        // Verificar si la fecha está en el formato dd-mm-yyyy
    
        /*
        document.getElementById("passwordError"): 
        Esta parte del código obtiene el elemento HTML que tiene el ID "passwordError". Este elemento probablemente es un mensaje de error asociado al 
        campo de contraseña en un formulario.
        .addEventListener("input", function(){ ... }): 
        Esta línea agrega un event listener al elemento obtenido en el paso anterior. Este event listener está configurado para escuchar el evento "input",
        que se activa cada vez que se ingresa texto en el campo asociado. Cuando se dispara este evento, se ejecuta la función anónima definida dentro de los corchetes.
        function(){ document.getElementById("passwordError").textContent = ""; }: 
        Esta es la función anónima que se ejecuta cuando se dispara el evento "input". Lo que hace esta función es seleccionar nuevamente el elemento con el ID "passwordError" 
        y establecer su contenido de texto (textContent) en una cadena vacía. En otras palabras, borra el contenido de texto del elemento "passwordError".

        */

    document.getElementById("nombre").addEventListener("input", function() {
        nombreError.textContent = "";
    });

    document.getElementById("carnet").addEventListener("input", function() {
        carnetError.textContent = "";
    });

    document.getElementById("fecha").addEventListener("input", function() {
        fechaError.textContent = "";
    });

    document.getElementById("rut").addEventListener("input", function() {
        rutError.textContent = "";
        var rut = rutInput.value;
        rut = rut.replace(/\D/g, ''); // Eliminar cualquier caracter que no sea un número
        if (rut.length > 1) {
            rut = rut.substring(0, rut.length - 1) + '-' + rut.charAt(rut.length - 1);
        }
        rutInput.value = rut;

        // Validar longitud del RUT y mostrar mensaje de error si es necesario
        if (rut.length < 10) {
            rutError.textContent = "El RUT debe tener al menos 10 caracteres.";
            hayErrores = true;
        } else if (rut.length > 10) {
            rutError.textContent = "El RUT no puede tener más de 10 caracteres.";
            hayErrores = true;
        }
    });

    document.getElementById("apellido1").addEventListener("input", function() {
        apellido1Error.textContent = "";
    });

    document.getElementById("apellido2").addEventListener("input", function() {
        apellido2Error.textContent = "";
    });

    var hayErrores = false;

    if (nombre.trim() === "") {
        nombreError.textContent = "Por favor, ingrese su nombre.";
        hayErrores = true;
    }

    if (apellido1.trim() === "") {
        apellido1Error.textContent = "Por favor, ingrese su apellido paterno";
        hayErrores = true;
    }

    if (apellido2.trim() === "") {
        apellido2Error.textContent = "Por favor, ingrese su apellido materno";
        hayErrores = true;
    }

    if (rutInput.value.trim() === "") {
        rutError.textContent = "Por favor, ingrese su RUT.";
        hayErrores = true;
    } else {
        var rut = rutInput.value.replace(/\D/g, '');
    }

    if (carnet.trim() === "") {
        carnetError.textContent = "Por favor, ingrese su foto de carnet.";
        hayErrores = true;
    }

    if (!/^\d{4}-\d{2}-\d{2}$/.test(fecha)) {
        fechaError.textContent = "Por favor, ingrese su fecha de nacimiento";
        hayErrores = true;
    }

    return !hayErrores; // Devuelve true si no hay errores, false si hay al menos un error
}



function validarRegistros() {

    var emailRegistrar = document.getElementById("emailRegistrar").value;
    var usuarioRegistrar = document.getElementById("usuarioRegistrar").value;
    var passwordRegistrar = document.getElementById("passwordRegistrar").value;

    var emailRegistrarError = document.getElementById("emailRegistrarError");
    var usuarioRegistrarError = document.getElementById("usuarioRegistrarError");
    var passwordRegistrarError = document.getElementById("passwordRegistrarError");

    document.getElementById("emailRegistrar").addEventListener("input", 
    function() {
        document.getElementById("emailRegistrarError").textContent = "";
    });
    document.getElementById("usuarioRegistrar").addEventListener("input", 
    function() {
        document.getElementById("usuarioRegistrarError").textContent = "";
    });
    document.getElementById("passwordRegistrar").addEventListener("input", 
    function() {
        document.getElementById("passwordRegistrarError").textContent = "";
    });


    var hayErrores = false;


    if (emailRegistrar.trim() === "") {
        emailRegistrarError.textContent = "Por favor, ingrese su correo.";
        hayErrores = true;
    } else {
        emailRegistrarError.textContent = "";
    }

    if (usuarioRegistrar.trim() === "") {
        usuarioRegistrarError.textContent = "Por favor, ingrese su usuario.";
        hayErrores = true;
    } else {
        usuarioRegistrarError.textContent = "";
    }

    if (passwordRegistrar.trim() === "") {
        passwordRegistrarError.textContent = "Por favor, ingrese su contraseña.";
        hayErrores = true;
    } else {
        passwordRegistrarError.textContent = "";
    }
    

return !hayErrores; // Devuelve true si no hay errores, false si hay al menos un error

}


function validacionCrear() {

    var nombrePlantilla = document.getElementById("nombrePlantilla").value;
    var foto = document.getElementById("foto").value;
    var coloresPlantillas = document.getElementById("coloresPlantillas").value;

    var nombrePlantillaError = document.getElementById("nombrePlantillaError");
    var fotoError = document.getElementById("fotoError");
    var coloresPlantillasError = document.getElementById("coloresPlantillasError");

    // Agregar event listener para los botones de radio
    var btnRadios = document.querySelectorAll('input[name="btnradio2"]');
    btnRadios.forEach(function(radio) {
        radio.addEventListener("change", function() {
            document.getElementById("seleccionError").textContent = "";
        });
    });

    document.getElementById("nombrePlantilla").addEventListener("input", function() {
        nombrePlantillaError.textContent = "";
    });
    document.getElementById("foto").addEventListener("input", function() {
        fotoError.textContent = "";
    });
    document.getElementById("coloresPlantillas").addEventListener("input", function() {
        coloresPlantillasError.textContent = "";
    });

    var hayErrores = false;

    var btnRadioSeleccionado = document.querySelector('input[name="btnradio2"]:checked');
    if (!btnRadioSeleccionado) {
        document.getElementById("seleccionError").textContent = "Por favor, seleccione una opción para cómo se puede usar la plantilla.";
    }

    if (nombrePlantilla.trim() === "") {
        nombrePlantillaError.textContent = "Por favor, ingrese el nombre de la plantilla.";
        hayErrores = true;
    }

    if (foto.trim() === "") {
        fotoError.textContent = "Por favor, ingrese su archivo.";
        hayErrores = true;
    }

    if (coloresPlantillas.trim() === "") {
        coloresPlantillasError.textContent = "Por favor, ingrese su categoria.";
        hayErrores = true;
    }

    return !hayErrores;
}







