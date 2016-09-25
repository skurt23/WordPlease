#WordPlease

Práctica para el módulo de Django del Web Development Bootcamp

##Anotaciones para el profesor:
* Las vistas de inicio de sesión, registro y cerrar sesión no tienen estilos
porque usé las vistas predefinidas de la librería django-allauth.Por esta razón el registro
vía web no solicita el nombre y apellidos del usuario, el registro vía API sí solicita esos datos.

* En este momento está todo realizado y funcionando(en la última prueba realizada funcionaba todo),
incluídos algunos extras.

* Para crear un nuevo artículo vía web, hay que estar autenticado y, para ir a la vista, clickar
sobre el botón que aparece en la esquina inferior derecha de la web.

* Algunos detalles del css para el responsive no funcionan del todo bien, no me dio tiempo de revisar todo 
el css en los distintos dispositivos.

* Las urls disponibles, son las requeridas por la práctica pero sería mejor consultarlas en los distintos urls.py,
por ejemplo, las urls de inicio de sesión, registro y cerrar cesión están definidas por la librería django-allauth:
    * /accounts/login
    * /accounts/signup
    * /accounts/logout

* La url del API del listado de blogs es **/api/1.0/blogs/**, pero la URL del listado de artículos
de un blog es **/api/1.0/blog/usuario_del_blog_que_desea_ver/** y para el detalle de un artículo, la URL
es **/api/1.0/blog/usuario_del_blog_que_desea_ver/id_del_artículo_que_desea_ver/**
