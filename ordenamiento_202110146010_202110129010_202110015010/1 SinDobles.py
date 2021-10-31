"""
1.	(10)Se desea eliminar todos los números duplicados de una lista  
Por ejemplo 
Si se le ingresan los valores [4,7,11,4,9,5,11,7,3,5]
Se debe cambia a [4,7,11,9,5,3]

analisis:
-leer
-revisar que no este  mas ese dato-->count
"""

def eliminarDuplicados(lista):

    i=0
    while(i<len(lista)):
        dato=lista[i]
        numVeces=lista.count(dato)

        while(numVeces>1):
            lista.pop(lista.index(dato,i+1))
            numVeces-=1

        i+=1

lista=[4,7,11,4,9,5,11,7,3,5]
print(lista)
eliminarDuplicados(lista)
print(lista)
