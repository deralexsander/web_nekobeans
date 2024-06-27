function validarInicioSesion(event) {
    var username = document.getElementById('id_username').value;
    var password = document.getElementById('id_password').value;
    var emailError = document.getElementById('emailError');
    var passwordError = document.getElementById('passwordError');
  
    emailError.textContent = '';
    passwordError.textContent = '';
  
    if (username === '') {
      emailError.textContent = 'El nombre de usuario es obligatorio.';
      event.preventDefault();
      return false;
    }
  
    if (password === '') {
      passwordError.textContent = 'La contraseña es obligatoria.';
      event.preventDefault();
      return false;
    }
  
    return true;
  }
  
  function togglePasswordVisibility() {
    var passwordInput = document.getElementById('id_password');
    var type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
  }
  

function togglePasswordVisibility() {
    var passwordField = document.getElementById("id_password");
    var passwordToggle = document.getElementById("togglePassword");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        passwordToggle.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-slash-fill" viewBox="0 0 16 16"><path d="M13.359 11.238a7.012 7.012 0 0 1-10.718 0 .5.5 0 1 1 .74-.672A6.012 6.012 0 0 0 13.86 11.61a.5.5 0 1 1 .74.672 7.012 7.012 0 0 1-1.24 0z"/><path d="M4.533 6.086a5.978 5.978 0 0 1 6.92 0 .5.5 0 0 1-.664.746A4.978 4.978 0 0 0 5.2 6.832a.5.5 0 1 1-.667-.746z"/><path d="M1.577 2.883a.5.5 0 0 1 .69-.143A7.012 7.012 0 0 1 14.24 11.15a.5.5 0 1 1-.74.672 6.012 6.012 0 0 0-10.128-7.327.5.5 0 0 1-.795-.612z"/></svg>';
    } else {
        passwordField.type = "password";
        passwordToggle.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16"><path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0"/><path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8m8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7"/></svg>';
    }
}


    
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


function validarRegistros(event) {
    var username = document.getElementById("username").value;
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;

    var usernameError = document.getElementById("usernameError");
    var password1Error = document.getElementById("password1Error");
    var password2Error = document.getElementById("password2Error");

    var hayErrores = false;

    // Limpia los mensajes de error anteriores
    usernameError.textContent = "";
    password1Error.textContent = "";
    password2Error.textContent = "";

    // Validaciones
    var usernamePattern = /^[\w.@+-]{1,150}$/;

    if (!usernamePattern.test(username)) {
        usernameError.textContent = "Requerido. 150 caracteres como máximo. Únicamente letras, dígitos y @/./+/-/_";
        hayErrores = true;
    }

    if (password1.length < 8) {
        password1Error.textContent = "Su contraseña debe contener al menos 8 caracteres.";
        hayErrores = true;
    }

    var commonPasswords = ["password", "12345678", "qwerty"];
    if (commonPasswords.includes(password1.toLowerCase())) {
        password1Error.textContent = "Su contraseña no puede ser una clave utilizada comúnmente.";
        hayErrores = true;
    }

    if (/^\d+$/.test(password1)) {
        password1Error.textContent = "Su contraseña no puede ser completamente numérica.";
        hayErrores = true;
    }

    if (password1 !== password2) {
        password2Error.textContent = "Las contraseñas no coinciden.";
        hayErrores = true;
    }

    return !hayErrores; // Devuelve true si no hay errores, false si hay al menos un error
}

// Mostrar/Ocultar contraseñas
document.getElementById("togglePassword1").addEventListener("click", function() {
    var password1 = document.getElementById("password1");
    if (password1.type === "password") {
        password1.type = "text";
    } else {
        password1.type = "password";
    }
});

document.getElementById("togglePassword2").addEventListener("click", function() {
    var password2 = document.getElementById("password2");
    if (password2.type === "password") {
        password2.type = "text";
    } else {
        password2.type = "password";
    }
});



// Mostrar/Ocultar contraseñas
document.getElementById("togglePassword1").addEventListener("click", function() {
    var password1 = document.getElementById("password1");
    if (password1.type === "password") {
        password1.type = "text";
    } else {
        password1.type = "password";
    }
});

document.getElementById("togglePassword2").addEventListener("click", function() {
    var password2 = document.getElementById("password2");
    if (password2.type === "password") {
        password2.type = "text";
    } else {
        password2.type = "password";
    }
});




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



