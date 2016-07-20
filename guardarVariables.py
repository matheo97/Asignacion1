import os
import commands
import sys
import random

def main():

        #variables globales
        valor = 0
        comando = ""


        #De acuerdo al parametro inicial, si esta en la instancia 1, o si esta en la instacia 2, se asigna a valor

        if(sys.argv[1] == "1"):
                valor = 1
        elif(sys.argv[1] == "2"):
                valor = random.randint(2,5)
                

        #De acuerdo a la asignacion de valor, se opta por guardar alguna variable, la 1 esta reservada para ser guardada desde
        #la instancia 1


        #El swap ocupado
        if(valor == 1):
                result = commands.getoutput('cat /proc/meminfo|grep "SwapTotal:"|tr -s "'" "'"|cut -d "'" "'" -f 2')
                nombre = "swap_ocupado"
                comando = """curl -i -XPOST 'http://localhost:8086/write?db=mydb' --data-binary 'variable,name=%s value=%s' """%(nombre, str(result))
                print "Se agrego " + nombre

        #El swap libre
        if(valor == 2):
                result = commands.getoutput('cat /proc/meminfo|grep "SwapFree:"|tr -s "'" "'"|cut -d "'" "'" -f 2')
                nombre = "swap_libre"
                comando = """curl -i -XPOST 'http://54.187.208.236:8086/write?db=mydb' --data-binary 'variable,name=%s value=%s' """%(nombre, str(result))
                print "Se agrego " + nombre

        #El numero de interfaces con errores
        if(valor == 3):
                result = commands.getoutput('/sbin/ifconfig -a|grep errors|tr -s "'" "'"|cut -d "'" "'" -f 4|grep -v errors:0|wc -l')
                nombre = "interfaces_errores"
                comando = """curl -i -XPOST 'http://54.187.208.236:8086/write?db=mydb' --data-binary 'variable,name=%s value=%s' """%(nombre, str(result))
                print "Se agrego " + nombre

        #La memoria usada
        if(valor == 4):
                result = commands.getoutput('free|grep Mem:|tr -s "'" "'" |cut -d "'" "'" -f 2')
                nombre = "memoria_usada"
                comando = """curl -i -XPOST 'http://54.187.208.236:8086/write?db=mydb' --data-binary 'variable,name=%s value=%s' """%(nombre, str(result))
                print "Se agrego " + nombre

        #El numero de interfaces con colisiones
        if(valor == 5):
                result = commands.getoutput('/sbin/ifconfig -a|grep collisions|tr -s "'" "'"|cut -d "'" "'" -f 2|grep -v collisions:0|wc -l')
                nombre = "interfaces_colisiones"
                comando = """curl -i -XPOST 'http://54.187.208.236:8086/write?db=mydb' --data-binary 'variable,name=%s value=%s' """%(nombre, str(result))                              
                print "Se agrego " + nombre


        #Se ejecuta el comando
        os.system(comando)



if __name__ == '__main__':
        main()

