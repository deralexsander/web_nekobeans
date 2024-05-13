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
    var categoriasSelect = document.getElementById("categoriasSelect").value;
  
    var rutInput = document.getElementById("rut");
    var nombreError = document.getElementById("nombreError");
    var apellido1Error = document.getElementById("apellido1Error");
    var apellido2Error = document.getElementById("apellido2Error");
    var rutError = document.getElementById("rutError");
    var carnetError = document.getElementById("carnetError");
    var fechaError = document.getElementById("fechaError");
    var categoriasSelectError = document.getElementById("categoriasSelectError");



   
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

        document.getElementById("categoriasSelect").addEventListener("input", function() {
            categoriasSelectError.textContent = "";
        });


    document.getElementById("nombre").addEventListener("input", function() {
        nombreError.textContent = "";
    });

    document.getElementById("carnet").addEventListener("input", function() {
        carnetError.textContent = "";
    });

    document.getElementById("categoriasSelect").addEventListener("input", function() {
        categoriasSelectError.textContent = "";
    });

    document.getElementById("fecha").addEventListener("input", function() {
        fechaError.textContent = "";
    });

    document.getElementById("rut").addEventListener("input", function() {
        rutError.textContent = "";
        

    // Validar longitud del RUT y mostrar mensaje de error si es necesario
        
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

    
    var rut = rutInput.value.replace(/\D/g, '');
    var rut = rutInput.value;
    if (rutInput.value.trim() === "") {
        rutError.textContent = "Por favor, ingrese su RUT.";
        hayErrores = true;
    } else if (rut.length < 10) {
        rutError.textContent = "El RUT debe tener al menos 10 caracteres.";
        hayErrores = true;
    } else if (rut.length > 12) {
        rutError.textContent = "El RUT no puede tener más de 12 caracteres.";
        hayErrores = true;
    }

    if (carnet.trim() === "") {
        carnetError.textContent = "Por favor, ingrese su foto de carnet.";
        hayErrores = true;
    }

    if (!/^\d{4}-\d{2}-\d{2}$/.test(fecha)) {
        fechaError.textContent = "Por favor, ingrese su fecha de nacimiento";
        hayErrores = true;
    }

    if (categoriasSelect.trim() === "") {
        categoriasSelectError.textContent = "Por favor, seleccione una región.";
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



function validacionCrear () {

    var nombrePlantilla = document.getElementById("nombrePlantilla").value;
    var foto = document.getElementById("foto").value;
    var coloresPlantillas = document.getElementById("coloresPlantillas").value;
    


    var nombrePlantillaError = document.getElementById("nombrePlantillaError");
    var fotoError = document.getElementById("fotoError");
    var coloresPlantillasError = document.getElementById("coloresPlantillasError");
    

    document.getElementById("nombrePlantilla").addEventListener("input", 
    function() {
        document.getElementById("nombrePlantillaError").textContent = "";
    });
    document.getElementById("foto").addEventListener("input", 
    function() {
        document.getElementById("fotoError").textContent = "";
    });
    document.getElementById("coloresPlantillas").addEventListener("input", 
    function() {
        document.getElementById("coloresPlantillasError").textContent = "";
    });

    
var hayErrores =false;


    var btnRadioSeleccionado = document.querySelector('input[name="btnradio2"]:checked');
    if (!btnRadioSeleccionado) {
        seleccionError.textContent = "Por favor, seleccione una opción para cómo se puede usar la plantilla.";
    } else {
        seleccionError.textContent = "";
    }

    if (nombrePlantilla.trim() === "") {
        nombrePlantillaError.textContent = "Por favor, ingrese el nombre de la plantilla.";
        hayErrores = true;
    } else {
        nombrePlantillaError.textContent = "";
    }

    if (foto.trim() === "") {
        fotoError.textContent = "Por favor, ingrese su archivo.";
        hayErrores = true;
    } else {
        fotoError.textContent = "";
    }

    if (coloresPlantillas.trim() === "") {
        coloresPlantillasError.textContent = "Por favor, ingrese su categoria.";
        hayErrores = true;
    } else {
        coloresPlantillasError.textContent = "";
    }
    
    


return !hayErrores; // Devuelve true si no hay errores, false si hay al menos un error
}




function soloNumeros(event) {
    // Obtiene el código de la tecla presionada
    var codigoTecla = event.keyCode ? event.keyCode : event.which;

    // Permite las teclas de control como "Enter" y "Backspace"
    if (codigoTecla == 8 || codigoTecla == 13) {
      return true;
    }

    // Verifica si el código de la tecla corresponde a un número o al guion ("-")
    if ((codigoTecla < 48 || codigoTecla > 57) && codigoTecla !== 45) {
      event.preventDefault(); // Detiene la acción predeterminada (ingresar el carácter)
      return false;
    }

    return true;
}


function validarCantidad(input) {
    var valor = input.value;
    var patron = /^[1-3]$/;

    if (!patron.test(valor)) {
        input.value = valor.replace(/[^1-3]/g, "");
    }
}


function decrementarCantidad(elemento) {
    var inputCantidad = elemento.parentNode.querySelector('input[type="text"]');
    var cantidadActual = parseInt(inputCantidad.value);
    if (cantidadActual > 1) {
        inputCantidad.value = cantidadActual - 1;
    }
}

function incrementarCantidad(elemento) {
    var inputCantidad = elemento.parentNode.querySelector('input[type="text"]');
    var cantidadActual = parseInt(inputCantidad.value);
    if (cantidadActual < 3) {
        inputCantidad.value = cantidadActual + 1;
    }
}



