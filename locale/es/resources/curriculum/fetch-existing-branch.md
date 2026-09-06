# Basándose en la sucursal existente de otra persona

En ocasiones, es posible que desees o necesites basarte en los cambios que otra persona ya ha introducido en una sucursal de un repositorio de lecciones, por ejemplo, [si ya no puede completar el trabajo y tú quieres ayudar a terminar su pull request] (/handbooks/maintainers.md#situation-1-a-pull-request-exists-but-is-incomplete).
En esta página, se describen dos maneras en las que puedes prepararte para construir sobre la base de los cambios que ya han realizado.
En las instrucciones se presupone cierta familiaridad con el control de versiones, Git y GitHub.

## 1. Bifurque su repositorio y sucursal

### Encuentra la bifurcación del colaborador original

Partiendo del pull request abierto en el que quieres seguir trabajando, desplázate hasta la parte superior de la pestaña _Conversación_.
Bajo el título del pull request, encontrarás un resumen de las ramas que se combinarían si el pull request se fusionara: por lo general, la organización del programa de la lección y «principal» a la izquierda, y el nombre de usuario del colaborador original y el nombre de la sucursal que eligió a la derecha (la «rama de funciones»).

! [Información de sucursal para una solicitud de extracción en GitHub. Se muestran el nombre de la rama predeterminada del repositorio oficial, `datacarpentry:main`, y de la rama de funciones del colaborador, `example-user:example-branch`.] (./img/branch-info-pr.png)

Al hacer clic en el nombre de la rama de funciones del colaborador, accederás a esa rama en su bifurcación del repositorio de lecciones.

### Haz tu propio tenedor con el de ellos

Desde esta página, puedes crear tu propia bifurcación de su repositorio con el botón «Bifurcación» situado en la parte superior derecha de la página.
Se abrirá un breve formulario en el que podrá establecer un nombre y una descripción para la nueva bifurcación que va a crear.
Lo importante aquí es \*\*desmarcar la casilla «Copiar solo la rama principal» \*\* para obtener también una copia de la rama de funciones en la que estaban trabajando para la solicitud de extracción.

! [El formulario que se presenta al bifurcar un repositorio existente en GitHub, con la casilla «Copiar solo la rama principal» sin marcar.] (./img/new-fork-all-branches.png)

### Editar la lección en GitHub

Después de crear tu bifurcación, usa el menú desplegable situado en la parte superior izquierda de la página de inicio del repositorio para elegir la rama en la que estaba trabajando el colaborador original.
Una vez seleccionada esta rama, puedes empezar a editar los archivos en GitHub teniendo cuidado de confirmar los cambios en esta misma rama.
Como alternativa, puedes [abrir el IDE de github.dev en tu navegador] (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor), seleccionar la rama y continuar editando y confirmando allí.

### Edita la lección localmente

Siga estos pasos después de crear la bifurcación.

1. Clónelo en su sistema local.
2. En el shell, navega hasta tu clon local del proyecto, por ejemplo, `cd ~/Documents/DataCarpEntry/r-ecology-lesson`.
3. Busca la rama en la que estaba trabajando el colaborador original (`git fetch origin <their-branch-name>`, p. ej., `git fetch origin 123-better-captions`).
4. Cambia a él (`git switch <their-branch-name>`, por ejemplo, `git switch 123-better-captions`).

Una vez que esté trabajando en esta rama, puede editar la lección y confirmar los cambios como de costumbre.
Cuando estés listo, agrega tu propia bifurcación del repositorio de lecciones en forma remota (`git remote add <remote-name> <address-of-forked-repository-you-just-copied>`, por ejemplo, `git remote add myfork git@github.com:myusername/image-processing.git`), inserta las confirmaciones que has realizado y abre una solicitud de cambios en el repositorio oficial.

## 2. Agregue su bifurcación como repositorio remoto

Si ya tienes un clon local del repositorio de la lección, puedes agregar la bifurcación de la lección del colaborador original como otro repositorio remoto para el proyecto y obtener desde allí la rama en la que estaba trabajando.

1. Siga los pasos descritos anteriormente en [_Find the original's fork_] (#1-fork-their-repository-and-branch).
2. Haga clic en el botón _Código_ y copie la dirección de este repositorio en su portapapeles.
3. En el shell, navega hasta tu clon local del proyecto, por ejemplo, `cd ~/Documents/DataCarpEntry/r-ecology-lesson`.
4. Añade la bifurcación del colaborador original como un nuevo repositorio remoto para este clon: `git remote add <remote-name> <address-of-forked-repository-you-just-copied>`,
   , por ejemplo, `git remote add toby git@github.com:tobyhodges/image-processing.git`.
5. Busca la rama en la que estaban trabajando desde su bifurcación, por ejemplo, `git fetch toby 123-better-captions`.
6. Cambia a esta rama, por ejemplo, `git switch 123-better-captions`.

Una vez que estés trabajando en esta rama, puedes editar la lección y confirmar los cambios como de costumbre, luego subirlos a tu bifurcación y abrir una solicitud de cambios cuando estés listo.

## Abrir una pull request con tus actualizaciones

Cuando estés listo para abrir una nueva solicitud de cambios que incluya tus cambios, asegúrate de hacerlo en el repositorio correcto (normalmente un repositorio de una de las organizaciones oficiales de The Carpentries, por ejemplo, `datacarpentry`): GitHub puede intentar ayudarte primero a abrir una solicitud de extracción en la bifurcación del colaborador original en lugar de en el repositorio central de Carpentries.

Cuando abras tu pull request, diles a los mantenedores que has creado sobre la base del trabajo anterior del otro colaborador. Etiqueta a ese colaborador original y haz referencia a su pull request por su número, por ejemplo, `Este pull request se basa en #37 y lo reemplaza por @USERNAME para cerrar el número #34 con [alguna descripción de los cambios realizados en tu pull request...] `.
Esto ayudará a los responsables del mantenimiento de la lección a entender que pueden cerrar la otra solicitud de extracción y la relación entre los dos conjuntos de cambios.
