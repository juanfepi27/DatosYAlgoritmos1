"""
6.	(10) Se cuenta con una lista de tuplas 

futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]

              si se aplica futbolistasTup.sort(key=lambda futbolista: futbolista[0])
a)	Que resultado se obtiene al aplicar el método .sort
b)	Que se esta especificando en los parámetro (key=lambda futbolista: futbolista[0])
c)	Aplique este método a las listas de los punto 1,3, 4. Que conclusión puede obtener
d)	Por favor según opinión realice una tupla con  los mejores inventos del 2019 . 
Donde usted califica el que mas le gusta o le parece importante. 
Anotación la escala con la que usted cuenta es de 1 a 100 
( no tiene que asignar ninguno de los extremos si no lo desea)  
"""
import time

futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]
print("antes del sort:\n",futbolistasTup)
futbolistasTup.sort(key=lambda futbolistas: futbolistas[0])
print("\na) luego del sort se obtiene:\n",futbolistasTup)
print("""\nb) los parametros significan lo siguiente:
key = lambda futbolistasTup 
--> el key es el criterio de ordenamiento, que en este caso se esta diciendo que responde a la funcion lambda
--> dicha funcion otorga de la lista self(futbolistasTup), cada elemento se vuelve la variable futbolistas 
y se retorna la posicion 0 de cada tupla, que corresponde al numero""")

print("\nc) los metodos para los puntos 1,3 y 4 funcionan así:")
t1=time.time()
punto1=[4,7,11,4,9,5,11,7,3,5]
print("(1) antes del sort:",punto1)
punto1.sort()
print("(1) luego del sort:",punto1)
t2=time.time()
t3=time.time()
punto3=[47,3,21,32,56,92]
print("(3) antes del sort:",punto3)
punto3.sort()
print("(3) luego del sort:",punto3)
t4=time.time()
t5=time.time()
punto4=[8,43,17,6,40,16,18,97,11,7]
print("(4) antes del sort:",punto4)
punto4.sort()
print("(4) luego del sort:",punto4)
t6=time.time()

print("""\nde esto podemos concluir :
-que arreglar listas simples no requieren de un key, pues no hay ambiguedad, a menos que se desee arreglar en orden descendente
-el metodo en si para las tuplas no requería el parametro que recibía, pues por default lo ordenaría por el primer dato, asi:""")
t7=time.time()
futbolistasTup2 = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]
print("antes del sort:\n",futbolistasTup2)
futbolistasTup2.sort()
print("\na) luego del sort se obtiene:\n",futbolistasTup2)
t8=time.time()
print("""
-ahora hablando de tiempos podemos ver como:
(1)tarda: """+str(t2-t1)+"""
(3)tarda: """+str(t4-t3)+"""
(4)tarda: """+str(t6-t5)+"""
(fut)tarda: """+str(t8-t7)+"""
donde fut generalmente es mayor por un orden de magnitud, aunque al hablar de esta masa de datos tan pequeña dichas conclusiones 
son muy superfluas y la realidad es que para estas listas los tiempos de ejecución son realmente similares""")

inventos=[("WeWALK",80),("OssoVR",100),("AirPods Pro",50),("Pantallas 8k",80),("protesis de BrainRobotics",100),("Serve",80),("nueva consola antigua de Sega",90),("PathSpot",80),("Moxi",60),("Sensor Can",60)]
print("d) mi lista de inventos es:\n",inventos)