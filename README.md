# Juego de la Vida

Este es un proyecto simple de implementación del "Juego de la Vida" de John Conway utilizando Pygame en Python. El juego simula la evolución de una población de células en un tablero bidimensional.

## Características

- Simulación del Juego de la Vida con reglas básicas de nacimiento y muerte de células.
- Interacción con el teclado y el mouse:
  - Pausar y reanudar el juego.
  - Activar o desactivar células manualmente.
- Menú principal con opciones para iniciar el juego y ver las instrucciones.

## Requisitos

Antes de ejecutar el juego, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.x**: Puedes descargar la última versión de Python desde [python.org](https://www.python.org/downloads/).
- **Pygame**: Una biblioteca de Python para escribir videojuegos. Puedes instalarla usando pip:

- pip install pygame

## Ejecución del Juego

Sigue estos pasos para ejecutar el juego en tu máquina local:

## Clona este repositorio:

git clone https://github.com/tu_usuario/juego-de-la-vida.git

cd juego-de-la-vida

## Ejecución del Juego

- Sigue estos pasos para ejecutar el juego en tu máquina local:

### Clona este repositorio:

- git clone https://github.com/tu_usuario/juego-de-la-vida.git
- cd juego-de-la-vida

### Instala las dependencias:

Asegúrate de tener instalado Pygame:

    - pip install pygame

### Ejecuta el juego:

- Puedes ejecutar el juego utilizando el siguiente comando:

  - python main.py

### Interactúa con el juego:

En la pantalla de menú:
Presiona 'S' para iniciar el juego.
Presiona 'I' para ver las instrucciones.

### En el juego:

Presiona Espacio para pausar/reanudar la simulación.
Usa el mouse para activar/desactivar células.
Presiona Esc para volver al menú principal.

## Estructura del Proyecto

```markdown
juego-de-la-vida/
│
├── main.py # Código principal del juego
├── README.md # Archivo de instrucciones
└── requirements.txt # Dependencias del proyecto (opcional)
```

## Instrucciones del Juego

El juego comienza con un tablero vacío o con algunas células ya vivas.

La simulación sigue las siguientes reglas:
Una célula muerta con exactamente 3 vecinas vivas "nace".
Una célula viva con menos de 2 o más de 3 vecinas vivas "muere".
Usa el mouse para añadir o eliminar células manualmente durante la simulación.
Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar este proyecto, no dudes en hacer un fork del repositorio y enviar un pull request.

**Licencia**
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

### Notas:

- Asegúrate de personalizar las secciones donde dice "tu_usuario" con tu nombre de usuario de GitHub.
- Si tienes otros archivos en tu proyecto (por ejemplo, imágenes, sonidos, etc.), puedes agregarlos a la estructura del proyecto en el README.

Este `README.md` proporciona una guía completa y clara para cualquiera que quiera entender, instalar y ejecutar tu proyecto en su máquina local.
