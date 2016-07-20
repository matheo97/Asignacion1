Example Program(R) Version 1.0 19/07/2016

================================================================================
About ======================================================================
================================================================================

-guardarVariables.py se encarga de guardar las variables en la influxbd de la
instancia uno, si se ejecuta con parametro igual a 1, hace una insercion local
de lo contrario lo estaria haciendo desde un lugar remoto, con el parametro igual
a 2.

-consultarBaseDatos.py consulta la ingfluxbd para obtener la informacion de las
variables guardadas con el archivo guardarVariables.py, toda esta informacion
es almacenada en 'datos.txt'


================================================================================
Ejecucion ======================================================================
================================================================================

-guardarVariables.py

Para el archivo guardarVariables.py, se necesita especificar desde que instancia
se esta ejecutando el programa, pasando como parametro el 1 si se encuentra en 
la instancia 1, o el 2 si se encuentra en la instacia 2.

Ejemplo para linux:

python guardarVariables.py 1
python guardarVariables.py 2


-consultarBaseDatos.py

Para el archivo consultarBaseDatos.py, solo se necesita ejecutar el programa
normalmente y este generara un archivo llamado 'datos.txt' con la informacion
extraida de la base de datos de la instacia 1.

Ejemplo para linux:

python consultarBaseDatos.py



