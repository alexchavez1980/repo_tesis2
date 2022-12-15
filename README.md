
# TRABAJO FINAL INTEGRADOR
### Especialización en ciencia de datos ITBA  
  
##### *(15/Dic/2022/10h)*  



  
## Los datasets.  
Son tres grupos de datasets: el *ERPTemplate.mat.*, el grupo de los 8 archivos que conforman el *P300-Dataset* y el grupo de los *p300-subject-XX.mat*.  
  
Cada uno de ellos contiene uno o varios archivos .mat. Por practicidad [se encuentran en la carpeta *dataset*](dataset/)  
  
### 1.El *ERPTemplate.mat*.
BLA BLA BLA    
  
  
  
### 2. El grupo de los 8 archivos que conforman el *P300-Dataset*.  
Dataset obtenido de las P300 de ocho sujetos sanos.  
La estructura se compone de la siguiente manera:  
  
• [Una descripción mas en detalle del dataset](a_analisis_P300S4.ipynb) junto con *data.X* que es la matriz EEG (8 canales).  
De todo el archivo lo que se extrae es la estructura *['data'][0][0][0]*.  
Acá podés leerlos todos al tiempo o elegir cuál canal analizar y:  
• data.y : Etiquetas (1/2).  
  
• **stim** y **type** tienen algunas características similares, [La analicé en un mismo archivo](a_analisis_stim&type.ipynb)
- stim número de estimulación: 1-6 filas, 7-12 columnas.  
- type: BLA BLA BLA.  
  
• **trial**: Punto muestral donde se inicia cada uno de los 35 ensayos. [Acá podés ver un análisis mas detallado](a_analisis_trial.ipynb)  
• **flash**: Punto de muestra donde comienza cada parpadeo (id del punto de muestra, duración, estimulación, hit/nohit). [También podés ver mas en detalle ésta onda](a_analisis_flash.ipynb)  

Dispositivo: g.Tec g.Nautilus g.LadyBird, 250 Hz, filtro de muesca a 50 Hz, paso de banda 0,1-30 Hz
  
Este conjunto de datos se produjo utilizando el estándar 6x6 Donchin y Farewell P300 Speller Matrix, con un ISI de 0,125 ms.  
Hay 7 palabras con 5 letras cada una. Hay 10 secuencias de intensificación por letra.  
El procedimiento original usaba 3 palabras para el entrenamiento y trataba de decodificar las 4 palabras restantes para la prueba.    
  





Inspiración
Intente decodificar la palabra deletreada directamente desde la matriz EEG. Hay 7 palabras de 5 letras cada una. Cada letra está compuesta por 120 estímulos de la matriz P300, 6 filas y 6 columnas, diez veces cada una. El objetivo es decodificar las palabras deletreadas de las últimas 20 letras (4 palabras). Dado que el ISI es muy bajo, es difícil adquirir buenos rendimientos.
Producido por el CiC, Universidad ITBA, Buenos Aires, Argentina

  
  
### 3. El grupo de los *p300-subject-XX.mat*.  






  




  **===========================================**  
  *De acá en adelante es guia*  
  **===========================================**  
    
Docentes:   
Pedro Ferrari | pedro@muttdata.ai  
Juan Martín Pampliega | jpamplie@itba.edu.ar  

Estudiantes:      
Guillermo Lencina | glencina@itba.edu.ar    
Nicolas Arosteguy | narosteguy@itba.edu.ar    
Alexander Chavez | achavezmontano@itba.edu.ar   
  
  
## Resumen

Se consultarán dos API's publicas de spotify, una con información de usuarios y sus playlist y otra con la información de las playlist perse.  
  
En una primera instancia mediante un script de python (y con usuarios pre-seleccionados manualmente) se obtienen datos de los mismos que contienen las playlist que tengan creadas.  
  
La salida del  response es almacenada en un csv (users_file.csv) sin tranformar, y subido a la base de datos SEMINARIO en el schema staging ( donde almacenaremos los csv en tablas sin transformar ).  
  
