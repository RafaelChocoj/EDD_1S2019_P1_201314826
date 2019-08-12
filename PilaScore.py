class NodeScore:
    def __init__(self, x_pos = None, y_pos = None, valor = None ):    
        self.valor = valor
        self.x_pos = x_pos    
        self.y_pos = y_pos    

        self.siguiente = None       

import os
class PilaScore:
    def __init__(self):        
        self.primero_head = None 
        self.size = 0
        self.ultimo = None

    def esVacio(self):
        return self.primero_head is None
        

    #para insertar nodo, lAST IN, ultimo a ingresar
    def insertNodo_Final(self, x_pos, y_pos, valor):
        
        nuevo = NodeScore(x_pos, y_pos, valor)
        
        if self.esVacio() == True:    
            self.primero_head = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size = self.size + 1


    #FIRT OUT, primero en salir es el ultimo
    #pop
    def eliminar_ultimo(self):  
        if self.esVacio()== True:
            print ("No puede eliminar ultimo La lista esta vacia") 
        elif self.primero_head == self.ultimo:
            self.primero_head = None
            self.ultimo = None 
            #print ("elemento ultimo eliminado, vacia")
        else:
            actual_del = self.primero_head
            aux22 = None
            while actual_del != None:
                if actual_del.siguiente == self.ultimo:
                    
                    aux22 = self.ultimo
                    self.ultimo = actual_del
                    actual_del.siguiente = None
                    
                    #print ("elemento ultimo eliminado")
                else:
                    #aux22 = actual_del
                    actual_del = actual_del.siguiente
        self.size = self.size - 1


    #Imprimir lista adelante
    def Lista_imprimir_ade(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head

            while temp_prin != None:         
                #print(str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) + " pila")     
                print( temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )          
                temp_prin = temp_prin.siguiente

    #Imprimir lista adelante
    def Clear_score(self):
        temp_prin = self.primero_head
        while temp_prin != None:         
            self.eliminar_ultimo()       
            temp_prin = temp_prin.siguiente
        self.eliminar_ultimo() 

    #para graficar en grapiz la pila score
    def graf_score(self):

        f = open("pila_score.txt", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")
        f.write("node0[label = \"")

        temp_prin = self.primero_head
        pila_cor = ""
        while temp_prin != None:    
            nodo_corde = "(" + str(temp_prin.x_pos) + "," + str(temp_prin.y_pos) + ")"
            pila_cor = "|" + nodo_corde  + pila_cor  
            #pila_cor = "|" + temp_prin.valor  + pila_cor  
            temp_prin = temp_prin.siguiente

        #print("impire " + pila_cor)
        f.write(str(pila_cor) + "\"")
        f.write("]; \n}")
        f.close()

        os.system("dot -Tpng pila_score.txt -o pila_score.jpg")
        os.system("pila_score.jpg")

        

#lis_score = PilaScore()
#lis_score.insertNodo_Final(0, 0, "1")
#lis_score.insertNodo_Final(0,1,"2")
#lis_score.insertNodo_Final(0,2,"3")
#lis_score.Lista_imprimir_ade()
##lis_score.graf_score()
##lis_score.eliminar_ultimo()
#print("elimando")
#lis_score.Clear_score()
#lis_score.Lista_imprimir_ade()
#lis_score.graf_score()

