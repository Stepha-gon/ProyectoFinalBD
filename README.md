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



# Introducción
Los laboratorios tienen una labor muy importante en el gestionamiento de todos los materiales, reactivos y equipos.mPor un lado, los equipos de laboratorio son extremadamente delicados y requieren de cuidados específicos. En cuanto a los materiales de los laboratorios el problema radica en su gran cantidad y en la fragilidad de algunos materiales. Por último, se encuentran los reactivos, punto que es fundamental y por lo cual se debe tener una gestión eficiente y adecuada, debido a que se deben controlar y supervisar todos los reactivos que sean peligrosos y que puedan apelar contra la salud y la integridad de cualquier persona que haga uso del laboratorio. 
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


<h2> Managment Studio y SQL server  </h2> 
SQL Server Management Studio es un entorno de desarrollo integrado para administrar cualquier infraestructura SQL y se utiliza para tareas relacionadas con la gestión de bases de datos y de la comunicación con el Servidor. Microsoft SQL Server es un sistema de administración de bases de datos que permite el procesamiento de transacciones y las aplicaciones de análisis.  

![sqlserver.jpg](https://blog.rmaafs.com/wp-content/uploads/2021/05/smss-logo.png)


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


