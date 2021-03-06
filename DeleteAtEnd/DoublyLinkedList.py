# Implementando la lista doblemente vinculada con Python

# 1. creamos el nodo
class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
# item variable almacenará los datos reales del node.
#  El nref almacena la referencia al siguiente node
#  el pref almacena la referencia al node anterior en la lista doblemente enlazada. 
#  
#  2.crear la DoublyLinkedListclase
# que contiene diferentes funciones relacionadas con listas doblemente enlazadas
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    # 2.1 Insertar elementos en una lista vacía
    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    # 2.2 Insertar elementos al principio
    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node   
    # 2.3 Insertar elementos al final
    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n
    # 2.4 Insertar un elemento despues
    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node  
    # 2.5 recorrer la lista
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref       

    #ELIMINAR AL FINAL DE LA LISTA
    def Delete_at_end(self):
        if(self.start_node):
            if(self.start_node.nref):
                nodo=self.start_node
                while(nodo.nref.nref):
                    nodo=nodo.nref

                nodo.nref.pref=None
                nodo.nref=None
            else:
                self.start_node=None
        else:
            raise Exception("no hay elementos en la lista para eliminar")         

new_linked_list = DoublyLinkedList()  
new_linked_list.insert_in_emptylist(50)   
new_linked_list.insert_at_start(10)
new_linked_list.insert_after_item(10,65)
new_linked_list.traverse_list()

print("ahora eliminaremos el 50")
new_linked_list.Delete_at_end()
new_linked_list.traverse_list()
print("ahora eliminaremos el 65")
new_linked_list.Delete_at_end()
new_linked_list.traverse_list()
print("ahora eliminaremos el 10")
new_linked_list.Delete_at_end()
new_linked_list.traverse_list()