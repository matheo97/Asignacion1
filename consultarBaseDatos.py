import os
import commands
import sys
import json

def main():

	#Se hace la peticion de la informacion a la bd, y se obtiene el json en un archivo llamado archivo.txt
	comando = """curl -G 'http://54.187.208.236:8086/query?pretty=true' --data-urlencode "db=mydb" --data-urlencode "q=SELECT * FROM variable" """ + " > archivoConJson.txt"
	os.system(comando)


	#Se lee de este archivo el json y se carga
	archivo = open("archivoConJson.txt", "r") 
	datos = archivo.read()
	archivo.close()
	decoded = json.loads(datos)


	#Se escribe el archivo datos.txt con la informacion del json
	archivoDatos = open('datos.txt','w')

	for n in decoded['results'][0]['series'][0]['values']:		
		archivoDatos.write('Fecha: %s Value: %s Name: %s\n'%(n[0],n[2],n[1]))

	archivoDatos.close()


if __name__ == '__main__':
		main()
