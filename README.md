<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenido</summary>
  <ol>
    <li>
      <a href="#botc-en-español">BOTC en Español</a>
    </li>
    <li>
      <a href="#maneras-de-generar-un-script">Maneras de generar un script</a>
      <ul>
        <li><a href="#script_gen">script_gen</a></li>
        <li><a href="#script_convert">script_convert</a></li>
        <li><a href="#exportar-pdf">Exportar PDF</a></li>
      </ul>
    </li>
    <li><a href="#usage">Notas</a></li>
    <li><a href="#contact">Contacto</a></li>
  </ol>
</details>

<!-- BOTC EN ESPAÑOL -->
## BOTC en Español

Este es un proyecto personal para que mi gente latina o de habla hispana no se quede con las ganas de jugar un script de BOTC en su idioma, ya sea en la app oficial (https://botc.app) o en persona con los PDFs. Contiene todos los personajes oficiales hasta la fecha, y continúo trabajando para que se pueda parecer cada vez más a los scripts originales en inglés.<br>
En las carpetas vienen varios scripts que suelo jugar, los oficiales, y algunos míos los cuales cualquiera puede copiar y pegar en la app oficial, sin tener que hacer gran cosa.<br>
<br>
Para que se vean las imágenes, es necesario dentro de la app irse a settings, general y activar "Show Custom Images / Homebrew Icons.

<p align="right">(<a href="#readme-top">inicio</a>)</p>

<!-- CÓMO GENERAR UN SCRIPT -->
## Maneras de generar un script

Hice dos maneras para generar cualquier script deseado, depende de cómo quieran hacerlo abren el archivo correspondiente.

### script_gen

La manera más "completa" es abriendo `script-gen.py` y llenando los datos, sólo `name`, `pdf` y `roles` son obligatorios;
* name
    ```
    "El Mejor Script 2: Electric Boogaloo"
    ```
* author
    ```
    "Yo, quién más"
    ```
* logo
    ```
    "https://link-del-logo"
    ```
* background (si no se pone nada, se pone el fondo morado predeterminado del juego)
    ```
    "https://link-del-fondo"
    ```
* pdf (tiene que ser 'Y' o 'N') -- léase el apartado PDF --
    ```
    'Y'
    ```
* roles (formato lista, con el 'id' de los roles en inglés)
    ```
    "washerwoman","chef","lunatic","spy","legion"
    ```
Al correr el archivo, se creará un `.json` (y un `.pdf` si fue solicitado) en el folder correspondiente dependiendo de los roles.
<p align="right">(<a href="#readme-top">inicio</a>)</p>

### script_convert

Si rápidamente se requiere convertir un script ya creado sin tener que escribir todos los roles, simplemente copia y pega el contenido `.json` del script en `source.json`. Guarda y corre el archivo.<br>
Al dejar vacíos `name` y `author` se usarán los que están guardados en `id: "meta"`.

<p align="right">(<a href="#readme-top">inicio</a>)</p>

### Exportar PDF

Para poder exportar archivos `.pdf` es necesario instalar lo siguiente:
```
pip install fpdf2
```

<p align="right">(<a href="#readme-top">inicio</a>)</p>

## Notas
-Aún no se puede apreciar visualmente cuando alguien cambia de equipo ya que no encuentro las imagenes de cada personaje con su equipo cambiado. <br>
-Vodú no funciona. <br>
-Banshee necesita revivirse para recuperar sus votos.<br>
-En los PDFs aún no se visualizan los jinxes ni los viajeros. Ni el orden de las noches.<br>
-Necesito modificar tres puntitos de dos roles en database.csv

## Contacto

@nolonunez