# Administrador de Empleados

## Instrucciónes para instalar e iniciar los servicios

Esta guía asume que usted posée una instalación de `Docker 20.10.17` y `docker-compose v2.10.2` en su sistema.

1. Descargue el repositorio con `git clone`.
2. Sitúese dentro de la carpeta raíz del proyecto `grupo-salinas-api`.
3. Desde esta ubicación ejecute `docker-compose up -d --build`.
4. Puede ver los logs del servidor con `docker-compose logs -f web`.
5. Ahora ingrese la siguiente dirección en la barra de búsqueda de su navegador `http://127.0.0.1:8004/docs` para visitar la documentación del projecto.

## Instrucciones para interactuar con la base de datos

La base de datos utilizada en este proyecto es PostgreSQL

1. Habra una terminal y ejecute `docker-compose exec web-db psql -U postgres`
2. Verá el siguiente propmt `postgres=#`
3. Para ver las bases de datos creadas `\l` incluya la barra invertida.
4. Para usar la base de datos del proyecto `\c empleados_dev`
5. Liste las tablas con `\dt`
6. Consulte las tablas que necesite

## Instrucciones de uso para la API REST

### NOTA: Su sesión está configurada para expirar cada 5 minutos (también puede validarlo)

1. El servidor valida el primer registro de usuario del sistema (no está autorizada ninguna petición sin un registro de usuario). Si es el primer usuario del sistema, éste le asignará el rol de `administrador`. Los siguientes usuarios creados, por defecto tendrán el rol de `operador` siguiendo la práctica del mínimo privilegio.
```
POST /api/v1/users
```
2. Para poder usar la documentación interactiva de manera óptima le recomiendo autenticarse dando click en el boton `Authorize` que se encuentra en la parte superior derecha. Esto permitirá que la documentación interactiva proporcione el token de acceso de manera automática en cada petición subsecuente.
3. Cree un par de `Empleados` para verificar la funcionalidad así como las validaciónes.
4. Puede crear más usuarios y modificar sus roles usando el usuario administrador que creó por primera vez (solo los administradores pueden modificar el rol de un usuario)