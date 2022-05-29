<h1 align="center">Proyecto Final Base de datos</h1>
<h2 align="center"> LABIN</h2>
<h3 align="center"> Programa para el inventario de Laboratorios Químicos</h3>
 Presentado por por: 
    Gina Stephanie Gonzalez M
    
# Tabla de Contenidos
[1. Introducción](#introducción)

[2. Herramientas usadas para la solución](#herramientas-usadas-para-la-solución)

[3. Necesidad](#necesidad)

[4. Diseño de interfaz](#diseño-de-interfaz)

[5. MER](#mer)

[6. Arquitectura de software](#arquitectura-de-software)

[7. Metología usada](#metodologia-usada)

[8.Desarrollo Proyecto](#Desarrollo-Proyecto)



# Introducción
Los laboratorios tienen una labor muy importante en el gestionamiento de todos los materiales, reactivos y equipos. Por un lado, los equipos de laboratorio son extremadamente delicados y requieren de cuidados específicos. En cuanto a los materiales de los laboratorios el problema radica en su gran cantidad y en la fragilidad de algunos materiales. Por último, se encuentran los reactivos, punto que es fundamental y por lo cual se debe tener una gestión eficiente y adecuada, debido a que se deben controlar y supervisar todos los reactivos que sean peligrosos y que puedan apelar contra la salud y la integridad de cualquier persona que haga uso del laboratorio. 
Cada laboratorio debe tener un sistema de base de datos donde se realiza la gestión del inventario, siendo una de las partes fundamentales y más complejas, debido a que cada vez que se usa un reactivo, se realiza mantenimiento a un equipo, se producen salidas o entradas de las sustancias o equipos, se debe actualizar el inventario con el fin de llevar un control total del laboratorio, volviéndose un proceso repetitivo y complejo.   

Es por esto que se decidió desarrollar un programa  para el control de inventarios que permita gestionar entradas y salidas de los diferentes equipos y reactivos para poder gestionar los inventarios de una forma más eficiente. 

# Herramientas usadas para la solución
<h2>Python</h2>
La primer  herramienta utilizada, será el lenguaje de programación Python. Este lenguaje se eligió debido a que es uno de los lenguajes de programación más actuales y de los más sencillos de usar, debido a que este posse una sintaxis simple y de fácil aprenidzaje. Además de esto es un lenguaje muy productivo y es de código abierte, por lo que ofrece muchas ventajas para este proyecto. 

![python.jpg](https://talently.tech/blog/wp-content/uploads/2020/11/cuanto-gana-un-programador-de-python-en-peru.jpg)


<h2> Visual Studio Code </h2> 

Se va a utilizar el editor de texto Visual Studio Code, esto debido a que es un editor de texto fácil de usar, el cual es multiplataforma, desarrollado por Microsoft por lo que es gratuito y de código abierto siendo esta una herramienta de programación avanzada.

![visualcode.jpg](https://programacion.net/files/article/20170630010634_visual-studio-code.png)



<h2> Balsamiq </h2> 
La herramienta balsamiq nos permitirá crear el prototipo y modelado del proyecto, debido a que esta herramienta es una de las mejores 
para crear prototipos, bocetos o wireframes es Balsamiq Mockups

![balsamiq.jpg](https://llops.com/blog/content/articulos/oct08/set_componentes.jpg)


<h2> MySQL y MySQL Workbench  </h2> 
MySQL es un sistema open source de administración de bases de datos que es desarrollado y soportado por Oracle, por lo cual además se utilizó el programa MySQL Workbench debido a que es una herramienta visual de diseño de bases de datos que integra desarrollo de software, administración de bases de datos, diseño de bases de datos, creación y mantenimiento para el sistema de base de datos MySQL.

![Mysql.jpg](https://solocodigoweb.com/wp-content/uploads/2014/03/cronologia-historia-de-mysql-cloud-computing-solocodigoweb.jpg)


# Necesidad
El incorrecto manejo del inventario perjudica las prácticas de los laboratorios debido a que afecta los procesos de formación y procesos de investigación al encontrar incoherencias en los inventarios . Esto genera que se compren mayores cantidades de reactivos innecesarios, o que se venzan los reactivos por lo que ya no se pueden usar en procesos de investigación. Por otro lado, se debe tener control de las salidas y las entradas de los productos para saber cuando se debe adquirir más de un producto o cuando hay suficiente cantidad para las prácticas. 

# Interfaz gráfica

El proyecto va a constar de diferentes secciones. En primer lugar va a constar de dos diferentes ingresos al inventario; El usuario puede ingresar al sistema como invitado para únicamente revisar el inventario y buscar los productos o puede iniciar sesión para poder modificar, eliminar e insertar los materiales en el inventario del laboratorio. 

![inisiosesion.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/iniciosesion.png)

En caso de que el usuario ingrese como invitado logrará navegar por el inventario y podrá buscar los productos para ver la información de cada uno, sin embargo, no tendrá permiso de insertar, eliminar o modificar ningún producto del laboratorio

![invitado.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/invitado.png)

Por otro lado, si el usuario inicia sesión va a tener el permiso de insertar, modificar y eliminar productos del inventario. Las sigueintes imagenes mostrarán los datos de cada uno de los productos del inventario como lo son Equipos, Reactivos y Materiales. 

![crud.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/crud.png)
![crudreac](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/crudreac.png)
![crudmat](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/crudmat.png)

Además, en una diferente sección se va a poder observar cual es la próxima fecha de revisión y mantenimiento en cuanto a los equipos, y cual es la fecha de vencimiento en cuanto a los reactivos como se muestra a continuación 

![revreactivos](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/revreac.png)
![revequipos](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/revreactivos.png)

# MER

El modelo entidad-relación del proyecto se muestra a continuación:
![Mer.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/MER.png)

# Arquitectura de Software

La arquitectura que se decidió implementar en el proyecto es la arquitectura cliente-servidor, esto debido a que los usuarios van a estar conectados al servidor de base de datos en donde se almacenará toda la información de los productos del laboratorio, por esto los recursos siempre estarán a disposición de los usuarios que van a hacer uso de esta información . Todas las gestiones que se realizarán van a estar concentradas en el servidor, además, el servidor tambien dispondrá de los requerimientos provenientes de los usuarios que tienen prioridad ,o, de la información que es de uso público. 

El proyecto se compondrá de una red LAN la cual tendrá 3 computadores para los usuarios una impresora y un servidor de base de datos donde se almacenará la información, los cuales estarán interconectados por medio de un switch. A continuación se muestra la arquitectura de software del proyecto realizada en Cisco Packet Tracer. 

![LAN.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/LAN.png)

# Metodología Ágil

El proyecto se realizará en base a una metodología ágil debido a que gracias a estas metodologías se logra adaptar a la forma de trabajo y a las condiciones del proyecto,utilizando enfoques flexibles para ofrecer mejoras y aumentar la satisfacción del cliente. Es por esto, que se decidió utilizar la metodología SCRUM.
La metodología SCRUM se utilizó debido a sus ventajas, las cuales son: innovación, flexibilidad, competitividad y productividad.
La metodología SCRUM se compone de diferentes etapas. 
- La primer etapa es de suma importancia debido a que se crea la visión del proyecto y el plan de lanzamiento.
- La segunda etapa es la de planificación y estimación donde se elaboran y se definen las primeras tareas y se aceptan sugerencias y optimizaciones del proceso
- La tercer etapa es la implementación donde se crean los primeros entregables diseñando la aplicación junto con las optimizaciones del cliente
- La cuarta etapa es la revisión e retroespectiva donde se construye y se implementa el programa realizando demostraciones y validaciones del mismo
- La quinta y última etapa es el lanzamiento donde se envían los entregables y se hace la respectiva evaluación y monitoreo del proyecto

![SCRUM.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagenes%20para%20el%20proyecto/SCRUM.png)

# Desarrollo Proyecto

### A continuación se expondrá el desarrollo y la demostración del proyecto:


Inicialmente se creo la base de datos que se usó para el proyecto la cual se nombró comó Lab_inventario donde por medio de esta se crearon las diferentes tablas para el desarrollo del proyecto, con un total de 4 tablas; Una tabla que contendrá los datos de los usuarios autorizados a modificar la base de datos. La segunda tabla contendrá los datos de los equipos registrados, la tercera tabla los datos de los reactivos registrados y finalmente, la cuarta tabla contendrá los materiales registrados. 
![sqltablas.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/sqltablas.png)

Una vez que se ejecuta el código este va a mostrar una ventana donde le usuario va a tener dos opciones; Si el usuario es un usuario autorizado, este podrá ingresar con sus credenciales y va a poder modificar, eliminar, e insertar datos haciendo click en iniciar sesión. Sin embargo, en dado caso que el usuario no este autorizado solo podrá ingresar a mirar el inventario y buscar los datos necesarios sin poder realizar ninguna modificación.

![login.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/login.png)

Si el usuario ingresa como invitado va poder realizar las busquedas necesarias y mirar el inventario, sin embargo si ya desea realizar un cambio el usuario debe iniciar sesión. A continuación se expone como un usuario no autorizado puede interactuar con el programa

### Inicio Invitado
![buscarinv.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/buscarinv.png)

### Pestaña Equipos vista invitado
![buscareqinv.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/buscareqinv.png)
### Pestaña Reactivos vista invitado
![buscarrecinv.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/buscarinv.png)
### Pestaña Materiales vista invitado
![buscarmatinv.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/buscarinv.png)

En dado caso que ya se dese iniciar sesión, en cada una de las pestañas mencionadas anteriormente hay un botón de inicio de sesión, y una vez presionado, redirige al usuario a hacer login, en caso que el usuario acceda con credenciales en las bases de datos el programa le mostrará una alerta de ingreso satisfactorio, y en caso de que el usuario ingrese credenciales que no se encuentren en la base de datos se negará el acceso. 

### Acceso Satisfactorio
![loginY.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/loginY.png)
### Acceso Denegado
![loginN.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/loginN.png)

Una vez que el usuario ingrese este logrará ver las diferentes opciones para modificar el inventario de laboratorio, cada una de las pestañas dejará al usuario autorizado insertar, eliminar o modificar un dato de una manera eficiente como se demuestra a continuación

### Inicio Admin
![admin.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/admin.png)

### Pestaña Equipos vista Admin
![admineq.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/admineq.png)
### Pestaña Reactivos vista Admin
![adminreac.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/adminreac.png)
### Pestaña Materiales vista invitado
![adminmat.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/adminmat.png)


Además si el usuario desea buscar un archivo una vez que ingrese a la pestaña de buscar esta lo redirigirá a la ventana de busqueda la cual es la misma que la de busqueda de invitado, sin embargo, si se ingresa a esta ventana una vez ya se ha iniciado sesión el programa ya no le dirá al usuario que inicie sesión sino le mostrará un botón de volver para que el usuario pueda volver a la ventana de modificación inmediatamente

### Búsqueda Admin
![adminbusc.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/adminbusc.png)

Finalmente tanto para vista invitado como para la vista de Admin la última pestaña que se verá en el programa es la venta autor, donde se verán los respectivos créditos y detalles de quien realizó el proyecto

### Autor
![adminautor.png](https://github.com/Stepha-gon/ProyectoFinalBD/blob/main/imagit/adminautor.png)

