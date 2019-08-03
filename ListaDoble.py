class NodeDo:
    def __init__(self, x_pos = None, y_pos = None, valor = None ):    
        self.valor = valor
        self.x_pos = x_pos    
        self.y_pos = y_pos    

        self.siguiente = None       
        self.anterior =  None   

class ListaDob:
    def __init__(self):        
        self.primero_head = None 
        self.size = 0
        #self.ultimo = None

    def esVacio(self):
        return self.primero_head is None

    #para insertar nodo al principio
    def insert_inicio(self, x_pos, y_pos, valor):
    
        new_nod = NodeDo(x_pos, y_pos, valor)
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
        new_nod = NodeDo(x_pos, y_pos, valor)

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

            
    #Imprimir lista adelante
    def Lista_imprimir_ade(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head
            while temp_prin.siguiente is not None:        
                print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )        
                temp_prin = temp_prin.siguiente
            #print(temp_prin.valor)
            print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 

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




#lis_dob = ListaDob()
#
#lis_dob.Insert_fin(0, 0, "1")
#lis_dob.Insert_fin(0,1,"2")
#lis_dob.Insert_fin(0,2,"3")
# 
#lis_dob.insert_inicio(10,21,"0*")
#lis_dob.insert_inicio(10,22,"-1*")
#lis_dob.Insert_fin(0,3, "4")
#lis_dob.insert_inicio(10,23,"-2*")

#lis_dob.delete_inicio()
#lis_dob.Lista_imprimir_ade()
#print("*** size: " + str(lis_dob.size) )
#lis_dob.Lista_imprimir_atra()
