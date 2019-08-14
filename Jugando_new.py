#Snake Battle royale como el fornais

from ListaDoble import ListaDob  # importando lista para serpiente
from PilaScore import PilaScore # importa pila para el score o puntuacion

import random # para importar random 
import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

snake_pos = ListaDob() #lista doble serpiente
score = PilaScore() #pila para el 
global jugando_now
jugando_now = ""

#obtengo el jugador actual
def Obtener_jugador(jugador = None):
    jugando_now = jugador


#Imprimir vacios de la serpiente
def ser_imprimir_ade():
    temp_prin = snake_pos.primero_head
    while (temp_prin != None):   
        window.addch(temp_prin.y_pos ,temp_prin.x_pos,' ') 
        #print ("xd ("+ str(temp_prin.x_pos) +","+ str(temp_prin.y_pos)+")")
        temp_prin = temp_prin.siguiente

def ser_imprimir_serpiente():
    temp_prin = snake_pos.primero_head
    while (temp_prin != None):        
        window.addch(temp_prin.y_pos ,temp_prin.x_pos,'#') 
        #print ("ser ("+ str(temp_prin.x_pos) +","+ str(temp_prin.y_pos)+")")
        temp_prin = temp_prin.siguiente

def ser_imprimir_serpiente_para_prueba():
    temp_prin = snake_pos.primero_head
    while (temp_prin != None):        
        #print ("pser ("+ str(temp_prin.x_pos) +","+ str(temp_prin.y_pos)+")")
        temp_prin = temp_prin.siguiente

#obtiene el primer valor
def ser_primer_val():
    temp_prin_val = snake_pos.primero_head
    while (temp_prin_val != None):   
        #print ("xxx "+ str(temp_prin_val.x_pos))
        temp_prin_val = temp_prin_val.siguiente


#cambio de direccion
def snake_cambio_dir():
    snake_tempo_inver = ListaDob() #me va a servir para invertir direccion del snake
    #print("tempo es vacio?: " + str(snake_tempo_inver.esVacio()))
    temp_prin = snake_pos.primero_head 
    while (temp_prin != None):   
        snake_tempo_inver.insert_inicio(temp_prin.x_pos, temp_prin.y_pos,  temp_prin.valor)
        #print ("inver ("+ str(temp_prin.x_pos) +","+ str(temp_prin.y_pos)+")")
        temp_prin = temp_prin.siguiente
        
    return snake_tempo_inver

#snake actual
def get_snake():
    return snake_pos

#score actual
def get_score():
    return score

#verificando si se topa
def is_death_snake():
    muere = False
    #verificando si el snake muere
    #el ulitmo simpre sera la cabeza
    cabeza_del_snake_no_de_la_lista = snake_pos.primero_head
    while cabeza_del_snake_no_de_la_lista.siguiente is not None:  
        cabeza_del_snake_no_de_la_lista = cabeza_del_snake_no_de_la_lista.siguiente     

    ##se obtiene el ultimo
    cab_xx = cabeza_del_snake_no_de_la_lista.x_pos
    cab_yy = cabeza_del_snake_no_de_la_lista.y_pos

    ##viendo si se topa consigo mismo
    tempo_todo = snake_pos.primero_head 
    #while (tempo_todo != None):   
    while tempo_todo.siguiente is not None:  
        if (tempo_todo.x_pos == cab_xx and tempo_todo.y_pos == cab_yy):
            muere = True
        tempo_todo = tempo_todo.siguiente
    return muere



stdscr = curses.initscr() #initialize console

def ObteniendoComida():
    global eat_x
    global eat_y
    eat_x = random.randint(2,58)
    eat_y = random.randint(2,18)

    #rando para obtener tipo de comidia
    # 0,2 = * (quita)
    # 1,3,4 = + (sumar)
    global xtipo_com
    xtipo_com = random.randint(0,4)
    #xtipo_com = random.randint(0,2)

    #if xtipo_com == 1:
    #    xtipo_com = 0

    if (xtipo_com == 1 or xtipo_com == 3 or xtipo_com == 4):      
        window.addch(eat_y,eat_x,'+')
    elif (xtipo_com == 0 or xtipo_com == 2):      
        window.addch(eat_y,eat_x,'*')

    #eat_x = 38
    #eat_y = 5
    #window.addch(eat_y,eat_x,'+')
    ##print(str(eat_x) +","+ str(eat_y))

