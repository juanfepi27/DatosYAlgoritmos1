"""
10.	(10) Construya un algoritmo para encontrar un valor específico en una matriz de valores ordenada por filas y columna. 
 El algoritmo toma como entrada una matriz de valores donde cada fila y cada columna están en orden, junto con un valor para ubicar en esa matriz.  Devuelve si ese elemento existe en la matriz.
 Por ejemplo, dado la siguiente matriz y buscar el 7, el algoritmo daría como resultado sí     
 Pero si se pide encontrar el número 0, el algoritmo daría como resultado no
"""

def busquedaMatrizOrdenada(matriz,valor):
    if matriz[len(matriz)-1][len(matriz[len(matriz)-1])-1] < valor:
        return "No"
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if(matriz[i][j]==valor):
                    return "Sí"
                elif(matriz[i][j]>valor):
                    break

    return "No"

    

matr=[[1,2,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]

print("busca el 7:",busquedaMatrizOrdenada(matr,7))
print("busca el 0:",busquedaMatrizOrdenada(matr,0))