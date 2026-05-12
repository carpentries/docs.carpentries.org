# Publicar una lección

**Tenga en cuenta que los mantenedores de clases de carpintería de datos, carpintería de bibliotecas y carpintería de software no deberían publicar las lecciones por el momento.**
El equipo curricular coordinará este proceso en los próximos meses.

Publicar la lección con regularidad les brinda a usted y a sus colaboradores la oportunidad de celebrar las mejoras que se han realizado y les facilita recibir crédito y reconocimiento por el trabajo que han realizado.
Es particularmente importante publicar la lección cuando alcance los hitos clave de su desarrollo, por ejemplo, antes de [los talleres piloto beta] (lesson-pilots.md) o cuando alcance [un estado estable] (./lesson-life-cycle.md).

Si [publicas la lección en Zenodo] (#publishing-the-lesson-on-zenodo) cuando la publiques, recibirás un identificador de objeto digital que tú y otras personas podrán usar para hacer referencia a la lección o a una versión en particular.
Publicar la lección hace que otras personas puedan encontrarla más fácilmente y, si incluyes tu identificador [ORCID iD] (https://info.orcid.org/what-is-orcid/) en la información sobre sus autores, te ayuda a incluir el proyecto en tu perfil público.

## Preparándose para un lanzamiento

### Actualización de la información de citas

Los repositorios de lecciones pueden contener información de citas en [Formato de archivo de citas] (https://citation-file-format.github.io/).
El plan de estudios de la capacitación para el desarrollo colaborativo de lecciones incluye [algunas explicaciones sobre por qué deberías incluir este archivo en tu repositorio de lecciones] (https://carpentries.github.io/lesson-development-training/collaborating-newcomers.html#helping-people-cite-your-lesson).
La documentación de Carpentries Workbench describe con más detalle [cómo se puede incluir el archivo en el repositorio] (https://carpentries.github.io/sandpaper-docs/editing.html#making-your-lesson-citable) y ofrece un ejemplo.

Le recomendamos que mantenga actualizada la información de las citas a medida que avance en el desarrollo y el mantenimiento de la lección.
Como mínimo, debes asegurarte de que la información de tu `Citation.cff` esté actualizada antes de publicar una nueva versión de la lección, ya que esto simplificará el proceso de publicación en Zenodo.

## Publicar la lección en Zenodo

- Primero, crea una cuenta [Zenodo] (https://zenodo.org/) si aún no tienes una, vinculada a tus credenciales de GitHub.
- Inicia sesión en Zenodo y selecciona «GitHub» en el menú desplegable de la esquina superior derecha.
- En esa página, busca el nombre de tu repositorio de lecciones en la lista y activa el interruptor para activar la integración entre Zenodo/GitHub.
- [Publica tu lección] (https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) desde su repositorio de GitHub. Esto creará un registro de Zenodo a partir de esa versión. Zenodo actualizará este registro con una nueva versión cada vez que publiques otro lanzamiento desde tu repositorio de lecciones.
- Edita la entrada de Zenodo para ajustar cualquier cosa que no esté bien.
  Por ejemplo, la presencia de un archivo `Citation.cff` en su repositorio hará que Zenodo piense que se trata de un registro que describe el software.
  Puede corregir esto a «Lección» en el campo _Tipo de recurso_.
- Agregue el DOI de su registro a los archivos `README.md` y `Citation.cff` del repositorio de lecciones.
  El registro creado a partir de tu publicación incluirá dos DOI: uno para la versión específica publicada esta vez y un segundo DOI de «nivel superior» que siempre se resolverá con la última versión de la lección publicada.
  Le recomendamos que añada el DOI de «nivel superior» a los archivos de su repositorio de lecciones. Zenodo te da un código Markdown para mostrar un icono de «insignia», por ejemplo! [DOI] (https://zenodo.org/badge/DOI/10.5281/zenodo.8415001.svg) en tu repositorio README.
  Busca el campo DOI en el cuadro _Detalles_ situado a la derecha de la página de registro para encontrar tu insignia.

