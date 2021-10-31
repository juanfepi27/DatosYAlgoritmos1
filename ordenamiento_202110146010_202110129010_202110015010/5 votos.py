"""
5.	(10) Dada una lista voto[0.......n-1], donde cada elemento de lista representa un voto en las elecciones. 
Suponga que cada voto se da como un número entero que representa el ID del candidato elegido. 

Desarrolle un algoritmo para determinar quién gana la elección. 

Determine la complejidad del algoritmo 
    su complejidad sería O(n*m)
        siendo n la longitud del arreglo
        y m el numero de participantes desde 0 hasta numParticipantes-1 
"""

def determinarGanador(votos):                                                   # n + m*n + m--> O(n*m)

    numParticipantes=0
    for dato in votos:                                                          #n=longitud del arreglo
        if(numParticipantes<dato):
            numParticipantes=dato

    numVotos=[]                                                                 #m=numParticipantes+1
    for i in range(numParticipantes+1):
        cant = votos.count(i)                                                   #n
        numVotos.insert(i, cant)                                                #1

    ganador=0
    numVotosGanador=0
    posibleEmpate=None

    for i in range(len(numVotos)):                                              #m
        if(numVotos[i]>numVotosGanador):
            ganador=i
            numVotosGanador=numVotos[i]
        elif(numVotos[i]==numVotosGanador):
            posibleEmpate=i

    if posibleEmpate:
        if(numVotos[posibleEmpate]==numVotos[ganador]):
            return "hay un empate (por lo menos) entre "+str(ganador)+" y "+str(posibleEmpate)
        else:
            return "el ganador es "+str(ganador)
    else:
        return "el ganador es "+str(ganador)

lista=[0,1,2,4,2,6,3,2,7,1,5,7,1,4,6,2,100,1,0,0,0]
print(determinarGanador(lista))