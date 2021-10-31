"""
2.	(10)Elimine los elementos duplicados de un vector ordenado.
¿Cuál es la eficiencia del método?
Compárela con la eficiencia del punto 1 --> en los archivos nombrados "2-1 comparacion"

"""

def eliminarDuplicados(lista):

    i=0
    datoAnt=None
    while(i<len(lista)):
        
        if(lista[i]==datoAnt):
            lista.remove(datoAnt)
            i-=1

        datoAnt=lista[i]
        i+=1

lista=[1,1,1,1,2,2,2,2,3,3,6,6,6,7,7,7]
print(lista)
eliminarDuplicados(lista)
print(lista)
