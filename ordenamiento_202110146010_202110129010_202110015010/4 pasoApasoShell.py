"""
4.	(10) Utilizar el algoritmo de ordenación SHELL, encuentre las pasadas e intercambios 
que se realizan para  la ordenación de la siguiente lista 
[8,43,17,6,40,16,18,97,11,7]
"""

def ordenShell(listanum):
    dist=len(listanum)//2
    while(dist>0):
        #se subdivide el arreglo en mitades
        inf = 0
        sup = inf + dist
        while(sup<len(listanum)):
            #se verifica si los numeros que están a la distancia de la mitad si  
            #el superior es menor que el inferior y cambiarlos, sino pues no
            if(listanum[sup]<listanum[inf]):
                print("se intercambia "+str(listanum[sup])+" con "+str(listanum[inf]))
                listanum[sup],listanum[inf]=listanum[inf],listanum[sup]
                nuevoInf=inf-dist
                nuevoSup=sup-dist
                #en caso de que eso ocurra se verifica si hay más numeros antes (a la misma 
                #distancia) y en caso tal hacer la misma verificación hasta no poder más
                while(nuevoInf>=0):
                    if(listanum[nuevoSup]<listanum[nuevoInf]):
                        print("se intercambia "+str(listanum[nuevoSup])+" con "+str(listanum[nuevoInf]))
                        listanum[nuevoSup],listanum[nuevoInf]=listanum[nuevoInf],listanum[nuevoSup]
                        nuevoInf-=dist
                        nuevoSup-=dist
                    else:
                        break
            #incrementamos de uno en uno los numeros que se revisan
            inf+=1
            sup+=1
        #se hace el cambio de la distancia de los subarreglos
        dist//=2

        print("la lista va asi:",listanum)

    return listanum

arreglo=[8,43,17,6,40,16,18,97,11,7]

print("la lista finalmente queda así:",ordenShell(arreglo))