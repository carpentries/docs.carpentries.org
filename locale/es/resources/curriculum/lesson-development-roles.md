# Funciones de desarrollo de la lección

\*\*Nota sobre _instructores_ y _instructores_: \*\* en la mayor parte de este manual nos referimos a los instructores, con mayúsculas para indicar que se trata de un puesto certificado dentro de la comunidad, es decir, alguien que ha completado la formación de instructores de carpintería.
Parte del contenido de nuestro manual sobre el desarrollo curricular hace referencia a los instructores (sin usar mayúsculas), para distinguir entre aquellos que imparten un taller pero es posible que aún no sean instructores certificados.
También puedes observar la misma distinción entre los _Maintainers_, que han completado la incorporación de mantenedores y se ocupan de una lección oficial de Carpentries, y los _mantenedores _, que se ocupan de las lecciones de la comunidad.

La creación de una nueva lección o plan de estudios es un proceso colaborativo, que generalmente involucra a muchos miembros de la comunidad que asumen diferentes roles. También es [un proceso iterativo] (./lesson-life-cycle.md), lo que significa que siempre se puede considerar que una lección está en desarrollo hasta cierto punto.

En esta página se describen las diferentes funciones que las personas pueden desempeñar en el diseño, el desarrollo, las pruebas y el mantenimiento de una nueva lección o plan de estudios.

