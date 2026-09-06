# Manual para desarrolladores de lecciones

## Acerca de este manual

El Manual para desarrolladores de lecciones está diseñado para ayudar a los miembros de la comunidad
de Carpentries que se desempeñan como desarrolladores de lecciones. Lo mantiene el equipo curricular de The Carpentries.  Si cree que es necesario añadir o actualizar algo aquí, o si desea enviar comentarios sobre el contenido, envíe un correo electrónico al {{'[Curriculum Team] (mailto:{}) '.format (curriculum_email)}} o abra una edición en el {{' [repositorio fuente de este manual] ({}) '.format (gh_repo)}}. Si no está familiarizado con alguno de los términos utilizados en este manual, consulte nuestro {{'[Glosario de términos] ({}) '.format (glossary)}}.

## Funciones y responsabilidades

Más allá de garantizar que la lección cumpla con los requisitos
para su inclusión en [The Carpentries
Incubator] (https://github.com/carpentries-incubator/proposals/blob/main/README.md#what-are-the-requirements-for-being-included-in-the-carpentries-incubator),
, no hay responsabilidades formales asociadas con el desarrollo de una lección
allí: los proyectos de lección en la incubadora son esfuerzos comunitarios que
pertenecen a los desarrolladores individuales que contribuyen a ellos. Estos desarrolladores
pueden optar por administrarlos y dedicarles tiempo según
según sus preferencias y disponibilidad.

Para garantizar la continuidad y la sostenibilidad de su proyecto de la lección
, The Carpentries recomienda que los desarrolladores de lecciones hagan responsables a
de las siguientes tareas:

- Gestionar el diseño y el desarrollo de la lección.
- Leer, responder y (cuando sea necesario) gestionar los problemas
  denunciados por los miembros de la comunidad.
- Dar la bienvenida y revisar las solicitudes de cambios y otras contribuciones realizadas por los miembros de la comunidad
  .
- Comunicarse con la comunidad sobre el desarrollo continuo de la lección
  .
- Reclutar instructores para probar la lección en versión beta, apoyar los preparativos de
  para los talleres piloto e incorporar los comentarios de
  en esos talleres.
- Enviar la lección para su revisión abierta por pares y su aceptación a [The
  Carpentries Lab] (https://carpentries-lab.org).

## Incorporación

Los desarrolladores de lecciones pueden empezar una nueva lección en cualquier momento abriendo un nuevo número
en [The Carpentries Incubator Proposals
repository] (https://github.com/carpentries-incubator/proposals/issues/new?assignees=&labels=&template=issue_proposal.md).
La plantilla del número incluye varias preguntas, que deben responderse
para ayudar al equipo curricular a configurar correctamente el repositorio de lecciones en
the Incubator.

Los miembros de la comunidad que tengan una idea para una nueva lección también pueden postularse para unirse a la capacitación colaborativa para el desarrollo de lecciones
, que se programará en
periódicamente a partir de 2023.

## Desembarque

No existe un proceso formal de baja para los desarrolladores de lecciones que trabajan en proyectos
en The Carpentries Incubator.

Para garantizar la continuidad y la sostenibilidad del proyecto, The
Carpentries recomienda que los desarrolladores de lecciones tomen las siguientes medidas
cuando abandonen una lección:

- Comunique la decisión a los demás desarrolladores de la lección, para que
  puedan redistribuir las tareas y planificar el proyecto en consecuencia.
- Reasigna cualquier problema que se les haya asignado a otro miembro del equipo de desarrollo de la lección
  .
- Elimine su nombre del archivo README de la lección y de cualquier otro lugar donde figuren los autores
  de la lección.
- Pide al propietario del proyecto (un desarrollador con acceso de administrador al repositorio
  ) que revoque los privilegios del desarrollador saliente en el repositorio de lecciones de
  .
- Si el único desarrollador de la lección que queda abandona el proyecto,
  añade un aviso en la parte superior del archivo README del repositorio y en la página
  de la primera página de la lección (`index.md`) para informar a los visitantes de que la lección no se está manteniendo/desarrollando activamente
  . En estas circunstancias, considere lo siguiente:

  1. ponerse en contacto con el [equipo de administración de la incubadora] (mailto:incubator@carpentries.org) para informarles que la lección no se mantendrá, y
  2. archivar el repositorio de lecciones.

Si los desarrolladores desean eliminar la lección de The Carpentries
Incubator, el propietario del proyecto (un desarrollador con acceso de administrador) puede
transferir el repositorio de lecciones fuera de la organización GitHub
`carpentries-incubator` a través de **Settings**->\ **General**->\ **Danger
Zone**->\ **Transferir la propiedad**.

## Espacios de comunicación y colaboración

### Calendario comunitario

Una vez programadas, todas las sesiones de coworking para el desarrollo de las lecciones figuran en
nuestro [Calendario
de la comunidad] (https://carpentries.org/community/events/). Tú
puedes añadir eventos relevantes a tu calendario personal desde allí haciendo clic en
en el evento al que te gustaría asistir.

### Etherpad

The Carpentries usa [Etherpad] (/resources/communications/etherpads.md) como una herramienta colaborativa para tomar notas durante talleres, capacitaciones y otros eventos relacionados con Carpentries. A continuación se muestra una lista de Etherpads relevantes para trabajar como desarrollador de lecciones.

- [Pad-of-Pads] (https://pad.carpentries.org/pad-of-pads): Una lista de
  nuestros Etherpads y otros recursos más utilizados.
- [Notas de la sesión de coworking
  para el desarrollo de la lección] (https://codimd.carpentries.org/lessondev-coworking): información de registro
  , detalles de conexión y notas tomadas de las sesiones de coworking mensuales de
  (CodiMD),

### GitHub

- [Repositorio
  de las propuestas de la incubadora de Carpentries] (https://github.com/carpentries-incubator/proposals): un lugar
  para que la comunidad de The Carpentries proponga nuevas lecciones para el desarrollo de
  en la incubadora.
- [Repositorio
  de The Carpentries Lab Reviews] (https://github.com/carpentries-lab/reviews): un lugar
  para que los desarrolladores de lecciones envíen las lecciones para su revisión abierta por pares y su aceptación
  en The Carpentries Lab.

### Slack

{{'[Únete al espacio de trabajo de The Carpentries Slack] ({}) '.format (slack_invite)}}. Para seguir las conversaciones relacionadas con este puesto, debes unirte a los siguientes canales:

- El canal #lesson -dev del espacio de trabajo de Slack de The Carpentries es una plataforma para que toda la comunidad formule preguntas y participe en debates sobre el tema del desarrollo de las lecciones.
- Recomendamos a los desarrolladores de lecciones que busquen en los canales existentes en el espacio de trabajo
  de Slack los que sean relevantes para el tema o el dominio de
  de su lección.
- También puede resultar útil crear un nuevo canal para la lección, como un espacio
  para que debas hablar del proceso de desarrollo con los colaboradores,
  y para que los miembros de la comunidad hagan preguntas sobre la lección.

Si no conoces Slack, nuestra {{"[Guía de Slack] ({})» .format (slack_guide)}} te ayudará a configurar tu perfil y te dará una visión general de cómo utilizamos la plataforma en el día a día.

### Lista de correo

Puedes acceder a las listas de correo de The Carpentries desde
[TopicBox] (https://carpentries.topicbox.com/latest). La
[lista de correo de desarrolladores de incubadoras] (https://carpentries.topicbox.com/groups/incubator-developers)
es la más relevante para desempeñar este cargo.

Para unirse a una o más listas de correo de Carpentries, necesitará [crear un inicio de sesión en el sitio] (https://carpentries.topicbox.com/latest). Una vez hecho esto, puede desplazarse por la lista de grupos y hacer clic en «Unirse a la conversación» (para abrir el correo) o «Solicitar unirse» (para las listas de correo que requieren la aprobación del administrador). Si eres nuevo en Topicbox, consulta nuestra {{"[Topicbox Guide] ({})» .format (topicbox_guide)}}.

## Guías paso a paso

### Uso de etiquetas de problemas para promover la colaboración

GitHub permite a los mantenedores de un repositorio agregar información contextual
a los problemas y solicitudes de cambios en forma de etiquetas.
[The Carpentries usa un conjunto ampliado de etiquetas de temas en sus repositorios de lecciones] (../resources/curriculum/issue-labels.md).

Se pueden implementar dos etiquetas, utilizadas por The Carpentries y en muchos repositorios de GitHub,
para aumentar la visibilidad de tu lección y alentar a los miembros de la comunidad de
a contribuir a su desarrollo.

La etiqueta \*\* «se busca ayuda» \*\* debe usarse para resaltar los problemas con
para los que agradecería recibir ayuda adicional. El sitio web
de Carpentries incluye una [página Se busca ayuda
] (https://carpentries.org/help-wanted-issues/), que
puede listar automáticamente todos los números etiquetados como «se busca ayuda» en los repositorios
de The Carpentries, Software Carpentry, Data Carpentry, Library
Carpentry, CarpentriesLab y The Carpentries Incubator. Descubre cómo
incluir temas de tu repositorio de lecciones en la página Se busca ayuda. Para ello,
revisa la [Información para los mantenedores de
] (https://carpentries.org/help-wanted-issues/#for-maintainers)
en la propia página.

La etiqueta \*\* «buen primer número» \*\* debe usarse para identificar los problemas en los que
sería un buen punto de partida para los recién llegados que buscan una forma de contribuir con
a su lección. Por lo general, el trabajo necesario para cerrar un problema con esta etiqueta
no requeriría un conocimiento exhaustivo de la estructura
o las complejidades del repositorio de lecciones, ni una comprensión experta
del contenido. La etiqueta «buen primer número» se usa tan ampliamente
que GitHub proporciona una página en\ `[URL del repositorio
] /contribute <https://github.com/swcarpentry/r-novice-gapminder/contribute>`__
para cada repositorio, en la que se enumeran los problemas con esta etiqueta.

### Agregar etiquetas de temas a un repositorio de lecciones

{{'[Las lecciones oficiales de los programas de lecciones de The Carpentries] ({}/lessons/) '.format (carpentries_website)}} aparecen en el sitio web de The Carpentries, según los metadatos que describen la lección. Estos metadatos se agregan en forma de etiquetas de temas en el repositorio de lecciones. Estas etiquetas de tema deben configurarse lo antes posible una vez que la lección se haya creado o agregado a la Incubadora. Algunos son esenciales y provienen de un conjunto limitado de valores, mientras que otros son más flexibles. La siguiente tabla contiene una guía sobre los tipos y la cantidad de etiquetas de tema que debe tener cada repositorio de lecciones.

| Categoría    | Ejemplo                  | Número | Descripción                                                                                                                                                                                                      |
| ------------ | ------------------------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lección      | lección                  | 1      | Debe ser una lección para figurar en la página de lecciones desarrolladas por la comunidad                                                                                                                       |
| Ubicación    | carpintería de datos     | 1      | Una descripción del programa de lección al que pertenece la lección con palabras separadas por guiones (es decir, carpintería de software, carpintería de datos y carpintería de bibliotecas) |
| Idioma       | español                  | > 0    | El (los) idioma (s) en el que está disponible la lección                                                                                                                   |
| Escenario    | estable                  | 1      | La etapa actual de desarrollo de la lección                                                                                                                                                                      |
| Dominio      | ecología microbiana      | 1-2    | Los dominios de alto nivel de la lección para una categorización general                                                                                                                                         |
| Herramientas | pitón                    | 1-3    | La (s) herramienta (s) principal (es) que se enseña (n) en la lección                                                                |
| Habilidades  | clasificación taxonómica | 1-3    | La (s) habilidad (s) principal (es) enseñada (s) en la lección                                                                       |

El equipo del plan de estudios lo ayudará a establecer las etiquetas de tema
apropiadas para su lección. Para garantizar la coherencia en todos los repositorios de la lección
desarrollados por la comunidad de The Carpentries, consulta
a [este listado] (https://docs.google.com/spreadsheets/d/1KkmBtCu4PaNb5nzJAD82UHcfHQlaPY84qPVxw8WO8es/edit?usp=sharing)
de las etiquetas de tema que se utilizan actualmente en The Carpentries Incubator y reutiliza
estos valores cuando corresponda, creando nuevas etiquetas de tema donde no exista ninguna etiqueta
preexistente para tu lección.

### [Cómo organizar un sprint de desarrollo de lecciones] (/resources/curriculum/lesson-sprint-recommendations.md)

A muchos desarrolladores de lecciones les resulta útil organizar un evento específico para avanzar y mejorar la colaboración en sus proyectos de lecciones.
Este recurso proporciona un conjunto de recomendaciones sobre cómo organizar un evento de sprint efectivo e inclusivo para el desarrollo de las lecciones.

### Promocionar su proyecto en el centro de atención de la lección de incubadora

The Incubator Lesson Spotlight es un artículo habitual del blog y boletín
de The Carpentries, en el que se destaca una lección que actualmente se está desarrollando en la comunidad
. El propósito de la serie Spotlight es aumentar la visibilidad
de esa lección entre la comunidad en general y alentar a los miembros de la comunidad
a contribuir al desarrollo posterior de esa lección
.

Cualquier lección de [The Carpentries
Incubator] (https://github.com/carpentries-incubator/) puede ser incluida en la serie
, independientemente de la etapa de desarrollo en la que se encuentre actualmente la lección
. Es una buena manera de que las lecciones que se encuentran en las primeras etapas
del desarrollo atraigan a nuevos colaboradores, y para que las que estén en las etapas posteriores de
inviten a otras personas a revisar la lección de manera informal e intentar que
enseñe el material. Para enviar tu lección para que aparezca en la serie
, sigue los pasos que se indican a continuación.

1. Piensa en cómo puedes preparar tu lección para los nuevos colaboradores
   antes de que se publique la función. Esto podría implicar etiquetar los problemas
   existentes (por ejemplo, para que aparezcan en [la página Se busca ayuda
   ] (https://carpentries.org/help-wanted-issues/)) o crear
   nuevos, asegurarse de que su contributing.md está actualizado o
   planificar la publicación de la función Spotlight para que se ajuste a un período
   relativamente tranquilo de su agenda, de modo que pueda responder
   con prontitud a cualquier nueva edición o solicitud de cambios.
2. Complete el [formulario
   de envío de contenido destacado de Incubator Lesson] (https://docs.google.com/forms/d/e/1FAIpQLScJimGMtzqAFE-Tii-LvbfGZqtKj0OC4ken7_Qdlta8uZXAUA/viewform),
   con los detalles de la lección que se incluirá en la función. Puede que
   sea beneficioso colaborar en este contenido con otros desarrolladores
   que estén trabajando en la lección. El equipo principal de Carpentries utilizará el contenido
   incluido en el formulario para crear una entrada para el [blog The Carpentries
   ] (https://carpentries.org/blog/) y un artículo para
   , el [boletín Carpentries Clippings] (https://carpentries.org/newsletter/).
3. Cuando se haya redactado la entrada del blog, se abrirá una solicitud de extracción para que
   añada esa publicación al sitio web. Se te etiquetará para que realices una revisión
   (opcional) de esta solicitud de incorporación de cambios antes de que se publique. Para revisar la entrada del blog
   , lee el contenido de la publicación y comenta el hilo del número
   para solicitar cualquier cambio en la función.

### Cómo enviar una lección a The Carpentries Lab

The Carpentries Lab ofrece lecciones desarrolladas por la comunidad que han sido revisadas por pares
y los instructores pueden confiar en ellas para cumplir con el alto estándar
de calidad y estabilidad. El laboratorio proporciona una plataforma para la revisión abierta de las lecciones por pares
y para promover las lecciones que han ingresado a la colección
.

Para enviar una lección para su revisión por pares en The Carpentries Lab, sigue estos pasos
:

1. Consulta los [criterios de elegibilidad para las lecciones que se revisarán en el laboratorio
   ] (https://github.com/carpentries-lab/reviews#what-makes-a-lesson-a-good-candidate-for-the-carpentries-lab).
2. Abre un nuevo número en el repositorio [Reviews
   ] (https://github.com/carpentries-lab/reviews/issues/new?assignees=&labels=new-submission&template=submission.md&title=%5BREV%5D%3A+)
   y responde a las preguntas de la plantilla del número para informar a los editores
   sobre la lección.

### [Pilotando una lección] (/resources/curriculum/lesson-pilots.md)

Enseñar una lección por primera vez es muy gratificante, pero la experiencia de los instructores y los alumnos también identifica oportunidades para abordar y aclarar aún más partes del contenido.
Esto hace que las enseñanzas de las primeras lecciones, a las que denominamos _lecciones pilotos_, sean hitos cruciales en el desarrollo de una lección de alta calidad.
Este recurso proporciona más información sobre cómo probar una nueva lección en talleres, cómo estos talleres piloto se alinean con [el ciclo de vida de la lección] (/resources/curriculum/lesson-life-cycle.md) y orientación sobre logística, recopilación de comentarios relevantes, etc.

## Recursos

### [Introducción a The Carpentries Workbench] (https://carpentries.github.io/sandpaper-docs/)

Documentación para The Carpentries Workbench, la infraestructura de código abierto
para sitios web de lecciones. La documentación explica cómo instalar el banco de trabajo
para que los desarrolladores de la lección puedan editar y previsualizar sus lecciones
en su propio ordenador, cómo inicializar una nueva lección y utilizar los distintos elementos de
de la plantilla de la lección, y cómo mantenerse al día con
los últimos cambios en la infraestructura.

### [Currículo de capacitación para el desarrollo colaborativo de lecciones] (https://carpentries.github.io/lesson-development-training/)

Una lección diseñada para enseñar habilidades y buenas prácticas en el diseño de lecciones, el desarrollo del sitio web de la lección
y la colaboración a través de GitHub. Los miembros de la comunidad
pueden solicitar unirse a esta capacitación o seguir el plan de estudios de
en su tiempo libre.

### [Elegir una narración y un conjunto de datos para una lección] (/resources/curriculum/narrative-example-data.md)

Guía para los desarrolladores de lecciones a la hora de elegir una narración para su lección y datos de ejemplo para incluirlos en ella.
Incluye listas de puntos a tener en cuenta al elegir un conjunto de datos narrativo y de ejemplo, e información asociada sobre la concesión de licencias y la publicación de datos.

### [Plantilla de encuesta de comentarios sobre el taller piloto] (https://docs.google.com/forms/d/1OGCQBotD2nOJkc7KpFZLhFfb3EBcxEDwHz_3p48qz3U/template/preview)

Las encuestas estándar de Carpentries antes y después del taller no son compatibles con las lecciones piloto de
, por lo que tendrás que crear tus propias encuestas para enviar
antes o después de un taller piloto. Si bien las encuestas para los talleres piloto
suelen incluir preguntas específicas de la lección
en particular que se está probando, hay algunas preguntas estándar de retroalimentación que se pueden hacer
después de una prueba piloto para evaluar el diseño y el flujo de la lección. Esta encuesta
[plantilla posterior al taller piloto
] (https://docs.google.com/forms/d/1OGCQBotD2nOJkc7KpFZLhFfb3EBcxEDwHz_3p48qz3U/template/preview)
se puede copiar y adaptar para que se adapte a las necesidades de la lección, y compartir
con los alumnos en lugar de la encuesta estándar posterior al taller.

### [Talleres piloto de lecciones] (/resources/curriculum/lesson-pilots.md)

Información sobre por qué y cómo probamos las nuevas lecciones en los talleres, incluida la orientación y las plantillas para que las usen los anfitriones e instructores de los talleres piloto.

### Plantillas de anuncios beta

Una [entrada
del blog de anuncios de la versión beta] (https://docs.google.com/document/d/1z8QmxDIiew-p1d8aLzXa0vt0FLUHNtK3oS3tucyrRsI/edit?usp=sharing)
y un [mensaje de correo electrónico de anuncio de la versión beta de la plantilla
] (https://docs.google.com/document/d/1hHnm-Ljb_o_rNd9bvQ83ilq40KoGoEfMPTSrFS4QOj8/edit?usp=sharing)
para dar a conocer la versión beta de una lección. Se pueden usar para pedir a los miembros de la comunidad de
que se ofrezcan como voluntarios para organizar un taller piloto beta que ayude al desarrollo continuo de la lección de
.

### [Materiales de incorporación al plan de estudios] (/resources/curriculum/curriculum_onboarding.md)

Guía para desarrollar materiales que ayudarán a los profesores a prepararse para enseñar la nueva lección o plan de estudios.

### [Proceso de publicación de la lección] (/resources/curriculum/lesson-release.md)

Una descripción de cómo preparar el lanzamiento de una lección y publicarlo en Zenodo.

