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
    var apellido = document.getElementById("apellido").value;
    var rut = document.getElementById("rut").value;
    var colores = document.getElementById("colores").value;
    var edad = document.getElementById("edad").value;
    

    var nombreError = document.getElementById("nombreError");
    var apellidoError = document.getElementById("apellidoError");
    var rutError = document.getElementById("rutError");
    var coloresError = document.getElementById("coloresError");
    var edadError = document.getElementById("edadError");
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
    document.getElementById("nombre").addEventListener("input", 
    function() {
        document.getElementById("nombreError").textContent = "";
    });
    
    document.getElementById("apellido").addEventListener("input", 
    function() {
        document.getElementById("apellidoError").textContent = "";
    });
    
    document.getElementById("rut").addEventListener("input", 
    function() {
        document.getElementById("rutError").textContent = "";
    });
    
    document.getElementById("colores").addEventListener("input", 
    function() {
        document.getElementById("coloresError").textContent = "";
    });
    
    document.getElementById("edad").addEventListener("input", 
    function() {
        document.getElementById("edadError").textContent = "";
    });
    
   

    var hayErrores = false;

    if (nombre.trim() === "") {
        nombreError.textContent = "Por favor, ingrese su nombre.";
        hayErrores = true;
    } else {
        nombreError.textContent = "";
    }

    if (apellido.trim() === "") {
        apellidoError.textContent = "Por favor, ingrese su apellido.";
        hayErrores = true;
    } else {
        apellidoError.textContent = "";
    }
    
    if (rut.trim() === "") {
        rutError.textContent = "Por favor, ingrese su RUT.";
        hayErrores = true;
    } else if (isNaN(rut)) { // Si el RUT tiene letras
        rutError.textContent = "Por favor, ingresa solo números.";
        hayErrores = true;
    } else if (rut.length < 10) { // Si el RUT tiene menos de 10 caracteres
        rutError.textContent = "El RUT debe tener al menos 10 caracteres.";
        hayErrores = true;
    } else if (rut.length > 10) { // Si el RUT tiene más de 10 caracteres
        rutError.textContent = "El RUT no puede tener más de 10 caracteres.";
        hayErrores = true;
    } else {
        rutError.textContent = ""; // Borrar el mensaje de error si la longitud es correcta
    }

    
    if (colores.trim() === "") {
        coloresError.textContent = "Por favor, ingrese el color que desea escojer.";
        hayErrores = true;
    } else {
        coloresError.textContent = "";
    }

    if (edad.trim() === "") {
        edadError.textContent = "Por favor, ingrese su edad.";
        hayErrores = true;
    } else {
        edadError.textContent = "";
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
        coloresPlantillasError.textContent = "Por favor, ingrese su plantilla.";
        hayErrores = true;
    } else {
        coloresPlantillasError.textContent = "";
    }
    
    


return !hayErrores; // Devuelve true si no hay errores, false si hay al menos un error



}


