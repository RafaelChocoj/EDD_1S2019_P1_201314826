import csv
from CircularDoble import ListaCir #para lista cicrular del usuario
lis_user = ListaCir()
class Import_data:

    def importando(self):
        archivo = open("users.csv")
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

    def retorno_users(self):
        return lis_user

#impo = Import_data()
#impo.importando()
#lis_user.Lista_imprimir_ade()
#lis_user.graf_users()