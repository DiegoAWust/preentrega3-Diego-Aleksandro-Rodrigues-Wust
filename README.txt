# Nombre de Proyecto: pagina terminada
# Alumno: Diego Aleksandro Rodrigues Wust
# Fecha: 7/2/2024
# Versión: Proyecto final 
# Video youtube:

# Aplicacion que permite la funcionalidad de una pagina de ventas

- Los modelos que presenta esta aplicacion son:
  - User
  - Producto
  - Soporte
  - Avatar
  - pedidos
  - lineapedidos

- Orden de prueba de la aplicacion 

  - registrar un usuario sin permiso admin: http://127.0.0.1:8000/registro/
  - loguearse : http://127.0.0.1:8000/login/
  - Loguear con usuario admin para visualizar todas las opciones que ofrece:
  Usuario: admin
  Contraseña: 123
  - Crear productos: http://127.0.0.1:8000/Agregarproductos/             #funcion de admin
  - Crear reportes : http://127.0.0.1:8000/reportes/

  - Consultar todos los productos: http://127.0.0.1:8000/productos/
  - Consultar todos los reportes: http://127.0.0.1:8000/soporte/
  - Busqueda de productos por un patron en el nombre: http://127.0.0.1:8000/buscar/
  - Actualizar un reporte: http://127.0.0.1:8000/soporte_actualizar/id del reporte/             #funcion de admin
  - Actualizar un producto: http://127.0.0.1:8000/producto_actualizar/id del producto/            #funcion de admin
  - se puede eliminar tanto productos como reportes dando click en el icono por debajo de editar               #funcion de admin
  - modificar avatar: http://127.0.0.1:8000/agregar_avatar/
  - editar perfil: http://127.0.0.1:8000/editar_perfil/
  - acerca de mi: http://127.0.0.1:8000/nosotros/
  - agregar elementos al carro, como tambien eliminarlos, no se puede realizar el pedido
  - se precisa estar logueado para ingresar a las url


  EXTRA
https://github.com/DiegoAWust/Proyecto-final-Diego-Aleksandro-Rodrigues-Wust
  el pedido no pude solucionar su funcionalidad, sus funciones estan y andan, lo que suelta error es la vinculacion de un correo para enviar el correo al usuario