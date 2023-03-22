#GIT: toma todos los archivos de un trabajo y los muta si hay una nueva version del codigo.
#Es un control de versiones gratuito y de codigo abierto. Registra todas los cambios realizados sobre un archivo o conjunto de archivos.

#Estados
#1er estado: "PREPARAMOS LAS CAJAS"(establecemos la carpeta de trabajo y su contenido)
#2do estado: "AGREGAMOS LAS CAJAS LISTAS"(seleccionamos los archivos en donde queremos generar una nueva version. Establecen un punto de recuperacion.)
#3er estado: "LOTE LISTO"(lugar donde se registran todos los cambios que hubo.)


#GIT HUB
#Un usuario pushea(sube al remoto) los commits que haya realizado. Una vez subido, el otro usuario realiza un pull(descarga) de los commits existentes y luego pushea los commits que realizo. De esta manera pueden trabajar de forma ordenada sobre el mismo archivo
    
#Las terminales para poder operar con GIT en Windows son: powershell, cmd y git te descarga BASH.


#Desde la pagina de Inicio de VSC, ingresamos a la terminal y podemos seleccionar trabajar con POWERSHELL O GITBASH. Es mejor en GITBASH

#1) Iniciamos en la terminal con el siguiente codigo: git init. Esto regresa un "Initialiced empty Git Repository in..."
#2) Creamos un archivo.py para comenzar
#3)Codeamos
#4)Cuando queremos que un archivo sea seguido(pero no versionado) lo debemos agregar a apartir de "git add archivo.py"






print("hola mundo")