
from ListaDoble import ListaDob  # importando lista para serpiente
#snake_pos = ListaDob() #lista doble serpiente

print("****************")
lis_dob = ListaDob()

lis_dob.Insert_fin(0, 0, "1")
lis_dob.Insert_fin(0,1,"2")
lis_dob.Insert_fin(0,2,"3")
lis_dob.Insert_fin(0,3, "4")

lis_dob.Lista_imprimir_ade()

####inicia para invertir
print("1111111  fin para lista lis_dob")
lis_tempo_22 = ListaDob()
temp_prin = lis_dob.primero_head
while (temp_prin != None):   
    lis_tempo_22.insert_inicio(temp_prin.x_pos, temp_prin.y_pos,  temp_prin.valor)
    temp_prin = temp_prin.siguiente

#lis_tempo_22.Insert_fin(0, 0, "11a")
#lis_tempo_22.Insert_fin(0,1,"22a")
#lis_tempo_22.Insert_fin(0,2,"33a")
lis_tempo_22.Lista_imprimir_ade()
print("222222  fin para lista lis_tempo_22")
print("imprime otra vez la lista 1")
lis_dob.Lista_imprimir_ade()

print("le asigno el valor de lista2 a lista1")
lis_dob = lis_tempo_22
lis_dob.Lista_imprimir_ade()
