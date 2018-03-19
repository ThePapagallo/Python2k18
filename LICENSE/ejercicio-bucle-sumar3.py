#coding: utf8
#Alejandro Gambín
salir = "N"
cifra=1
maximo=5
suma=0
while ( salir=="N" ):
	print (cifra ,)
	if(cifra<=maximo-1):
    	print ("+" ,)
    
	suma=suma+cifra
	cifra=cifra+1
	if ( cifra > maximo ):
        	salir = "S"
print ("=" , suma)
