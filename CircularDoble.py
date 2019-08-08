class NodeCir:
    def __init__(self,  user = None, iduser = None):    
        self.user = user
        self.siguiente = None       
        self.anterior =  None   
        self.iduser = iduser

import os
class ListaCir:
    def __init__(self):        
        self.primero_head = None 
        self.size = 0
        self.ultimo = None

    def esVacio(self):
        return self.primero_head is None

    #para insertar nod (fin)
    def Insert_nod(self, user):
        new_nod = NodeCir(user, self.size)
        if self.esVacio():
            self.primero_head = new_nod
            self.ultimo = new_nod

            self.primero_head.anterior = self.ultimo
            self.ultimo.siguiente = self.primero_head
        else:
            self.ultimo.siguiente = new_nod
            new_nod.anterior = self.ultimo
            self.ultimo = new_nod

            self.primero_head.anterior = self.ultimo
            self.ultimo.siguiente = self.primero_head
            
        self.size = self.size + 1


    #Imprimir lista adelante
    def Lista_imprimir_ade(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head
            #while temp_prin.siguiente != self.primero_head:  
            while temp_prin != self.ultimo:         
                print(temp_prin.user + " - " + str(temp_prin.iduser))            
                temp_prin = temp_prin.siguiente
            print(temp_prin.user + " - " + str(temp_prin.iduser)) 

    #Imprimir lista atras
    def Lista_imprimir_atra(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.ultimo
            while temp_prin != self.primero_head:         
                print(temp_prin.user)            
                temp_prin = temp_prin.anterior
            print(temp_prin.user)

    #para graficar en grapiz
    def graf_users(self):

        f = open("user_list.txt", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")

        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head
            while temp_prin != self.ultimo:         
                #print(temp_prin.user) 
                nodo_name =  str(temp_prin.iduser)
                nodo_name_sig = str(temp_prin.siguiente.iduser)
                f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ temp_prin.user +"|<f2> }\"];\n")            
                
                f.write("node"+ nodo_name +" -> ")
                f.write("node"+ nodo_name_sig +";\n") 

                f.write("node"+ nodo_name_sig +" -> ")
                f.write("node"+ nodo_name +";\n") 

                temp_prin = temp_prin.siguiente
            #print(temp_prin.user)
            nodo_name =  str(temp_prin.iduser)
            nodo_name_sig = str(temp_prin.siguiente.iduser)

            f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ temp_prin.user +"|<f2> }\"];\n")

            f.write("node"+ nodo_name +" -> ")
            f.write("node"+ nodo_name_sig +";\n") 

            f.write("node"+ nodo_name_sig +" -> ")
            f.write("node"+ nodo_name +";\n") 

        f.write("}")
        f.close()

        os.system("dot -Tpng user_list.txt -o user_list.jpg")
        os.system("user_list.jpg")

    def add_ejemplo(self):
        self.Insert_nod("user1")
        self.Insert_nod("rafael")
        self.Insert_nod("angel")
        self.Insert_nod("nny")

        self.Lista_imprimir_ade()



#lis_cir = ListaCir()
#lis_cir.Insert_nod("user1")
#lis_cir.Insert_nod("rafael")
#lis_cir.Insert_nod("angel")
#lis_cir.Insert_nod("nny")

#lis_cir.Lista_imprimir_ade()
#print("*******")
##lis_cir.Lista_imprimir_atra()

#lis_cir.graf_users()