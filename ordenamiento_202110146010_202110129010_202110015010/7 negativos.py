"""
7.	(10) Diseñe e implemente una función para encontrar todos los valores negativos dentro de una lista dada. Tu función debería devolver una nueva lista que contiene los valores negativos. 

¿Cuándo ocurre el peor de los casos y cuál es el tiempo de ejecución para ese caso?
"""

from random import randrange
import time 

#se realiza la siguiente importacion para mejor complejidad
def particion(arr, inicio, fin):
    #se toma cualquier numero como el pivote
    indice_pivote = randrange(inicio, fin + 1)
    pivote = arr[indice_pivote]
    #se crea una variable para tener control de los menores que el pivote
    ultimo_menor = inicio - 1    
    for actual in range(inicio, fin+1): 
        # se organizan los datos respecto al pivote        
        if actual == indice_pivote: 
            #se ignora el pivote            
            continue        
        if arr[actual] < pivote: 
            #en caso de encontrar uno menor se aumenta la variable de control
            #y se ubica al dato actual en el valor de la variable
            #y el que estaba en la variable se va a la actual            
            ultimo_menor += 1 
            if(ultimo_menor==indice_pivote) :
                arr[actual], arr[ultimo_menor] = arr[ultimo_menor], arr[actual]
                indice_pivote=actual
            else:  
                arr[actual], arr[ultimo_menor] = arr[ultimo_menor], arr[actual]
    #al finalizar se ubica el pivote en el siguiente justo del último menor
    arr[ultimo_menor + 1], arr[indice_pivote] = arr[indice_pivote], arr[ultimo_menor + 1]
    return ultimo_menor + 1

def quickSort(arr, inicio, fin):
    #siempre que el indice de inicio sea menor (no igual) 
    # podrá hacer el ordenamiento
    if(inicio < fin):
        #se hace la particion/ordenamiento del arreglo en mitades 
        #y se asigna el indice del pivote
        indice_pivote = particion(arr, inicio, fin)
        #se realiza el proceso anterior para 
        # los datos mayores y menores del pivote
        quickSort(arr, inicio, indice_pivote - 1)       
        quickSort(arr, indice_pivote + 1, fin)

#----------------------METODO SOLICITADO------------------------#
def numNegativos(lista):

    quickSort(lista,0,len(lista)-1)

    listaNeg=[]
    for i in lista:
        if i<0:
            listaNeg.append(i)
        else:
            break

    return listaNeg

pos=[]
for i in range(1,1001):
    pos.append(i)
prom=[]
for i in range(1000):
    ranNum = randrange(-1000, 1001)
    prom.append(ranNum)
neg=[]
for i in range(1,1001):
    neg.append(i*-1)

t1=time.time()
print(numNegativos(pos))
t2=time.time()
t3=time.time()
print(numNegativos(prom))
t4=time.time()
t5=time.time()
print(numNegativos(neg))
t6=time.time()

print("""
-ahora hablando de tiempos podemos ver como:
(TODOS POSITIVOS)tarda: """+str(t2-t1)+"""
(PROMEDIO)tarda: """+str(t4-t3)+"""
(TODOS NEGATIVOS)tarda: """+str(t6-t5)+"""
donde claramente el peor de los casos es el que tiene todos los negativos, con un tiempo de ejecución
de """+str(t6-t5)+""" para una lista con 1000 negativos""")
