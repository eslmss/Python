# Guia para crear un proyecto con Poetry

### Instalar Poetry 
- Desde la terminal, ejecuta el siguiente comando:

    ```
    py -m pip install poetry
    ```
    o

    ```
    python -m pip install poetry
    ```

</br>

### Crear un nuevo proyecto

- Desde la terminal, ubicate en la carpeta donde quieras crear tu proyecto y ejecuta: 
    ```
    py -m poetry new repository_name
    ```
    o

    ```
    python -m poetry new repository_name
    ```

### Configurar dependencias
- Ubicate en el repositorio creado con el siguiente comando:
  ```
  cd repository_name
  ```
- Dentro del repository, verás la estructura básica de un proyecto. Abre "pyproject.toml" para ver la configuración y modificarla. Podrás modificar ahí las dependencias pero es mejor ejecutarlas por consola.
- Desde la terminal instala los paquetes/librerias que quieras utilizar en tu proyecto.
  ```
  py -m poetry add library_name
  ```
  o

  ```
  python -m poetry add library_name
  ```

### Crear un entorno virtual con la config seteada

- Cuando termines de instalar todas las dependencias. ejecuta el siguiente comando para crear el entorno virtual.
  ```
  py -m poetry install
  ```
  o

  ```
  python -m poetry install
  ```

### Utilizar entorno virtual

- Para ingresar al entorno generado, ejecuta el siguiente comando:
  ```
  py -m poetry shell
  ```
  o

  ```
  python -m poetry shell
  ```
- Para ejecutar un modulo python en el entorno:
  ```
  poetry run python nombre_archivo.py
  ```

### Salir del entorno

- Cuando quieras salir del entorno, puede ejecutar en la terminal:
  ```
  exit
  ```

### Actualizar dependencias
- Verifica si existen versiones mas recientes de todas las dependencias con:
  ```
  py -m poetry update
  ```
  o

  ```
  python -m poetry update
  ```
- Actualizar todo, ejecuta:
  ```
  py -m poetry update --lock
  ```
  o
  ```
  python -m poetry update --lock
  ```
- Actualizar solo dependencias específicas:
  ```
  py -m poetry update library_name
  ```
  o

  ```
  python -m poetry update library_name
  ``` 

### Eliminar dependencias
- Para sacar librerias instaladas, ejecuta el siguiente comando en consola:
  ```
  py -m poetry remove library_nam
  ```