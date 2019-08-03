class NodeDo:

    def __init__(self, valor):    
        self.valor = valor         
        self.siguiente = None       
        self.anterior =  None   

class ListaDoble:
    def __init__(self):        
        self.primero_head = None 
        self.size = 0
        #self.ultimo = None

    def esVacio(self):
        return self.primero_head is None

    #para insertar nodo al principio
    def insert_inicio(self, valor):
    
        new_nod = NodeDo(valor)
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
    def Insert_fin(self, valor):
        new_nod = NodeDo(valor)

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
            
    #Imprimir lista adelante
    def Lista_imprimir_ade(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head
            while temp_prin.siguiente is not None:        
                print(temp_prin.valor)        
                temp_prin = temp_prin.siguiente
            print(temp_prin.valor)

    #Imprimir lista atras
    def Lista_imprimir_atra(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:

            temp_prin = self.primero_head
            while temp_prin.siguiente is not None:  
                temp_prin = temp_prin.siguiente      
            while temp_prin.anterior is not None: 
                print(temp_prin.valor)
                temp_prin = temp_prin.anterior
            print(temp_prin.valor)




#lis_dob = ListaDoble()

#lis_dob.Insert_fin("1")
#lis_dob.Insert_fin("2")
#lis_dob.Insert_fin("3")
 
#lis_dob.insert_inicio("0*")
#lis_dob.insert_inicio("-1*")
#lis_dob.Insert_fin("4")
#lis_dob.insert_inicio("-2*")

#lis_dob.Lista_imprimir_ade()
#print("size: " + str(lis_dob.size) )

#lis_dob.Lista_imprimir_atra()
