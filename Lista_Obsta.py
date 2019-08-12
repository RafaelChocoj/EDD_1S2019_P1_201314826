class NodeOb:
    def __init__(self, x_pos = None, y_pos = None, valor = None ):    
        self.valor = valor
        self.x_pos = x_pos    
        self.y_pos = y_pos    

        self.siguiente = None       
        self.anterior =  None   
import os
class ListaObtaculo:
    def __init__(self):        
        self.primero_head = None 
        self.size = 0


    def esVacio(self):
        return self.primero_head is None

    #para insertar nodo al principio
    def insert_inicio(self, x_pos, y_pos, valor):
    
        new_nod = NodeOb(x_pos, y_pos, valor)
        if self.esVacio():    
            self.primero_head = new_nod
            #self.ultimo = new_nod
        else:
            #new_nod.siguiente  = self.primero_head
            tempo = self.primero_head
            new_nod.siguiente  = tempo

            self.primero_head = new_nod
            tempo.anterior = new_nod

        self.size = self.size + 1

    #para insertar nodo Al final
    def Insert_fin(self, x_pos, y_pos, valor):
        new_nod = NodeOb(x_pos, y_pos, valor)

        if self.esVacio():
            self.primero_head = new_nod
            #self.ultimo = new_nod
        else:
            tempo = self.primero_head
            while (tempo.siguiente is not None):
                tempo = tempo.siguiente
            tempo.siguiente = new_nod
            new_nod.anterior = tempo
        self.size = self.size + 1

    #para eliminar nodo al principio
    def delete_inicio(self):

        if self.esVacio() == False:    
            ##esta vacia
            #print ("vacio")
        #else:
            aux = self.primero_head
            self.primero_head = self.primero_head.siguiente
            aux.siguiente = None
            self.primero_head.anterior = None
            #print ("eliminado")

        self.size = self.size - 1

    #para eliminar nodo al FINAL
    def delete_fin(self):

        if self.esVacio() == False:    
            ##esta vacia
            #print ("vacio")
        #else:
            #aux = self.primero_head
            #self.primero_head = self.primero_head.siguiente
            #aux.siguiente = None
            #self.primero_head.anterior = None

            temp_prin = self.primero_head
            while temp_prin.siguiente is not None: 
            #while temp_prin != None: 
                tempo = temp_prin 
                temp_prin = temp_prin.siguiente                     

            tempo.siguiente = None
            temp_prin.anterior = None
            
            ##print ("eliminado")


        self.size = self.size - 1

            
    #Imprimir lista adelante
    def Lista_imprimir_ade(self):
    #def Lista_imprimir_ade():
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head
            #while temp_prin.siguiente is not None:        
            #    #print( temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )   
            #    print(str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )             
            #    temp_prin = temp_prin.siguiente
            ##print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 
            #print(str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 

            while temp_prin != None:         
                print(str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )     
                #print( temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )          
                temp_prin = temp_prin.siguiente

    #Imprimir lista atras
    def Lista_imprimir_atra(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:

            temp_prin = self.primero_head
            while temp_prin.siguiente is not None:  
                temp_prin = temp_prin.siguiente      
            while temp_prin.anterior is not None: 
                #print(temp_prin.valor)
                print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 
                temp_prin = temp_prin.anterior
            #print(temp_prin.valor)
            print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 

    #para graficar en grapiz
    def graf_serpiente_solo_prueba(self):

        f = open("list_ser.txt", "w")

        #f.write("digraph G {\n")
        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")
        #f.write("node [shape = square];\n")

        #l = ["A1", "B2","C3","D4","E5", "F6"]
        #for i in range(len(l)-1):
        #    f.write("\""+ l[i]+ "\"->\"JUAN\";\n")
        temp_prin = self.primero_head
        #while temp_prin.siguiente is not None:    
        while temp_prin != None:    
            #print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )  
            nodo_name = str(temp_prin.x_pos) + str(temp_prin.y_pos)
            nodo_corde = "(" + str(temp_prin.x_pos) + "," + str(temp_prin.y_pos) + ")"
            f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ nodo_corde +"|<f2> }\"];\n")  
            
            if (temp_prin.anterior == None):
                f.write("node_n1[label = \"null\"];\n")  
                f.write("node"+ nodo_name +":f0 -> node_n1;\n" )           
            
            f.write("node"+ nodo_name +"-> ")

            #if (temp_prin == self.primero_head):
            #    f.write("node"+ nodo_name +"-> NULL1;\n")

            temp_prin = temp_prin.siguiente

            if (temp_prin != None):
                #nodo_name_sig = "-"
                #########
                nodo_name_sig = str(temp_prin.x_pos) + str(temp_prin.y_pos)
                f.write("node"+ nodo_name_sig +";\n")

                #regreoso
                f.write("node"+ nodo_name_sig +"-> node" + nodo_name+";\n")
                #node0 -> node1;
            else:
                f.write("node_n2;\n")  
                f.write("node_n2[label = \"null\"];\n")   

        #print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 

        f.write("}")
        f.close()

        os.system("dot -Tpng list_ser.txt -o list_ser.jpg")
        #os.system("list_ser.txt")
        os.system("list_ser.jpg")
        #print("f en el chat")

        #para graficar en grapiz
    def graf_serpiente(self):

        f = open("list_ser.txt", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")

        temp_prin = self.primero_head
        #while temp_prin.siguiente is not None:    
        while temp_prin != None:    
            nodo_name = str(temp_prin.x_pos) + str(temp_prin.y_pos)
            nodo_corde = "(" + str(temp_prin.x_pos) + "," + str(temp_prin.y_pos) + ")"
            f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ nodo_corde +"|<f2> }\"];\n")  
            
            if (temp_prin.anterior == None):
                f.write("node_n1[label = \"null\"];\n")  
                f.write("node"+ nodo_name +":f0 -> node_n1;\n" )           
            
            f.write("node"+ nodo_name +"-> ")


            temp_prin = temp_prin.siguiente

            if (temp_prin != None):
                nodo_name_sig = str(temp_prin.x_pos) + str(temp_prin.y_pos)
                nodo_name_ante = str(temp_prin.anterior.x_pos ) + str(temp_prin.anterior.y_pos)
                f.write("node"+ nodo_name_sig +";\n")

                #regreoso
                #f.write("node"+ nodo_name_sig +"-> node" + nodo_name+";\n")
                f.write("node"+ nodo_name_sig +"-> node" + nodo_name_ante+";\n")

            else:
                f.write("node_n2;\n")  
                f.write("node_n2[label = \"null\"];\n")   

        f.write("}")
        f.close()

        os.system("dot -Tpng list_ser.txt -o list_ser.jpg")
        #os.system("list_ser.txt")
        os.system("list_ser.jpg")


