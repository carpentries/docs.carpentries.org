# Páginas de resumen del plan de estudios

De forma predeterminada, The Carpentries Workbench está diseñado para crear [sitios web de lecciones que constan de varias páginas de episodios] (./curriculum-structure.md), que reflejen la estructura típica de nuestras lecciones.
Sin embargo, a veces es útil poder ofrecer un sitio de «lecciones» de una sola página, normalmente como una descripción general o «página de inicio» para una colección de lecciones que van juntas ([a esto lo llamamos _curriculum_] (./curriculum-structure.md)).

En Workbench, esto se admite con el parámetro opcional `overview` del archivo de configuración global (`config.yaml`).
Agregar `overview: true` como una nueva línea a `config.yaml` evita que la infraestructura genere un error si no hay ningún archivo en la carpeta `episodes`. La página principal del sitio de información general se crea a partir de `index.md` y `learners/setup.md`, como de costumbre.

## ¿Qué debe contener una página de resumen?

Los desarrolladores de lecciones pueden optar por rellenar estas páginas como quieran.
Estas son algunas recomendaciones sobre qué incluir:

- Una breve descripción del plan de estudios en su conjunto, incluido su público objetivo y los resultados de aprendizaje más importantes.
- Una lista de los conocimientos previos para el plan de estudios. (Esto se puede formatear como un div cerrado con la clase `prereq`).
- Una tabla en la que se describen las lecciones incluidas en el plan de estudios y el orden recomendado en el que se deben impartir.
  - Si existen varias rutas posibles en su plan de estudios, estas deben describirse como tablas individuales o en algún texto introductorio antes de mostrar la tabla de todas las lecciones. Si existen muchas rutas a lo largo de tus lecciones, descríbelas en una página separada creada a partir de un archivo fuente de la carpeta `learners/` y enlaza a él desde `index.md`.
- Las instrucciones de configuración, como la instalación del software y la descarga de datos, deben describirse en `learners/setup.md`.
  Al igual que en una lección sobre la configuración predeterminada, el contenido de esta página se anexará a la página de inicio del sitio.
- Si sus lecciones comparten un conjunto de datos de ejemplo común, es posible que desee describirlo en una página dedicada en este sitio de información general.
  Por ejemplo, esta página podría incluir un _diccionario de datos_ que describa las características del conjunto de datos, una breve descripción de sus orígenes, un enlace a los datos sin procesar y un enlace a más información (por ejemplo, una publicación con los datos originales).
  - Consulte la página [_Workshop Data_ de la descripción general del plan de estudios de ecología de la carpintería de datos] (https://datacarpentry.org/ecology-workshop/data.html) para ver un ejemplo.

Todos los elementos descritos anteriormente deben incluirse en el sitio de información general de un plan de estudios oficial de Carpentries.

## Markdown de plantillas para la tabla de descripción general del plan de estudios

Haz una copia de esta plantilla para ayudarte a crear una tabla de Markdown que describa las lecciones de tu plan de estudios.

```markdown
| **Lección** | **Resumen** |
|: ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
URL-of-lesson-site
URL-of-lesson-site 
agregar líneas en este formato hasta que hayas enumerado todas tus lecciones |
```