def print_title(win,var):
    #x_start = round((60-len(var))/2)  
    #win.addstr(0,x_start,var) 
    tit = " SNAKE (Battle Royale) "
    x_start = round((60-len(tit))/2)
    win.addstr(0,x_start,tit)
    puntos_score = " Score: " + str(score.size) + " "
    global jugando_now
    if jugando_now == None:
        jugando_now = ""
    des_jug = " User : " + jugando_now + " "
    win.addstr(0,5,puntos_score)    
    win.addstr(0,45,des_jug) 


height = 20
width = 60
pos_y = 0
pos_x = 0
window = curses.newwin(height,width,pos_y,pos_x) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
window.border(0)        #default border for our window
window.nodelay(True)    #return -1 when no key is pressed
key = KEY_RIGHT         #key defaulted to KEY_RIGHT
pos_x = 5               #initial x position
pos_y = 5               #initial y position

key_ante = KEY_RIGHT         #key guarda el key anterior

##solo para preba inicio
#key = KEY_LEFT
#key_ante = KEY_LEFT
#pos_x = 10               
#pos_y = 5
##solo para preba fin

#window.addch(pos_y,pos_x,'X')   #print initial dot

#inicializo los primeros 3 del snake
snake_pos.Insert_fin(pos_x, pos_y, None)
pos_x = pos_x + 1
snake_pos.Insert_fin(pos_x, pos_y, None)
pos_x = pos_x + 1
snake_pos.Insert_fin(pos_x, pos_y, None)

##inicializo los primeros 3 del snake
#snake_pos.insert_inicio(pos_x, pos_y, None)
#pos_x = pos_x - 1
#snake_pos.insert_inicio(pos_x, pos_y, None)
#pos_x = pos_x - 1
#snake_pos.insert_inicio(pos_x, pos_y, None)

