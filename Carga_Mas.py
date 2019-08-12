import csv
from CircularDoble import ListaCir #para lista cicrular del usuario
lis_user = ListaCir()
class Import_data:

    def importando(self, name_gamer):
        encontrado = False
        try:           
            #archivo = open("users.csv")
            archivo = open(name_gamer)
            reader = csv.DictReader(archivo)
            for row in reader:
                #print(row['Usuarios'])
                lis_user.Insert_nod(row['Usuarios'])

            #archivo = open("users.csv")
            #reader = csv.reader(archivo)
            #for row in reader:
            #    lis_user.Insert_nod(row[0])
            #    #print(row[0])

            #lis_user.Lista_imprimir_ade()
            encontrado = True
        except:
            #print("No existe ruta")
            encontrado = False
        return encontrado

    def new_user(self, name_gamer):
        lis_user.Insert_nod(name_gamer)

    def retorno_users(self):
        return lis_user

#impo = Import_data()
#impo.importando("123")
#lis_user.Lista_imprimir_ade()
#lis_user.graf_users()