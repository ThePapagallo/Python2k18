#coding: utf8
#Alejandro Gambín Gómez

import os
os.system("clear")

valor=input("Escriba un año y le diré si es bisiesto: ")

if(valor==0):
    print "No hubo año 0"
elif(valor<0):
    if(valor%4==0 and valor%100!=0) or valor%400==0:
        print -valor,"a.C es año bisiesto"
    else:
        print -valor,"a.C no es año bisiesto"
else:
    if(valor%4==0 and valor%100!=0) or valor%400==0:
        print valor,"es año bisiesto"
    else:
        print valor,"no es año bisiesto"
