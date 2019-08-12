import random

class rando:
   

    def Random_comida():
        #rando para obtener tipo de comidia
        # 0,2 = * (quita)
        # 1,3,4 = + (sumar)
        ran_x = random.randint(0,4)
        ran_y = random.randint(1,1)
        print(str(ran_x) +","+ str(ran_y))

al = rando
al.Random_comida()