## Tabla de contenidos

- [Acerca de este repositorio](#Acerca-de-este-repositorio)
- [Hecho con](#Hecho-con)
- [Uso](#Uso)

## Acerca de este repositorio

Predice el precio del combustible en España introduciendo varios parámetros: datos obtenidos desde [CNMC Data](https://data.cnmc.es/energia/productos-petroliferos/precios-diarios-provinciales-de-productos-petroliferos). La predicción es a nivel provincial.  
Basado en un proyecto anterior para un curso.

Por un lado está la página web que una vez introducida la información necesaria, se hace una petición a la API que está en un 
contenedor de **Docker**. Se hace la predicción y se devuelve al usuario.  

Los modelos han sido ya entrenados y guardados en dos **Pickle**.  
Los modelos y el dataset sin limpiar no están incluidos en este repositorio, pero sí hay un cuaderno de **Jupyter** (**get_clean_train.ipynb** en el 
directorio **src**) para obtener tanto los datos como los modelos. Dicho cuaderno también tiene algunos comentarios de qué se está haciendo en cada bloque.  

Ahora mismo *origins* y *middleware* aceptan cualquier cosa, si se desea se puede cambiar en el archivo **api.py** dentro del directorio **api**.

Hay varios *bind mounts*, esto quiere decir que hay directorios que se comparten entre el contenedor y el host. Para este caso concreto, lo hago así 
para que sea más fácil editar los archivos desde VSCode con el host. Véase **docker-compose.yml**.

## Hecho con

- [Uvicorn](https://www.uvicorn.org)
- [FastAPI](https://fastapi.tiangolo.com)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [scikit-learn](https://scikit-learn.org/stable/index.html)
- [Docker](https://docs.docker.com)

## Uso

1. Desde el host lanzar todo el archivo **get_clean_train.ipynb** para obtener los datos, el archivo de **provincias.json**, el entrenamiento (ahora mismo es un árbol de decisión) 
y los modelos entrenados (en **Pickle**).
2. Iniciar el contenedor: `docker-compose up --build`
3. Ir a **localhost:8080/docs** si se quiere probar la API con [Swagger](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs).
4. Dentro del directorio **web**, desde CLI arrancar un servidor HTTP: `python -m http.server 8000`. Es posible que esto no sea necesario si se usa Live Server.
5. Ir a **localhost:8000** para poder navegar por la web (si no se hace de esta manera no cargará el archivo de **provincias.json** por culpa del CORS).
6. PAI predice el precio del combustible sin impuestos, PVP predice el precio del combustible con impuestos.
7. Introducir la fecha, provincia y el tipo de combustible.

## Por hacer

- Pasar el directorio **web** a un contenedor de Docker que esté relacionado con el de la API para poder saltar el paso 4.
- Ordenar mejor los archivos de **web**: guardar CSS y JS en subdirectorios.