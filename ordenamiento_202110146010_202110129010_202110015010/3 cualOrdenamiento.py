"""
3.	(5)Dada la siguiente lista 
[47,3,21,32.56,92]

Después de 2 “pasadas” de un algoritmo de ordenación, la lista ha quedado dispuesto asi
[3,21,47,32,56,92]

¿Qué algoritmo de ordenación se esta utilizando (selección, burbuja o inserción)?-->respuesta por terminal

"""

def ordenBurbuja(Lista):
    #se revisa la lista completa
    for i in range(len(Lista)):
        #se revisa los datos por parejas desde
        #el inicio hasta lo que ya se ha revisado
        #es decir (len(Lista)-1)-i veces
        for j in range(len(Lista)-(i+1)):
            #y se hace el cambio si el siguiente
            #es menor que el actual
            if(Lista[j]>Lista[j+1]):
                aux=Lista[j]
                Lista[j]=Lista[j+1]
                Lista[j+1]=aux
        print(Lista)
    return(Lista)

def ordenInsersion(Lista):
    #se va a revisar los datos desde el segundo elemento
    for i in range(1,len(Lista)):
        #se almacena el actual 
        actual = Lista[i]
        #se almacena el índice donde está el actual
        j = i
        #se hace un ciclo hasta antes que j sea 0
        #o hasta ver que el anterior a j sea menor que el actual
        while j>0 and Lista[j-1]>actual:
            #si cumple lo anterior vamos moviendo los datos
            #subiendolos uno a uno
            Lista[j]=Lista[j-1]
            #este decremento ayuda a seguirse moviendo 
            j = j-1
        #al final j tendrá el valor donde debe ir el actual
        Lista[j]=actual
        print(Lista)

    return(Lista)

def ordenSeleccion(Lista):
    
    #Se recorre el arreglo buscando un dato mínimo
    for i in range(len(Lista)):
        minimo=i
        for j in range (i+1,len(Lista)):
            #si se encuentra uno menor al primero se va
            #eligiendo como el nuevo menor
            if(Lista[j]<Lista[minimo]):
                minimo=j
        
        Lista[i],Lista[minimo]=Lista[minimo],Lista[i]
        print(Lista)
    
    return(Lista)


prueba1=[47,3,21,32,56,92]
print("ordenamiento por Burbuja")
print(ordenBurbuja(prueba1))

prueba2=[47,3,21,32,56,92]
print("ordenamiento por Insersion")
print(ordenInsersion(prueba2))

prueba3=[47,3,21,32,56,92]
print("ordenamiento por Seleccion")
print(ordenSeleccion(prueba3))

print("puede verse que tanto el ordenamiento por seleccion\ny el de insersion en su segunda pasada muestran\nla respuesta esperada, pudiendo ser cualquiera de los dos")