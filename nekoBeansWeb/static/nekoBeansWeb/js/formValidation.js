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
  var nombre = document.getElementById("{{ form.nombre.id_for_label }}").value.trim();
  var apellido1 = document.getElementById("{{ form.apellidos.id_for_label }}").value.trim();
  var rut = document.getElementById("{{ form.rut.id_for_label }}").value.trim();
  var region = document.getElementById("{{ form.region.id_for_label }}").value.trim();
  var fecha = document.getElementById("{{ form.fecha_nacimiento.id_for_label }}").value.trim();
  var carnet = document.getElementById("{{ form.carnet.id_for_label }}").value.trim();

  var nombreError = document.getElementById("nombreError");
  var apellido1Error = document.getElementById("apellidosError");
  var rutError = document.getElementById("rutError");
  var regionError = document.getElementById("regionError");
  var fechaError = document.getElementById("fechaError");
  var carnetError = document.getElementById("carnetError");

  var hayErrores = false;

  if (nombre === "") {
    nombreError.textContent = "Por favor, ingrese su nombre.";
    hayErrores = true;
  }

  if (apellido1 === "") {
    apellido1Error.textContent = "Por favor, ingrese su apellido paterno";
    hayErrores = true;
  }

  if (rut === "") {
    rutError.textContent = "Por favor, ingrese su RUT.";
    hayErrores = true;
  } else if (rut.length < 10 || rut.length > 12) {
    rutError.textContent = "El RUT debe tener entre 10 y 12 caracteres.";
    hayErrores = true;
  }

  if (region === "") {
    regionError.textContent = "Por favor, seleccione una región.";
    hayErrores = true;
  }

  if (fecha === "" || !/^\d{4}-\d{2}-\d{2}$/.test(fecha)) {
    fechaError.textContent = "Por favor, ingrese una fecha válida en formato yyyy-mm-dd.";
    hayErrores = true;
  }

  if (carnet === "") {
    carnetError.textContent = "Por favor, adjunte su foto de carnet.";
    hayErrores = true;
  }

  return !hayErrores; // Devuelve true si no hay errores, false si hay al menos un error
}

// Event listener para limpiar errores al escribir en los campos
var campos = ["{{ form.nombre.id_for_label }}", "{{ form.apellidos.id_for_label }}", "{{ form.rut.id_for_label }}", "{{ form.region.id_for_label }}", "{{ form.fecha_nacimiento.id_for_label }}", "{{ form.carnet.id_for_label }}"];
campos.forEach(function(campo) {
  document.getElementById(campo).addEventListener("input", function() {
    document.getElementById(campo + "Error").textContent = "";
  });
});


// Event listener para limpiar errores al escribir en los campos
var campos = ["{{ form.nombre.id_for_label }}", "{{ form.apellidos.id_for_label }}", "{{ form.rut.id_for_label }}", "{{ form.region.id_for_label }}", "{{ form.fecha_nacimiento.id_for_label }}", "{{ form.carnet.id_for_label }}"];
campos.forEach(function(campo) {
  document.getElementById(campo).addEventListener("input", function() {
    document.getElementById(campo + "Error").textContent = "";
  });
});


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



function validacionCrear() {
    var nombrePlantilla = document.getElementById("nombrePlantilla").value;
    var foto = document.getElementById("foto").value;
    var descripcion = document.getElementById("descripcion").value;
    var tipoModoUso = document.getElementById("tipo_modo_uso").value;
    var categoria = document.getElementById("categoria").value;

    var nombrePlantillaError = document.getElementById("nombrePlantillaError");
    var fotoError = document.getElementById("fotoError");
    var descripcionError = document.getElementById("descripcionError");
    var tipoModoUsoError = document.getElementById("tipoModoUsoError");
    var categoriaError = document.getElementById("categoriaError");

    // Limpiar errores previos
    nombrePlantillaError.textContent = "";
    fotoError.textContent = "";
    descripcionError.textContent = "";
    tipoModoUsoError.textContent = "";
    categoriaError.textContent = "";

    var hayErrores = false;

    if (nombrePlantilla.trim() === "") {
        nombrePlantillaError.textContent = "Por favor, ingrese el nombre de la plantilla.";
        hayErrores = true;
    }
    if (foto.trim() === "") {
        fotoError.textContent = "Por favor, ingrese su archivo.";
        hayErrores = true;
    }
    if (descripcion.trim() === "") {
        descripcionError.textContent = "Por favor, ingrese la descripción.";
        hayErrores = true;
    }
    if (tipoModoUso === "") {
        tipoModoUsoError.textContent = "Por favor, seleccione el modo de uso.";
        hayErrores = true;
    }
    if (categoria.trim() === "") {
        categoriaError.textContent = "Por favor, ingrese la categoría.";
        hayErrores = true;
    }

    return !hayErrores; // Devuelve true si no hay errores, false si hay al menos un error
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

function validateForm(event) {
    var nombre = document.getElementById("id_nombre").value;
    var apellidos = document.getElementById("id_apellidos").value;
    var email = document.getElementById("id_email").value;
    var telefono = document.getElementById("id_telefono").value;
    var tipoSolicitud = document.getElementById("id_tipo_solicitud").value;
    var mensaje = document.getElementById("id_mensaje").value;
    
    var nombreError = document.getElementById("nombreError");
    var apellidosError = document.getElementById("apellidosError");
    var emailError = document.getElementById("emailError");
    var telefonoError = document.getElementById("telefonoError");
    var tipoSolicitudError = document.getElementById("tipoSolicitudError");
    var mensajeError = document.getElementById("mensajeError");

    // Clear previous error messages
    nombreError.textContent = '';
    apellidosError.textContent = '';
    emailError.textContent = '';
    telefonoError.textContent = '';
    tipoSolicitudError.textContent = '';
    mensajeError.textContent = '';

    var isValid = true;

    // Validate nombre
    if (nombre === '') {
        nombreError.textContent = 'El nombre es obligatorio.';
        isValid = false;
    }

    // Validate apellidos
    if (apellidos === '') {
        apellidosError.textContent = 'Los apellidos son obligatorios.';
        isValid = false;
    }

    // Validate email
    if (email === '') {
        emailError.textContent = 'El email es obligatorio.';
        isValid = false;
    } else if (!validateEmail(email)) {
        emailError.textContent = 'El email no es válido.';
        isValid = false;
    }

    // Validate telefono
    if (telefono === '') {
        telefonoError.textContent = 'El teléfono es obligatorio.';
        isValid = false;
    } else if (telefono.length !== 9 || isNaN(telefono)) {
        telefonoError.textContent = 'El número de teléfono debe tener exactamente 9 dígitos.';
        isValid = false;
    }

    // Validate tipoSolicitud
    if (tipoSolicitud === '') {
        tipoSolicitudError.textContent = 'El tipo de solicitud es obligatorio.';
        isValid = false;
    }

    // Validate mensaje
    if (mensaje === '') {
        mensajeError.textContent = 'El mensaje es obligatorio.';
        isValid = false;
    }

    if (!isValid) {
        event.preventDefault();
    }

    return isValid;
}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@(([^<>()[\]\\.,;:\s@"]+\.[^<>()[\]\\.,;:\s@"]{2,}))$/i;
    return re.test(String(email).toLowerCase());
}

function soloNumeros(event) {
    var key = window.event ? event.keyCode : event.which;
    if (key < 48 || key > 57) {
        event.preventDefault();
    }
}
