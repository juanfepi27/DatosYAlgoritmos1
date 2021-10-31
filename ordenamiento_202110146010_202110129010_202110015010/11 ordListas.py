"""
11.	(10)  se tiene una lista A con 100 elementos A[ a1……a100  ] 
                                        B de 60 elementos    B[ b1……b60  ]  
Se desean resolver las siguientes tareas
a.)	Ordenar cada lista aplicando el método Quicksort
b.)	Crear una lista C que sea la unión de la lista A y B
c.)	Ordenar la lista C y visualizarla
"""

from random import randrange

A=[]
for i in range(100):
    num=randrange(-100,100)
    A.append(num)

B=[]
for i in range(60):
    num=randrange(-100,100)
    B.append(num)

print("\npreviamente A estaba así:\n"+str(A))
print("\npreviamente B estaba así:\n"+str(B))

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

quickSort(A,0,len(A)-1)
quickSort(B,0,len(B)-1)
print("\na)")
print("\nLuego del quicksort A esta así:\n"+str(A))
print("\nLuego del quicksort B esta así:\n"+str(B))

print("\nb) se crea lista c")

C=A+B

quickSort(C,0,len(C)-1)
print("\nc)")
print("\nLuego del quicksort C esta así:\n"+str(C))