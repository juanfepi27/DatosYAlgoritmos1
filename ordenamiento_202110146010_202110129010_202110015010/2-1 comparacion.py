import time

def eliminarDuplicados1(lista):

    i=0
    while(i<len(lista)):
        dato=lista[i]
        numVeces=lista.count(dato)

        while(numVeces>1):
            lista.pop(lista.index(dato,i+1))
            numVeces-=1

        i+=1

def eliminarDuplicados2(lista):

    i=0
    datoAnt=None
    while(i<len(lista)):
        
        if(lista[i]==datoAnt):
            lista.remove(datoAnt)
            i-=1

        datoAnt=lista[i]
        i+=1

a=[]

for i in range (25000):
    a.append(2)

for i in range (20000):
    a.append(5)

for i in range (15000):
    a.append(7)

for i in range (40000):
    a.append(15)

b=[]

for i in range (25000):
    b.append(2)

for i in range (20000):
    b.append(5)

for i in range (15000):
    b.append(7)

for i in range (40000):
    b.append(15)

t1=time.time()
#print(a)
eliminarDuplicados1(a)
print(a)
t2=time.time()
print("el tiempo de el metodo 1 es:",(t2-t1))

t3=time.time()
#print(b)
eliminarDuplicados2(b)
print(b)
t4=time.time()
print("el tiempo de el metodo 2 es:",(t4-t3))