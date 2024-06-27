para poder usar un servidor local (localhost) necesitamos usar node en esta ocacion usamos la version v20.15.0
para poder ver que vercion de node tenemos en el equipo debemos de usar una terminal cualquiera nos sirve

En esta devemos escribir el comando 'node -v' y precionar 'ENTER' luegoo nos mostrara la version de node instalada en el equipo

En caso tal que la vercion istalada no sea la v20.15.0 debemos hacer uso de nuestro navegador de confiansa y realizar la busqueda de 'node.js' y accedemos al primer resultado esto nos llevara a la pagina de node dentro de la pagina nos dirigiremos al apartado de descargas (Download)

Dentro del apartado de descargas nos dirigiremos al apartado de 'Prebuilt Installer' buscamos la version v20.15.0 y la descagamos e instalamos
la nueva vercion del nodo 

Cuando termine de ejecutarce el programa de instalacion reinaciaremos el equipo esto para que deje de usar la vercion anterior y empiece a usar la nueva version 

Ya con la version v20.15.0 debemos de instalar el servidor esto la haremos desde la terminal escribiendo el comando 'npm install json-server' luego de instalarlo crearemos una capeta llamada 'server' dentro de esta carpeta crearemos un archivo llamado 'db.json' dentro de este archivo es donde se guardara toda la informacion de nuestro servidor local 

por ultimo para obtener el url de este servidor ingresaremos el comando 'npx json-server db.json' en la consola esto encendera el servidor por lo cual ya podremos trabajar con el 