#print("****************")
#lis_dob = ListaDob()

#lis_dob.Insert_fin(0, 0, "1")
#lis_dob.Insert_fin(0,1,"2")
#lis_dob.Insert_fin(0,2,"3")
 
##lis_dob.insert_inicio(10,21,"0*")
##lis_dob.insert_inicio(10,22,"-1*")
#lis_dob.Insert_fin(0,3, "4")
##lis_dob.insert_inicio(10,23,"-2*")

###lis_dob.delete_inicio()
##lis_dob.Lista_imprimir_atra()
##lis_dob.delete_fin()
##print("*** size: " + str(lis_dob.size) )
#lis_dob.Lista_imprimir_ade()
##lis_dob.Lista_imprimir_atra()

#print("1111111  fin para lista lis_dob")
#lis_tempo_22 = ListaDob()
#lis_tempo_22.Insert_fin(0, 0, "11a")
#lis_tempo_22.Insert_fin(0,1,"22a")
#lis_tempo_22.Insert_fin(0,2,"33a")
#lis_tempo_22.Lista_imprimir_ade()
#print("222222  fin para lista lis_tempo_22")
###lis_dob.graf_serpiente()
###lis_dob.Lista_imprimir_atra()
#print("imprime otra vez la lista 1")
#lis_dob.Lista_imprimir_ade()

#print("le asigno el valor de lista2 a lista1")
#lis_dob = lis_tempo_22
#lis_dob.Lista_imprimir_ade()