Luego mediante Queries de SQL se ejecutan diferentes transformaciones para lograr extraer y estructurar de la tabla de staging de usuarios tanto los datos de los mismos como sus playlist.  
  
Una vez construidas las tablas de usuarios y playlist en el eschema public , con un segundo script de python obtenemos estos id de playlist ya procesados y consultamos la API de playlist, de donde obtenemos un 2do csv (playlist_file.csv) que será almacenado también en el schema de staging, sin procesar.  
  
Nuevamente con Queries SQL extraemos y estructuramos la tabla de playlist_artist, en donde vamos a poder obtener que artistas contiene cada playlist.  
  
Por último, con SQL, se genera una tabla con información (user_id, artista), vinculando todos los artistas que se hayan encontrado en las playlist con sus respectivos usuarios.  
  
Esta ultima información es exportada en un csv (export_colab.csv) para ser el input del colab y empezar con los algoritmos de clusterización.  
  
Todas estas tareas estarán osquestadas mediante operadores de airflow ( Postgres Operators y Python Operators)  
  
  
## Objetivo    
  
Obtener datos sobre que artistas que escuchan los usuarios en sus playlists publicas con el fin de prototipar la extraccióon, el procesamiento, y los análisis de la información para un futuro sistema de recomendacion basado en las coincidencias de artistas entre los usuarios.


## Contenido

* [Infraestructura](#Infraestructura)
* [Instalación y puesta en marcha del ambiente](#Pasos-para-instalar)
* [Jupyter Notebook](jupyter/notebook/README.md)
* [Airflow (DAGs configurados en _users_spotify.py_)](dags/README.md)
  
    
## Infraestructura  
  
Nuestro trabajo simula una instalación de producción con múltiples containers en Docker.
_docker-compose.yaml_ contiene las definiciones y configuraciones para los siguientes servicios:

* Interfaz gráfica de Jupyter obtenida de la imagen arjones/pyspark:2.4.5. 

    Una vez los containers estén en Running, podés ingresar desde acá -> [Jupyter](http://localhost:8888)

* Interfaz gráfica de Airflow obtenida de la imagen -apache/airflow:2.4.1. 

    Una vez los containers estén en Running, podés ingresar desde acá -> [Airflow](http://localhost:8080)

* Motor de base de datos postgres obtenida de la imagen postgres:13. 


## Pasos para instalar

1. Clonar repo: git clone https://github.com/guillelencina/seminario_final.git

![](./images/git_clone.jpg)


2. Abrir _Docker Desktop_ para visualizar desde la interfaz.

![](./images/docker_desktop_ini.jpg)


3. Desde VSCode, abrir la carpeta _seminario_final-master_.

![](./images/folder_seminario_final.jpg)


4. Ejecutar una consola de Ubuntu.

![](./images/ubuntu_console.jpg)


5. Ingresar a la carpeta: cd seminario_final-master

6. Ejecutar el comando: docker-compose -f docker-compose.yaml up -d

* El docker-compose es un archivo yaml/yml para crear todos los containers necesarios y a la vez.
* Una vez ejecutado, deben aparecer todos los containers OK como indica la imagen.

![](./images/containers_done.jpg)

* También los podés chequear en la interfaz gráfica de Docker.

![](./images/containers_running.jpg)


Sitios de interés: 

    * https://www.youtube.com/c/PeladoNerd  
    * https://www.youtube.com/c/HolaMundoDev  
    * https://www.youtube.com/c/NetworkChuck
    * Postgres + PGAdmin : https://www.youtube.com/watch?v=uKlRp6CqpDg  


## Acerca de

Nicolás Arostegui | [LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-arosteguy-a564a97a/) 

Guillermo Lencina | [LinkedIn](https://www.linkedin.com/in/guillermolencina/) 

Alexander Chavez | [LinkedIn](https://www.linkedin.com/in/alexchavez1980/) 

ITBA &copy; 2021/2022 
