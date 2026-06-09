# Bifurcación de un repositorio de lecciones de Workbench

Sigue estos pasos para ayudarte a configurar cuando bifurques un repositorio de lecciones en GitHub que utilice [The Carpentries Workbench] (https://carpentries.github.io/workbench/).

1. [Habilitar los flujos de trabajo de GitHub Actions] (#enable-the-github-actions-workflows)
2. [Activar páginas de GitHub] (#activate-github-pages)
3. [Configurar flujos de trabajo de mantenimiento] (#configure-maintenance-workflows)
4. [Obteniendo ayuda] (#getting-help)

## Habilitar los flujos de trabajo de GitHub Actions

Las acciones están deshabilitadas de forma predeterminada en los repositorios bifurcados.
Si quieres crear el sitio web de una lección a partir de los archivos de tu bifurcación, tendrás que activarlos.
\*\*Debes hacer esto antes de activar las páginas de GitHub en el repositorio. \*\*

1. Para activar GitHub Actions, navega hasta la pestaña _Acciones_ de tu repositorio.
   Deberías encontrar un botón que diga _ «Comprendo mis flujos de trabajo, actívalos» _, en el que puedes hacer clic.
   A continuación, debería mostrar una página con los flujos de trabajo del repositorio listados en el lado izquierdo.
2. Tres de los flujos de trabajo que aparecen en la barra lateral izquierda están programados para ejecutarse semanalmente y seguirán deshabilitados.
   Para habilitar la creación de sitios web de lecciones, seleccione el flujo de trabajo denominado `01 Crear e implementar sitio` y, a continuación, _Habilitar flujo de trabajo_ cerca de la parte superior derecha de la ventana.
3. Para ejecutar el flujo de trabajo de creación del sitio de lecciones por primera vez, seleccione el menú desplegable _Ejecutar flujo de trabajo_ (donde estaba el botón _Habilitar flujo de trabajo_ en el paso 2) y, a continuación, el botón _Ejecutar flujo de trabajo_.
   El proceso de compilación tardará unos minutos, tras lo cual se creará/actualizará la rama `gh-pages` de su repositorio para que contenga la última versión del sitio web de la lección.
   Ahora puedes [activar las páginas de GitHub] (#activate-github-pages) para enviar los archivos de esa rama a Internet.
4. Si desea configurar las ejecuciones de flujo de trabajo semanales para que puedan abrir automáticamente solicitudes de cambios para actualizar la infraestructura de la lección y la caché de paquetes (solo en las lecciones de R Markdown), debe repetir el paso 2 anterior para los otros dos flujos de trabajo deshabilitados, denominados `02 Mantener: actualizar archivos de flujo de trabajo` y `03 Mantener: actualizar caché de paquetes`.
   Una vez que se hayan activado esos flujos de trabajo, tendrá que [completar alguna configuración adicional, que se describe a continuación] (#configure-maintenance-workflows), antes de que se ejecuten correctamente.

## Activar páginas de GitHub

\*\*Una vez que hayas activado tus flujos de trabajo de GitHub Actions (consulta más arriba) \*\* puedes configurar las GitHub Pages para que sirvan tu sitio de lección desde la rama `gh-pages` de tu repositorio.

1. Abre la pestaña _Configuración_ de tu repositorio de lecciones y, a continuación, navega hasta _Páginas_ en _Código y automatización_ en la barra lateral izquierda.
2. En _Construir e implementar_, mantén seleccionada la opción _Implementar desde una rama_ y elige `gh-pages` en el menú desplegable de _Branch_.
3. Haz clic en _Guardar_.
4. Regresa a la página principal (pestaña _Código_) de tu repositorio de lecciones y selecciona el símbolo del engranaje en la parte superior derecha de la sección _Acerca de_.
   Marca la casilla _Usa tu sitio web de GitHub Pages _ para mostrar la URL del sitio web de la lección creado a partir de tu bifurcación.

## Configurar flujos de trabajo de mantenimiento

Cuando se configuran correctamente, los dos flujos de trabajo de mantenimiento, `02 Maintain: Update Workflow Files` y `03 Maintain: Update Package Cache`, pueden crear solicitudes de cambios en tu repositorio para mantener la infraestructura de la lección y (si la lección usa archivos fuente de R Markdown) los paquetes utilizados en la lección actualizados a medida que se publiquen nuevas versiones.
Para que esto funcione, debes crear un token de acceso que permita a los flujos de trabajo abrir solicitudes de cambios en tu nombre.

1. Abre <https://github.com/settings/tokens/new> e introduce el nombre `Sandpaper Token (<your github repository name>) `para tu token, por ejemplo, `Sandpaper Token (carpintería/lesson-development-training)`
2. Elige una vida útil para el token.
   Por motivos de seguridad, le recomendamos que no elija _Sin caducidad_. Pero **si sigues el siguiente paso**, el token solo se puede usar para realizar un número muy limitado de tareas en tu repositorio, por lo que tampoco es necesario que elijas una vida útil muy corta.
3. En _Seleccionar alcance_, marca la casilla del alcance del _flujo de trabajo_. (Esto hará que también se comprueben todos los ámbitos de _repo_).
4. Selecciona _Generar token_.
5. Se mostrará tu nuevo token de acceso personal, con un botón al lado que se puede usar para copiar el token al portapapeles.
   Copia el token y vuelve a la pestaña _Settings_ de tu repositorio de lecciones.
   En _Seguridad_ en la barra lateral izquierda, abre el menú desplegable _Secretos y variables_ y elige _Acciones_.
6. Introduzca `SANDPAPER_WORKFLOW` como nombre y pegue el token en el campo _Valor_.
7. Seleccione _Agregar secreto_ para completar la configuración.

## Obteniendo ayuda

Si tienes problemas con alguno de estos pasos, puedes pedir ayuda de la siguiente manera:

- Publicar en los canales `#workbench` y/o `#lesson -dev` de Slack ({{'[Únete al espacio de trabajo de Slack de The Carpentries] ({}) '.format (slack_invite)}}).
- [Ponerse en contacto con el equipo del plan de estudios por correo electrónico] (mailto:curriculum@carpentries.org).
- Abre un problema en tu repositorio, describe el problema que has encontrado y etiqueta `@tobyhodges`.

Para ayudar a otros a solucionar tu problema, incluye en tu mensaje una URL a tu repositorio bifurcado.
