#coding: utf8
#Alejandro Gambín
salir= "N"
cifra= 1
maximo= 5
suma= 0
while ( salir=="N"):
	if(cifra%2==0):
    	print (cifra ,)
    	if(cifra<=maximo-2):
        	print ("+" ,)
       	 
    	suma=suma+cifra
   	 
	cifra=cifra+1
  if( cifra > maximo):
        	salir= "S"
print ("=" , suma)
