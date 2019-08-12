class NodeFila:
    def __init__(self, name = None, puntos = None):    
        self.name = name
        self.puntos = puntos    

        self.siguiente = None     


import os
class FilaPuntos:
    def __init__(self):        
        self.primero_head = None 
        self.size = 0
        self.ultimo = None

    def esVacio(self):
        return self.primero_head is None

    #para insertar, ultimo a ingresar ##enqueue
    def insertNodo(self, name, puntos):
        
        nuevo = NodeFila(name, puntos)
        
        if self.esVacio() == True:    
            self.primero_head = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size = self.size + 1

        ##verificando si ya se llego al limite#
        fil_tam = self.size
        #print("fil_tam: "+ str(fil_tam) + " - " + name)
        if (fil_tam > 10):
            self.eliminar_nod()

    #primero en salir ##dequeue
    def eliminar_nod(self):
        if self.esVacio()== True:
            print ("No puede eliminar primero La lista esta vacia")
        elif self.primero_head == self.ultimo:
            self.primero_head = None
            self.ultimo = None
            self.size = self.size - 1
            #print ("eliminado, vacio")
        else:
            aux = self.primero_head
            self.primero_head = self.primero_head.siguiente
            aux.siguiente = None
            self.size = self.size - 1


    #Imprimir fila adelante
    def fila_imprimir_ade(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head
            while temp_prin != None:                    
                temp_prin = temp_prin.siguiente

    #graf puntuaciones                
    def graf_puntuaciones(self):

        f = open("puntos.txt", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")
        conta = 0
        temp_prin = self.primero_head   
        while temp_prin != None:    
            nodo_name = "nod" + str(conta)
            nodo_corde = "(" + str(temp_prin.name ) + "," + str(temp_prin.puntos ) + ")"
            f.write( nodo_name +"[label = \"{<f1> "+ nodo_corde +"|<f2> }\"];\n")  
                  
            f.write(nodo_name +"-> ")

            temp_prin = temp_prin.siguiente
            conta = conta + 1

            if (temp_prin != None):
                nodo_name_sig = "nod" + str(conta)
                f.write(nodo_name_sig +";\n")
            else:
                f.write("null;\n")  

        f.write("}")
        f.close()

        os.system("dot -Tpng puntos.txt -o puntos.jpg")
        os.system("puntos.jpg")
            
            
#fil = FilaPuntos()
#fil.insertNodo("juanito", 1)
#fil.insertNodo("g3", 2)
#fil.insertNodo("rambio", 3)
#fil.insertNodo("saber", 4)
#fil.insertNodo("x3", 5)
#fil.insertNodo("panchito", 6)
#fil.insertNodo("panchito", 7)
#fil.insertNodo("panchito", 8)
#fil.insertNodo("panchito", 9)
#fil.insertNodo("panchito", 10)
##fil.insertNodo("panchito",11)
##fil.insertNodo("panchito", 12)
##fil.insertNodo("panchito", 13)
###fil.fila_imprimir_ade()
###fil.eliminar_nod()
##print("////")
#fil.fila_imprimir_ade()
#fil.graf_puntuaciones()