ObteniendoComida()
contador = 0
print ("i("+ str(pos_x) +","+ str(pos_y)+")")
print_title(window,"")
while key != 27:                #run program while [ESC] key is not pressed
    #window.timeout(150)         #delay of 100 milliseconds
    #600
    contador = contador + 1
    window.timeout(500)  
    keystroke = window.getch()  #get current key being pressed

    #if keystroke is not  -1:    #key is pressed
    #    key = keystroke         #key direction changes
   
    #snake_cambio_dir()
    #ser_imprimir_ade()

    if (key == KEY_LEFT and key_ante == KEY_RIGHT):  ##esto quiere decir que se cambio de posicion IZ#
        snake_pos = snake_cambio_dir()

    elif (key == KEY_RIGHT and key_ante == KEY_LEFT):  ##esto quiere decir que se cambio de posicion DER#
        snake_pos = snake_cambio_dir()

    elif (key == KEY_DOWN and key_ante == KEY_UP): #cambio de pos de arriba hacia abajo
        snake_pos = snake_cambio_dir()
    
    elif (key == KEY_UP and key_ante == KEY_DOWN): #cambio de pos de arriba hacia abajo
        snake_pos = snake_cambio_dir()

    ser_imprimir_ade()
    
    #print("key: "+ str(key) +" - key_ante: "+ str(key_ante))
    #
    #if (key == KEY_LEFT and key_ante == KEY_RIGHT):  ##esto quiere decir que se cambio de posicion IZ#
    #    #####key = 27
    #    print("cambia a izquierda")
    #    snake_pos.delete_fin()
    #    #ser_imprimir_serpiente()
    #elif (key == KEY_LEFT and key_ante == KEY_LEFT): ##si va todo para la izquierda
    #    snake_pos.delete_fin()
    #
    #elif (key == KEY_RIGHT and key_ante == KEY_LEFT):  ##esto quiere decir que se cambio de posicion DER#
    #    print("cambia a la derecha")
    #    snake_pos.delete_inicio()
    #elif (key == KEY_RIGHT and key_ante == KEY_RIGHT): ##si va todo para la derecha
    #    print("solo para la derecha")
    #    snake_pos.delete_inicio()
    #
    #elif (key == KEY_DOWN and key_ante == KEY_DOWN): ##si va todo para abajo
    #    snake_pos.delete_inicio()
    #
    #else:
    #    snake_pos.delete_inicio()
    snake_pos.delete_inicio()
    #print("------")
    #ser_imprimir_serpiente_para_prueba()
    #print("------")

    #ser_imprimir_ade()
    ### si es derecha o abajo elimna el primero
    ##if (key == KEY_RIGHT or key == KEY_DOWN):        
    #snake_pos.delete_inicio()
    ##
    ##    #si es izquierda o arriba, elimina utimo
    ##elif (key == KEY_LEFT or key == KEY_UP):
    ##    snake_pos.delete_fin()
     

    if key == KEY_RIGHT:                #right direction
        pos_x = pos_x + 1               #pos_x increase
    elif key == KEY_LEFT:               #left direction
        pos_x = pos_x - 1               #pos_x decrease
    elif key == KEY_UP:                 #up direction
        pos_y = pos_y - 1               #pos_y decrease
    elif key == KEY_DOWN:               #down direction
        pos_y = pos_y + 1               #pos_y increase
    #window.addch(pos_y,pos_x,'X')       #draw new dot
    
    #print ("eat_x ="+ str(eat_x) +" eat_y ="+ str(eat_y)+" , ")
    
    #verificando si se come algo
    if(pos_x == eat_x and  pos_y == eat_y):
        # 1,3,4 = + (sumar)
        if (xtipo_com == 1 or xtipo_com == 3 or xtipo_com == 4):
            snake_pos.Insert_fin(pos_x, pos_y, None)
            score.insertNodo_Final(pos_x, pos_y, None)

        # 0,2 = * (quita)
        elif (xtipo_com == 0 or xtipo_com == 2):
 
            tam_score = snake_pos.size
            if (tam_score >= 3):
                snake_pos.delete_inicio()
                score.eliminar_ultimo()

        #window.addch(eat_y ,eat_x,' ')
        ser_imprimir_serpiente()
        print_title(window,"-")

        if (xtipo_com == 1 or xtipo_com == 3 or xtipo_com == 4):
            if key == KEY_RIGHT:                #right direction
                pos_x = pos_x + 1               #pos_x increase
            elif key == KEY_LEFT:               #left direction
                pos_x = pos_x - 1               #pos_x decrease
            elif key == KEY_UP:                 #up direction
                pos_y = pos_y - 1               #pos_y decrease
            elif key == KEY_DOWN:               #down direction
                pos_y = pos_y + 1               #pos_y increase
      

        ObteniendoComida()


    #pas = False
    if (key == KEY_LEFT and key_ante == KEY_RIGHT): #cambia de direcccion de derecha a izquierda
        #obtengo ultima posicion
        temp_prin = snake_pos.primero_head
        while temp_prin.siguiente is not None:  
            temp_prin = temp_prin.siguiente      
        #while temp_prin.anterior is not None: 
        #    temp_prin = temp_prin.anterior
    
        pos_x = temp_prin.x_pos
        pos_x = pos_x - 1
        #tambien tengo que obtener pos en y
        pos_y = temp_prin.y_pos
        #print("cabeza x ulitma: " + str(pos_x))
        #print("cabeza y ulitma: " + str(pos_y))
        
    
    elif (key == KEY_RIGHT and key_ante == KEY_LEFT): #de izquierda a derecha
        #obtengo ultima posicion
        temp_prin = snake_pos.primero_head
        while temp_prin.siguiente is not None:  
            temp_prin = temp_prin.siguiente      

        pos_x = temp_prin.x_pos
        pos_x = pos_x + 1
        #tambien tengo que obtener pos en y
        pos_y = temp_prin.y_pos

        #print("cabeza x : " + str(pos_x))
        #print("cabeza y : " + str(pos_y))

    elif (key == KEY_DOWN and key_ante == KEY_UP): #cambio de pos de arriba hacia abajo
        #obtengo ultima posicion
        temp_prin = snake_pos.primero_head
        while temp_prin.siguiente is not None:  
            temp_prin = temp_prin.siguiente      

        pos_x = temp_prin.x_pos
        pos_y = temp_prin.y_pos
        pos_y = pos_y + 1

        #print("cxabeza x : " + str(pos_x))
        #print("cxabeza y : " + str(pos_y))

    elif (key == KEY_UP and key_ante == KEY_DOWN): #cambio de pos de arriba hacia abajo
        #obtengo ultima posicion
        temp_prin = snake_pos.primero_head
        while temp_prin.siguiente is not None:  
            temp_prin = temp_prin.siguiente      

        pos_x = temp_prin.x_pos
        pos_y = temp_prin.y_pos
        pos_y = pos_y - 1

        #print("cxabeza x : " + str(pos_x))
        #print("cxabeza y : " + str(pos_y))
     
    ####para reiniciar o aparecer de otro lado
    # para posiciones de x
    if (pos_x == width - 1): # pos_x == 60
        pos_x = 1
    elif (pos_x == 0): # pos_x == 0
        pos_x = 58

    # para posiciones de y
    if (pos_y == height -1): # pos_x == 20
        pos_y = 1
    elif (pos_y == 0): # pos_x == 0
        pos_y = 18

    #if (key == KEY_LEFT and key_ante == KEY_RIGHT): #si cambia de direccion
    #    #key = 27
    #    ###obtengo el valor de X y Y de la posicion al inicio##
    #    tempo_primero = snake_pos.primero_head
    #    pos_x = tempo_primero.x_pos
    #    pos_y = tempo_primero.y_pos
    #    pos_x = pos_x -1
    #    print("cabeza x : " + str(pos_x))
    #    #print("cabeza y : " + str(pos_y))
    #    
    #    snake_pos.insert_inicio(pos_x, pos_y, None)
    #
    #elif (key == KEY_LEFT and key_ante == KEY_LEFT): #si va todo par la izquirda
    #    snake_pos.insert_inicio(pos_x, pos_y, None)
    #
    #elif (key == KEY_RIGHT and key_ante == KEY_LEFT): 
    #    #obtengo ultima posicion
    #    temp_prin = snake_pos.primero_head
    #    while temp_prin.siguiente is not None:  
    #        temp_prin = temp_prin.siguiente      
    #    #while temp_prin.anterior is not None: 
    #    #    temp_prin = temp_prin.anterior
    #
    #    pos_x = temp_prin.x_pos
    #    pos_x = pos_x + 1
    #    print("cabeza x ulitma: " + str(pos_x))
    #
    #    snake_pos.Insert_fin(pos_x, pos_y, None) 
    #
    #elif (key == KEY_RIGHT and key_ante == KEY_RIGHT): ##si va todo para la derecha
    #    snake_pos.Insert_fin(pos_x, pos_y, None) 
    #
    #elif (key == KEY_DOWN and key_ante == KEY_DOWN): ##si va todo para abajo
    #    snake_pos.Insert_fin(pos_x, pos_y, None)
    #
    #else:
    #    snake_pos.Insert_fin(pos_x, pos_y, None)

    #print("*1*******cont" + str(contador) +": " + str(pos_x))
    snake_pos.Insert_fin(pos_x, pos_y, None) 
    ser_imprimir_serpiente()

    #print("------")
    #ser_imprimir_serpiente_para_prueba()

    key_ante = key
    if keystroke is not  -1:    #key is pressed
        key = keystroke         #key direction changes

    
    ##solo para prueba
    #if pas == True:
    #    key = 27

    #if (contador == 5):   
    #    key = 27 
    ##print ("tecla: " + str(key))
    
    #if (contador == 2): 
    #    ##para probar izquierda, cambio direccion
    #    #key = KEY_LEFT
    #
    #    #para probar derecha, cambio direccion
    #    key = KEY_RIGHT

    te_moriste_we = is_death_snake()
    if (te_moriste_we == True):
        print("te_moriste_we: " + str(te_moriste_we))
        key = 27
    
    if (key == 80 or key == 112):
        key = 27
    ##print("tttttttt")
    
curses.endwin() #return terminal to previous state

#snake_pos.graf_serpiente()
##snake_pos.Lista_imprimir_ade()
#score.graf_score()
##score.Lista_imprimir_ade()

