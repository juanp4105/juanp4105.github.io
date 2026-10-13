# Sitio académico de Juan Pablo Arrobo Agila

Sitio estático en español, inglés y portugués, publicado con GitHub Pages en
https://juanp4105.github.io

## Estructura

- `index.html`, `investigacion.html`, `publicaciones.html`, `docencia.html`,
  `capacitacion-ia.html`, `contacto.html`: páginas en español.
- `en/` y `pt/`: las mismas páginas en inglés y portugués.
- `assets/`: estilos, script y fotografías.
- `_fuente/`: contenido y plantillas con los que se generan las páginas.
  GitHub Pages no publica esta carpeta.

## Cómo actualizar el contenido

1. Edite `_fuente/contenido.py` (biografía, publicaciones, proyectos, cursos).
   Cada texto traducible tiene sus versiones `"es"`, `"en"` y `"pt"`.
2. Regenere las páginas desde la carpeta del sitio:

   ```
   pip install jinja2
   python3 _fuente/build.py
   ```

3. Suba los cambios al repositorio. GitHub Pages actualiza el sitio en uno o dos minutos.

Para añadir una publicación, copie un bloque de la lista `PUBLICACIONES`,
cambie los datos y asigne su `tipo` (indexado, regional, capitulo, congreso,
divulgacion) y su `linea` de investigación (imagen, narrativas, ia, competencias).
