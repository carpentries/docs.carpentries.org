# El ciclo de vida de las lecciones

\*\*Nota sobre _instructores_ y _instructores_: \*\* en la mayor parte de este manual nos referimos a los instructores, con mayúsculas para indicar que se trata de un puesto certificado dentro de la comunidad, es decir, alguien que ha completado la formación de instructores de carpintería.
Parte del contenido de nuestro manual sobre el desarrollo curricular hace referencia a los instructores (sin usar mayúsculas), para distinguir entre aquellos que imparten un taller pero es posible que aún no sean instructores certificados.

La comunidad de Carpentries desarrolla las lecciones como proyectos de código abierto: las lecciones y sus archivos fuente suelen estar disponibles en línea desde las primeras etapas de desarrollo en adelante.
Puede resultar útil para los visitantes de una lección (profesores que están pensando en enseñarla, posibles colaboradores que exploran su contenido, etc.) y para los propios desarrolladores, poder identificar rápidamente el estado de desarrollo de una lección.
El desarrollo de las lecciones es un proceso iterativo, en el que el contenido y el diseño siempre están sujetos a evolución y mejora.
Por ejemplo, cuando se reciben comentarios cuando se enseña una nueva lección o en respuesta a nuevas funciones y otros cambios en el tema.
Con el tiempo, el contenido suele ser más completo, preciso, impactante y estable, y los cambios, especialmente las modificaciones importantes, como la reorganización o la adición o eliminación de secciones enteras, se vuelven menos frecuentes.

The Carpentries etiqueta el estado de desarrollo de las lecciones en un sistema similar al que se usa en el desarrollo de software: las clasificamos según su madurez y estabilidad, desde _prealfa_ hasta _estable_.

! [El modelo del ciclo de vida de la lección de carpintería] (../../img/life_cycle.svg)

- **_Pre-alpha:_** la lección se encuentra en las etapas iniciales de diseño y desarrollo.
  Es probable que el contenido de las lecciones prealfa esté incompleto y no haya sido probado, y puede sufrir cambios importantes en cualquier momento. Por lo general, esta etiqueta se aplica a una lección hasta que se haya completado un primer borrador.
- **_Alpha:_** la lección está siendo puesta a prueba por sus desarrolladores.
  Es probable que el contenido de las lecciones en versión alfa esté completamente redactado, pero se pueden esperar algunas lagunas, inconsistencias y errores.
  Por lo general, esta etiqueta se aplica a una lección después de que se haya completado su primer borrador y antes de que tengan lugar los primeros talleres piloto.
- **_Beta: _** la lección está lista para que la prueben otros instructores.
  El contenido de las lecciones de la versión beta ha sido probado por (al menos) sus desarrolladores, y el contenido se ha ajustado en función de esa experiencia.
  El contenido incluye orientación para los profesores sobre cómo enseñarlo de forma eficaz.
  Es probable que haya más cambios, a medida que se incorporen los comentarios de otros talleres piloto.
  Esta etiqueta se suele aplicar a una lección cuando sus desarrolladores están seguros de que está lista para ser utilizada en talleres por otros profesores.
- **_Stable:_**: la lección se ha sometido a pruebas exhaustivas y no se esperan cambios importantes (sin previo aviso).
  El contenido de las lecciones estables seguirá cambiando de vez en cuando, pero los cambios suelen ser pequeños y no afectan en gran medida a la capacidad del instructor para enseñarlas si está familiarizado con una versión anterior (estable).
  Por lo general, esta etiqueta se aplica a una lección después de que se hayan incorporado los comentarios de los talleres piloto de la versión beta.

La fase del ciclo de vida de una lección se muestra de forma destacada en la parte superior de la página en los sitios web de las lecciones.
También está visible como un «tema» en el repositorio de GitHub de la lección, debajo del cuadro _Acerca de_ en la parte derecha de la página de inicio del repositorio.

## ¿Cómo se establece la etapa del ciclo de vida?

El estado del ciclo de vida de una lección se puede ajustar modificando el parámetro `life_cycle` en el archivo `config.yaml` de la lección, así como el tema equivalente en el repositorio de GitHub de origen.

## ¿Quién es responsable de elegir la etapa del ciclo de vida de una lección?

Para las lecciones de propiedad comunitaria en The Carpentries Incubator, los desarrolladores de las lecciones pueden elegir la etiqueta que consideren apropiada.
Las lecciones de propiedad comunitaria en The Carpentries Lab han pasado la revisión por pares y deberían marcarse como estables.
La etapa del ciclo de vida de las lecciones que pertenecen a un programa de lecciones de Carpentries debe cambiarse tras consultar con el Comité Asesor Curricular correspondiente y/o el equipo curricular.
La consulta es especialmente importante antes de marcar una lección como beta o estable.

## ¿Qué ocurre en cada etapa del ciclo de vida?

Los [talleres piloto] (lesson-pilots.md) son probablemente los eventos más importantes que tienen lugar antes de que una lección alcance la estabilidad.
Sin embargo, aquí hay otras acciones que los desarrolladores de lecciones pueden tomar en diferentes etapas:

- \*\*Pre-alfa: \*\*
  - [Envía la lección a The Carpentries Incubator] (https://github.com/carpentries-incubator/proposals/).
  - Únase a [Capacitación colaborativa para el desarrollo de lecciones] (https://carpentries.org/lesson-development-training).
  - Convocatoria de colaboradores.
  - Si tiene la intención de que la nueva lección se una a un plan de estudios o programa de lecciones de Carpentries existente, consulte al [Comité Asesor Curricular] (https://carpentries.org/curriculum-advisors/) o al [Comité de Gobierno del Programa de Lecciones] (https://carpentries.org/community/lesson_program_governors/) correspondiente lo antes posible.
    Estos grupos de gobierno comunitario pueden proporcionar comentarios sobre sus planes y ofrecer orientación sobre cómo garantizar la integración exitosa de la nueva lección.
- \*\*Alfa: \*\*
  - Realice [talleres piloto alfa] (lesson-pilots.md#alpha-and-beta-pilots) y repita el diseño y el contenido de la lección.
  - Aumente la conciencia sobre la lección en la comunidad de The Carpentries.
- \*\*Beta: \*\*
  - Busca profesores que puedan impartir la lección en [talleres piloto beta] (lesson-pilots.md#alpha-and-beta-pilots) y recaba sus comentarios para mejorar aún más la lección.
    Considera la posibilidad de invitar a esos [instructores de la versión piloto de la versión beta] (./lesson-development-roles.md#beta-pilot-instructors) a unirse al equipo que desarrolla o mantiene la lección.
  - [Publica la lección en Zenodo y obtén un DOI] (./lesson-release.md).
  - [Envíe la lección para su revisión por pares en The Carpentries Lab] (https://github.com/carpentries-lab/reviews/).
- \*\*Estable: \*\*
  - [Publicar la versión estable en Zenodo] (./lesson-release.md).
    - Es posible que desee repetir este proceso con regularidad, por ejemplo, hacer publicaciones anuales.

! [El modelo del ciclo de vida de la lección de carpintería está anotado para mostrar más detalles de lo que puede suceder en cada etapa del proceso] (../../img/life_cycle_annotated.svg)
