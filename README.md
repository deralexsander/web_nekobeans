# NekoBeans 🐱

Mi **primer proyecto web**. Es la tienda online de mi pyme de manualidades, donde vendo **broches y colgantes de chaquira**. La idea era que los clientes pudieran comprar sin tener que depender tanto del contacto directo conmigo.

Hecho con **Django 5.0.6**, SQLite, Bootstrap y SweetAlert.

## Funciones principales

- **Productos:** el cliente elige lo que le gusta.
- **Carrito:** muestra la cantidad y el precio total.
- **Pagar:** el cliente rellena sus datos de envío.
- **Formas de pago:** efectivo o transferencia. La opción **tarjeta es solo decorativa**, porque en el ramo nos pidieron no trabajar con pagos con tarjeta.
- **Sugerencias:** el cliente puede pedir un broche o colgante en especial.
- **Trabaja con nosotros:** postulación para ser parte del equipo del vendedor.
- **Ayuda:** cómo funciona, problemas con un pedido y servicio de reparación.

## Roles y permisos

El sitio usa los grupos de Django para controlar quién ve qué.

| Función | Visitante | Usuario | Vendedor | Administrador |
|---|:-:|:-:|:-:|:-:|
| Ver inicio, productos y ayuda | ✅ | ✅ | ✅ | ✅ |
| Registrarse / iniciar sesión | ✅ | ✅ | ✅ | ✅ |
| Carrito, pagar y *tus pedidos* | | ✅ | ✅ | ✅ |
| Enviar sugerencia, contacto y postulación | | ✅ | ✅ | ✅ |
| Crear / modificar productos | | | ✅ | ✅ |
| Listar plantillas (sugerencias) | | | ✅ | ✅ |
| Pedidos generales y modificar pedido | | | ✅ | |
| Lista de peticiones (postulaciones) | | | | ✅ |
| Lista de comentarios | | | | ✅ (solo superusuario) |
| Panel `/admin/` de Django | | | | ✅ (superusuario) |

> Las cuentas de las capturas son de demostración y no corresponden a clientes reales.

---

## 👤 Visitante (sin cuenta)

| Inicio | Productos |
|---|---|
| ![Inicio](docs/screenshots/visitante/01-inicio.png) | ![Productos](docs/screenshots/visitante/02-productos.png) |

**Detalle de un producto**

![Detalle de producto](docs/screenshots/visitante/08-producto-detalle.png)

**Ayuda:** cómo funciona, problemas con el pedido y servicio de reparación

![Cómo funciona](docs/screenshots/visitante/03-como-funciona.png)
![Problemas con el pedido](docs/screenshots/visitante/04-problemas-pedido.png)
![Servicio de reparación](docs/screenshots/visitante/05-servicio-reparacion.png)

**Cuenta**

| Iniciar sesión | Registro |
|---|---|
| ![Login](docs/screenshots/visitante/06-iniciar-sesion.png) | ![Registro](docs/screenshots/visitante/07-registro.png) |

## 🛍️ Usuario (cliente)

**Perfil:** desde aquí accede a sus opciones.

![Perfil de usuario](docs/screenshots/usuario/01-perfil.png)

**Sugerencias:** pedir un broche o colgante especial.

| Formulario | Lleno | Enviado |
|---|---|---|
| ![](docs/screenshots/usuario/02-sugerencia-vacio.png) | ![](docs/screenshots/usuario/03-sugerencia-formulario-lleno.png) | ![](docs/screenshots/usuario/04-sugerencia-enviada.png) |

**Contacto / comentarios**

| Lleno | Enviado |
|---|---|
| ![](docs/screenshots/usuario/05-contacto-formulario-lleno.png) | ![](docs/screenshots/usuario/06-contacto-enviado.png) |

**Trabaja con nosotros**

| Lleno | Enviado |
|---|---|
| ![](docs/screenshots/usuario/07-trabaja-formulario-lleno.png) | ![](docs/screenshots/usuario/08-trabaja-enviado.png) |

**Compra**

1. Productos y detalle

   ![Productos](docs/screenshots/usuario/09-productos.png)
   ![Detalle](docs/screenshots/usuario/10-producto-detalle.png)

2. Carrito con cantidades y precio

   ![Carrito](docs/screenshots/usuario/11-carrito.png)

3. Pagar: datos y forma de pago (efectivo o transferencia)

   ![Pagar](docs/screenshots/usuario/12-pagar-formulario-lleno.png)

4. Pedido confirmado

   ![Pedido confirmado](docs/screenshots/usuario/13-pedido-confirmado.png)

5. Seguimiento en *tus pedidos*

   ![Tus pedidos](docs/screenshots/usuario/14-tus-pedidos.png)

## 🧵 Vendedor

Crea productos y gestiona los pedidos y las plantillas que llegan de los clientes.

| Perfil | Crear producto |
|---|---|
| ![](docs/screenshots/vendedor/01-perfil.png) | ![](docs/screenshots/vendedor/02-crear-producto-formulario-lleno.png) |

| Listar productos | Modificar producto |
|---|---|
| ![](docs/screenshots/vendedor/03-listar-productos.png) | ![](docs/screenshots/vendedor/04-modificar-producto.png) |

| Listar plantillas | Pedidos generales |
|---|---|
| ![](docs/screenshots/vendedor/05-listar-plantillas.png) | ![](docs/screenshots/vendedor/06-pedidos-generales.png) |

**Modificar pedido** (estado del pedido, envío y pago)

![Modificar pedido](docs/screenshots/vendedor/07-modificar-pedido.png)

**Sin acceso** a las peticiones: el sitio lo redirige al login.

![Sin acceso](docs/screenshots/vendedor/08-sin-acceso-peticiones.png)

## 🛠️ Administrador

| Perfil | Listar productos |
|---|---|
| ![](docs/screenshots/administrador/01-perfil.png) | ![](docs/screenshots/administrador/02-listar-productos.png) |

| Listar plantillas | Lista de peticiones |
|---|---|
| ![](docs/screenshots/administrador/03-listar-plantillas.png) | ![](docs/screenshots/administrador/04-lista-peticiones.png) |

| Pedidos generales | Lista de comentarios |
|---|---|
| ![](docs/screenshots/administrador/05-pedidos-generales.png) | ![](docs/screenshots/administrador/06-lista-comentarios.png) |

**Panel de Django (`/admin/`)**

![Admin inicio](docs/screenshots/administrador/07-django-admin-inicio.png)
![Usuarios](docs/screenshots/administrador/08-django-admin-usuarios.png)
![Grupos](docs/screenshots/administrador/09-django-admin-grupos.png)
![Permisos del grupo vendedor](docs/screenshots/administrador/10-django-admin-permisos-vendedor.png)

---

## Cómo ejecutarlo

Requiere Python 3.10–3.12 (Django 5.0.6 no funciona con 3.14).

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir <http://127.0.0.1:8000/inicio/>. Para crear una cuenta de administrador: `python manage.py createsuperuser`.

## Lo que aprendí

Fue mi primera web: aprendí modelos, formularios, sesiones, carrito de compras y permisos por grupos con Django. Cosas que mejoraría:

- La *Lista de comentarios* pide el permiso `view_comentarios`, que no existe (debería ser `view_contacto`), así que solo la ve el superusuario.
- Hay un error de JavaScript en `formValidation.js` por selectores sin renderizar.
- El grupo *administrador* no tiene permisos sobre pedidos.
