# El manual de carpintería

Este es el repositorio que crea [The Carpentries Handbook] (https://docs.carpentries.org).

## Organización del sitio

Este manual tiene tres secciones principales:

- **Manuales**.  Contiene manuales para cada función en la comunidad (anfitrión de la sesión comunitaria, instructor, etc.).  Cada rol de la comunidad tiene las mismas secciones siguientes, para garantizar que los usuarios tengan una experiencia uniforme mientras exploran cada rol.
  - Funciones y responsabilidades
  - Incorporación
  - Desembarque
  - Espacios de comunicación y colaboración
  - Guías paso a paso
  - Recursos
  - PREGUNTAS MÁS FRECUENTES
- **Recursos**.  Esta es una lista de los recursos generales disponibles para la comunidad de The Carpentries (guía de estilo, recursos de comunicación, etc.).
- **Políticas**.  Esta es una lista de todas las políticas de Carpentries (código de conducta, privacidad, etc.)

## Estructura de archivos

- `/build/` Se usa para crear un sitio web local. En `.gitignore`, por lo que esto no aparecerá en el repositorio.  No edite estos archivos.
- `/source/` Contiene todos los archivos necesarios para crear el sitio.  Incluye:
  - archivos css y plantillas de página que anulan los estilos y plantillas del tema
  - carpetas para manuales, recursos y políticas, con archivos «md\` con el contenido de cada página.
  - `/_includes/`: bloques de texto y otro contenido que se incluirá en otras páginas
  - `/_templates/`: plantillas para contenido especializado, como la tabla de contenido de la barra lateral
  - `/_static/` - contiene estilos css personalizados
  - `conf.py` - configuración del sitio
  - `index.rst` - establece la estructura de la página de inicio
- `.gitignore` Archivo gitignore estándar
- `Makefile`: incluye comandos Make personalizados y hereda los comandos generales de Sphinx Make.

## Edición de contenido

El contenido se organiza en el directorio `source`.  Se deben realizar modificaciones en el contenido de estos archivos.  No edite los archivos de la carpeta `build`.

## Edición de estilos

La mayoría de los estilos provienen de la plantilla `pydata_sphinx_theme`.  Los estilos personalizados se implementan en `/source/_static/css`.  Esto incluye los archivos de fuentes de la fuente Mulish de Google y un archivo css personalizado.

## Edición de plantillas y diseños

La mayoría de las plantillas y diseños provienen de la plantilla `pydata_sphinx_theme`.  Las plantillas de página personalizadas se implementan en `/source/_templates/`.  Por ejemplo, el tema estándar incluye funciones de Python para crear plantillas para la tabla de contenido de la barra lateral y la barra de navegación superior. En su lugar, utilizamos plantillas personalizadas y codificadas.  Luego se llaman en `html_theme_options` en `conf.py`.

## Creación del manual a nivel local

El manual está construido con Sphinx y el `pydata_sphinx_theme`.

- `make clean` Elimina todos los archivos del directorio `build`
- `make html` Crea el sitio y publica el contenido HTML en el directorio de compilación. Ejecute un servidor Python con `python -m http.server -d build/html/` para obtener una vista previa del sitio. Será necesario reconstruir el sitio con cada cambio.

También puedes usar `sphinx-autobuild` para reconstruir el sitio y volver a cargar el navegador cada vez que se realicen cambios con `sphinx-autobuild source/ build/html/`

## Cambios en `conf.py`

Tras configurar el tema, se necesitaron los siguientes cambios adicionales en `conf.py`.  Tenga en cuenta que esta lista no incluye cambios que solo reflejen la identidad de The Carpentries (configuración del nombre, identificadores de redes sociales, etc.).  La lista incluye los cambios que afectan a la funcionalidad del sitio.

- Para que la plantilla represente correctamente los archivos de marcado, añada `.md` a la lista `source_suffix` y añada `myst_parser` a la lista de `extensions`
- Para usar una hoja de estilos personalizada, defina `html_static_path = ['_static'] `y `html_css_files = ['css/custom.css']`
- Añade la configuración de la barra de navegación y la barra lateral a `html_context`
- Para usar encabezados como enlaces de anclaje, agrega `myst_heading_anchors = 6`
- Para eliminar las advertencias sobre la duplicación de encabezados en los documentos, agrega `suppress_warnings = ['autosectionlabel.*'] `

## Enlaces útiles

- [Tema Pydata Sphinx] (https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html)
- [Documentación general sobre Sphinx] (https://www.sphinx-doc.org/en/master/usage/configuration.html)