- [Desarrolladores de lecciones] (#lesson-developers)
- [Instructores del taller piloto] (#pilot-workshop-instructors)
  - [Instructores de Alpha Pilot] (#alpha-pilot-instructors)
  - [Instructores de la beta piloto] (#beta-pilot-instructors)
- [Mantenedores] (#maintainers)
- [Revisores] (#reviewers)

## Desarrolladores de lecciones

Una lección puede tener uno o varios desarrolladores iniciales. Los desarrolladores redactan el contenido, las figuras y el código de la lección y crean los problemas de desafío apropiados. El equipo de desarrolladores debe contar con la experiencia adecuada en el campo (trabajar en el mismo campo que el público al que van dirigidos los materiales) y experiencia programática (es decir, utilizar regularmente las herramientas para las que están desarrollando lecciones en su propio trabajo). Desde un punto de vista técnico, los desarrolladores de las lecciones también deberán estar familiarizados con la infraestructura que utilizamos para desarrollar y alojar las lecciones de The Carpentries: principalmente git, GitHub y Markdown y/o R Markdown. Si no te sientes cómodo con alguna o todas estas herramientas, puedes usar algunos de los recursos que se enumeran a continuación para aprender y practicar con ellas.

La redacción de una lección es solo una parte del proceso de desarrollo: las nuevas lecciones deben probarse minuciosamente en [_talleres pilotos_] (lesson-pilots), ajustarse en respuesta a los comentarios y, luego, actualizarse y mantenerse a largo plazo. [Este ciclo de vida de una lección se analiza con más detalle en otra parte de este manual] (lesson-life-cycle.md).

### Recursos para desarrolladores de lecciones

- Nuestra [Capacitación colaborativa para el desarrollo de lecciones] (https://carpentries.github.io/lesson-development-training/) enseña principios y buenas prácticas en el diseño y el desarrollo curricular, y habilidades de colaboración para ayudar al equipo de desarrollo de lecciones a trabajar en conjunto de manera efectiva. También presenta los fundamentos de la creación de contenido didáctico accesible con The Carpentries Workbench, las herramientas que utilizamos para crear sitios web de lecciones a partir de archivos fuente en un repositorio de GitHub.
- [Introducción a The Carpentries Workbench] (https://carpentries.github.io/sandpaper-docs/) proporciona una documentación más completa de la infraestructura de la lección.
- [Introducción a Markdown y GitHub] (https://carpentries.github.io/lesson-development-training/instructor/markdown-github-primer.html) enlaza con dos recursos que enseñan los fundamentos de dos herramientas fundamentales para el desarrollo de las lecciones en The Carpentries.

## Instructores del taller piloto

Nuestras lecciones están destinadas principalmente a impartirse en talleres, y su diseño y contenido deben probarse en ese entorno. Los comentarios deben recopilarse durante el taller e incorporarse a la lección. Nos referimos a los eventos en los que se prueba una nueva lección como _talleres pilotos_.
[La sección Talleres piloto de lecciones de este manual] (lesson-pilots) proporciona más información sobre estos eventos, incluidas plantillas y orientación sobre la logística de los eventos.

### Instructores de Alpha Pilot

Es común, pero no esencial, que los instructores del primer piloto de una nueva lección sean los desarrolladores de la lección original. Nos referimos a estos eventos como _pilotos alfa_ y representan una gran oportunidad para recopilar información y recibir comentarios anticipados que sirvan de base para el desarrollo futuro del contenido. Además de recopilar los comentarios de los alumnos, los instructores de Alpha Pilot deben tomar notas exhaustivas durante el evento. Recomendamos que los instructores piloto se reúnan lo antes posible después del taller, o al final de cada sesión de enseñanza, para analizar su experiencia y preparar una lista de puntos de acción para que los desarrolladores de las lecciones los aborden a fin de mejorar la lección.

### Instructores de Beta Pilot

Si se está considerando la posibilidad de incorporar la nueva lección al plan de estudios oficial de The Carpentries, los instructores de estos talleres piloto beta deben ser instructores de carpintería certificados que hayan impartido anteriormente al menos dos talleres de carpintería. Los instructores con este nivel de experiencia estarán más preparados para solucionar los problemas que surjan durante el taller y es más probable que proporcionen comentarios útiles después del taller. No se requieren instructores certificados para los pilotos beta de las lecciones que no se convertirán en el plan de estudios oficial de Carpentries.

Los instructores de la versión beta pueden ser mantenedores, asesores curriculares o cualquier miembro de la comunidad de Carpentries que no sean los desarrolladores de la lección original. De hecho, es probable que reclutar instructores piloto beta que ya estén desempeñando un papel activo en la lección sea fructífero, ya que estas personas invierten en llevar la lección a la madurez. Para dos talleres piloto beta, necesitarás al menos cuatro instructores. Los autores de las lecciones deben planificar una reunión virtual con los instructores piloto antes del taller para responder a las preguntas y brindar ayuda técnica con la configuración.

### Recursos para los instructores de talleres piloto

- [La sección Talleres piloto de lecciones de este manual] (lesson-pilots) incluye más información sobre el propósito de las lecciones piloto, orientación para los desarrolladores y anfitriones de las lecciones, plantillas para encuestas de comunicación y comentarios, etc.
- El episodio [Preparándose para enseñar] (https://carpentries.github.io/lesson-development-training/preparing.html) de la capacitación colaborativa para el desarrollo de lecciones proporciona orientación para los desarrolladores de lecciones que planifican pilotos alfa para una nueva lección.

## Mantenedores

Los mantenedores de las lecciones son esenciales para la viabilidad a largo plazo de una lección. A medida que se enseña una lección, los profesores y los alumnos identifican posibles puntos de mejora, ya sea corrigiendo un error tipográfico, simplificando el código o sugiriendo un cambio significativo en la narrativa de una lección. Los mantenedores supervisan proactivamente el repositorio de GitHub de sus lecciones para asegurarse de que los problemas y las sugerencias de mejora se aborden de manera oportuna. Los mantenedores también desempeñan un papel vital a la hora de comunicarse con los colaboradores, garantizando que nuestra comunidad esté a la altura de sus ideales al recibir y apreciar las contribuciones de todos, desde los que colaboran por primera vez hasta los miembros más antiguos de la comunidad de The Carpentries.
Las personas que actúan como mantenedores deben tener experiencia con las herramientas que se enseñan en la lección, idealmente usándolas a diario o semanalmente en su propio trabajo. Además, deben tener experiencia trabajando en un dominio relevante relacionado con la lección o experiencia trabajando con GitHub y las demás tecnologías que utilizamos para crear y alojar nuestras lecciones. Cada lección debe tener al menos dos responsables de mantenimiento, y es beneficioso para esos responsables tener diversos niveles de experiencia con el dominio y los aspectos técnicos de la lección, así como con las herramientas para el mantenimiento.

### Recursos para mantenedores

- El [Manual para mantenedores] (../../handbooks/maintainers.md) incluye orientación sobre las comunicaciones, la gestión del repositorio de lecciones y otros aspectos del puesto.
- El [plan de estudios de incorporación de mantenedores] (https://carpentries.github.io/maintainer-onboarding/) contiene la información que proporcionamos a los mantenedores para las clases oficiales de Carpentries cuando comienzan a desempeñar el puesto.
- [Introducción a The Carpentries Workbench] (https://carpentries.github.io/sandpaper-docs/) proporciona una documentación más completa sobre la infraestructura de las lecciones: las herramientas que utilizamos para crear sitios web de lecciones a partir de los archivos fuente de un repositorio de GitHub.

## Asesores curriculares

(Aunque los asesores curriculares pueden ser muy útiles para el desarrollo de cualquier lección o plan de estudios nuevo, solo son necesarios para el plan de estudios oficial de Carpentries).

Mientras que los desarrolladores y mantenedores de las lecciones se encargan de la mejora y el mantenimiento diarios de las lecciones, los asesores curriculares brindan orientación de nivel superior sobre la dirección de ese desarrollo. Los asesores curriculares deben ser expertos en el dominio de la lección y conocer la forma en que las habilidades que enseña se aplican (o deben aplicarse) en ese dominio. Los asesores curriculares asumen la responsabilidad de guiar el desarrollo de un [plan de estudios] completo (./curriculum-structure.md): cuando ese plan de estudios consta de varias lecciones, los asesores curriculares deben considerar cómo debe desarrollarse en su conjunto y cómo los cambios en una lección pueden afectar a las demás.

Si se pretende incorporar una nueva lección a un plan de estudios existente, los desarrolladores de la lección deben consultar al Comité Asesor Curricular existente sobre sus planes lo antes posible en el proceso de desarrollo. Por ejemplo, los desarrolladores de la lección pueden compartir una descripción general del diseño planificado y el contenido de la lección antes de invertir mucho tiempo en la creación del material. Esta consulta temprana permite a los asesores curriculares comentar la lección planificada, evaluar la facilidad con la que se adaptará al plan de estudios existente y considerar el impacto que puede tener en otras lecciones del mismo.

### Recursos para asesores curriculares

El [Manual de asesores curriculares] (/handbooks/curriculum_advisors.md) incluye más información sobre el puesto, la logística de cómo se administran los comités asesores curriculares, etc.

## Revisores

La retroalimentación es esencial para el desarrollo de una lección eficaz. El objetivo principal de [talleres piloto] (lesson-pilots.md) es proporcionar comentarios que los desarrolladores puedan utilizar para mejorar el diseño y el contenido de su nueva lección. En este sentido, los instructores de los talleres piloto pueden considerarse revisores importantes, especialmente aquellos que dirigen y proporcionan comentarios sobre los pilotos beta. Sin embargo, puede resultar beneficioso solicitar comentarios adicionales por parte de los revisores. Los revisores deben centrar su evaluación de una lección en su utilidad como recurso de aprendizaje y enseñanza accesible, en su idoneidad para su público objetivo declarado y en la precisión de su contenido.
Los desarrolladores de las lecciones pueden encontrar revisores a través de sus propias redes o comunicándose con la comunidad en general para solicitar voluntarios. Los revisores pueden enviar comentarios y sugerir mejoras directamente, en forma de problemas y solicitudes de cambios en el repositorio de lecciones, o por correo electrónico o mediante un debate. The Carpentries también alberga una plataforma para la revisión por pares estructurada y abierta de las lecciones por parte de la comunidad.

### Revisión abierta por pares de las lecciones en The Carpentries Lab

[The Carpentries Lab] (https://carpentries-lab.org/) organiza lecciones propiedad de la comunidad que han pasado la revisión por pares y proporciona una plataforma para que se lleve a cabo el proceso de revisión por pares.
Las reseñas existen como discusiones sobre temas visibles públicamente en [el repositorio de reseñas de laboratorio] (https://github.com/carpentries-lab/reviews/). Los miembros de la comunidad de The Carpentries se ofrecen como voluntarios como revisores y editores del laboratorio.

### Recursos para revisores

- La documentación del repositorio de reseñas de laboratorios de Carpentries proporciona [más información sobre el proceso de revisión por pares] (https://github.com/carpentries-lab/reviews?tab=readme-ov-file#what-is-the-process-for-submitting-a-lesson-to-the-carpentries-lab) y [la orientación proporcionada a los revisores] (https://github.com/carpentries-lab/reviews/blob/main/docs/reviewer_guide.md).
- The Carpentries [Entrenamiento colaborativo para el desarrollo de lecciones] (https://carpentries.github.io/lesson-development-training/) proporciona orientación sobre las mejores prácticas en el diseño de las lecciones y el desarrollo del contenido, que se puede utilizar para informar las revisiones de las lecciones.

