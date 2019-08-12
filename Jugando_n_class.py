#Snake Battle royale como el fornais

from ListaDoble import ListaDob  # importando lista para serpiente
from PilaScore import PilaScore # importa pila para el score o puntuacion

from Lista_Obsta import ListaObtaculo

import random # para importar random 
import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN 

global snake_pos
global score
global punteo_total
punteo_total = 0

snake_pos = ListaDob() #lista doble serpiente
score = PilaScore() #pila para el 

global paredes
global paredes2
paredes = ListaObtaculo()
paredes2 = ListaObtaculo()

global score_total
score_total = PilaScore() 

global jugando_now
jugando_now = ""

##obtengo el jugador actual
#def Obtener_jugador(jugador = None):
#    jugando_now = jugador

def reset_snake_g():
    snake_limpio = ListaDob()
    return snake_limpio

def reset_score_g():
    score_limpio = PilaScore() 
    return score_limpio

def reset_paredes_g():
    paredes_limpio = ListaObtaculo()
    return paredes_limpio



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


def get_direction():
    return key_ante
#graficar score
def game_graf_score():
    score.graf_score()

#graficar snake
def game_graf_serpiente():
    snake_pos.graf_serpiente()

#snake actual
def get_snake():
    return snake_pos

#score actual
def get_score():
    return score

#obtener  puntos
def get_puntos():
    return score.size

#obtener  puntos totales
def get_puntos_totales():
    return score_total.size



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


    ##viendo si se con las paredes
    if (nivel >= 2):
        tempo_todo2 = snake_pos.primero_head 
        while (tempo_todo2 != None): 
            te_par1 = paredes.primero_head 
            while (te_par1 != None): 
                if (te_par1.x_pos == tempo_todo2.x_pos and te_par1.y_pos == tempo_todo2.y_pos):
                    muere = True
                te_par1 = te_par1.siguiente
            tempo_todo2 = tempo_todo2.siguiente

    return muere

def ObteniendoComida():
    global eat_x
    global eat_y
    eat_x = random.randint(3,58)
    eat_y = random.randint(3,18)

    #rando para obtener tipo de comidia
    # 0,2 = * (quita)
    # 1,3,4 = + (sumar)
    global xtipo_com
    xtipo_com = random.randint(0,5)
    #xtipo_com = random.randint(0,2)
    #if xtipo_com == 1:
    #    xtipo_com = 0

    if (nivel >= 2): 
        temp_par = paredes.primero_head
        while (temp_par != None): 
            if (temp_par.y_pos == eat_y and temp_par.x_pos == eat_x): 
                eat_x = random.randint(3,58)
                eat_y = random.randint(3,18)           
            temp_par = temp_par.siguiente
           
    temp_corde = snake_pos.primero_head
    while (temp_corde != None): 
        if (temp_corde.y_pos == eat_y and temp_corde.x_pos == eat_x): 
            eat_x = random.randint(3,58)
            eat_y = random.randint(3,18)           
        temp_corde = temp_corde.siguiente

    

    if (xtipo_com == 1 or xtipo_com == 3 or xtipo_com == 4 or xtipo_com == 5 or xtipo_com == 0):      
        window.addch(eat_y,eat_x,'+')
    #elif (xtipo_com == 0 or xtipo_com == 2):  
    elif (xtipo_com == 2):      
        window.addch(eat_y,eat_x,'*')
    #print("eat_y: " + str(eat_y) + " - eat_x: " + str(eat_x))
    #snake_pos.Lista_imprimir_ade()


def print_title(win,var):

    tit = "SNAKE (Battle Royale)"
    x_start = round((60-len(tit))/2)
    win.addstr(0,x_start,tit)
    puntos_score = " Score: " + str(score.size) + " "
    #global jugando_now
    if var == None:
        var = ""
    des_jug = " user : " + var + " "
    win.addstr(0,3,puntos_score)    
    x_start22 = round(58-len(des_jug))
    win.addstr(0,x_start22,des_jug) 

    pun_total = "Total: " + str(score_total.size ) + " "
    niv_game = "Nivel(" + str(nivel ) + ")"
    win.addstr(19,3,pun_total) 
    win.addstr(19,25,niv_game) 

def gano_nivel():
    gano = False
    #if score.size == 10:
    if score.size == 15:
        #global punteo_total
        #punteo_total = punteo_total + score.size
        gano = True
        
    return gano

#def nivel_2_o_mas():
#    ##paredes en x
#    paredes.Insert_fin(6,10, "par")
#    paredes.insert_fin(6,11, "par")
#    paredes.insert_fin(6,12, "par")

#    #paredes en y
#    paredes2.insert_fin(45,3, "par")
#    paredes2.insert_fin(45,4, "par")
#    paredes2.insert_fin(45,5, "par")

def imprimir_paredes():
    temp_pard = paredes.primero_head
    while (temp_pard != None):        
        window.addch(temp_pard.y_pos ,temp_pard.x_pos,'0') 
        temp_pard = temp_pard.siguiente

    #temp_pard2 = paredes2.primero_head
    #while (temp_pard2 != None):        
    #    window.addch(temp_pard2.y_pos ,temp_pard2.x_pos,'0') 
    #    temp_pard2 = temp_pard2.siguiente

def imprimir_paredes_nada():
    temp_pard = paredes.primero_head
    while (temp_pard != None):        
        window.addch(temp_pard.y_pos ,temp_pard.x_pos,' ') 
        temp_pard = temp_pard.siguiente

    #temp_pard2 = paredes2.primero_head
    #while (temp_pard2 != None):        
    #    window.addch(temp_pard2.y_pos ,temp_pard2.x_pos,' ') 
    #    temp_pard2 = temp_pard2.siguiente




def play_now(jugador, tipo_game, direc):
    global snake_pos
    global window
    global score
    global score_total

    global nivel
    global paredes
    global paredes2
    # si tipo_game 
    # 1 = continuar juego
    # 0 = juego nuevo

    stdscr = curses.initscr() #initialize console
    height = 20
    width = 60

    pos_y = 0
    pos_x = 0

    y_par1 = 0
    y_par2 = 0
    #nivel = 1
    
    window = curses.newwin(height,width,pos_y,pos_x) #create a new curses window
    window.keypad(True)     #enable Keypad mode
    curses.noecho()         #prevent input from displaying in the screen
    curses.curs_set(0)      #cursor invisible (0)
    window.border(0)        #default border for our window
    window.nodelay(True)    #return -1 when no key is pressed

    global key
    global key_ante


    if tipo_game == 0:
        key = KEY_RIGHT         #key defaulted to KEY_RIGHT
        key_ante = KEY_RIGHT         #key guarda el key anterior

        snake_pos = reset_snake_g() #si es nuevo reseteo lista
        score = reset_score_g()
        score_total = reset_score_g()
        paredes = reset_paredes_g()
    elif tipo_game == 1:
        key = direc
        key_ante = direc

    if tipo_game == 0:
        pos_x = 5               #cuando es nuevo juego inicia en 5 x
        pos_y = 5               #cuando es nuevo juego inicia en 5 y

    velocidad = 150 ##Buarda la velocidad del juego

    
    ##solo para preba inicio
    #key = KEY_LEFT
    #key_ante = KEY_LEFT
    #pos_x = 10               
    #pos_y = 5
    ##solo para preba fin

    #window.addch(pos_y,pos_x,'X')   #print initial dot

    #inicializo los primeros 3 del snake
    if tipo_game == 0:
        snake_pos.Insert_fin(pos_x, pos_y, None)
        pos_x = pos_x + 1
        snake_pos.Insert_fin(pos_x, pos_y, None)
        pos_x = pos_x + 1
        snake_pos.Insert_fin(pos_x, pos_y, None)
        nivel = 1


    elif tipo_game == 1:
        pos_conti = snake_pos.primero_head
        while pos_conti.siguiente is not None:  
            pos_conti = pos_conti.siguiente      
        pos_x = pos_conti.x_pos
        pos_y = pos_conti.y_pos

        if (nivel >= 2):
            ppar_conti = paredes.primero_head
            while ppar_conti.siguiente is not None:  
                ppar_conti = ppar_conti.siguiente      
            #pos_x = ppar_conti.x_pos
            y_par1 = ppar_conti.y_pos
        #print ("reanudar ("+ str(pos_x) +","+ str(pos_y)+")")
        
            ##paredes en y
            #paredes2.Insert_fin(45,y_par2, "par")
            #y_par2 = y_par2 +1
            #paredes2.Insert_fin(45,y_par2, "par")
            #y_par2 = y_par2 +1
            #paredes2.Insert_fin(45,y_par2, "par")


    ##inicializo los primeros 3 del snake
    #snake_pos.insert_inicio(pos_x, pos_y, None)
    #pos_x = pos_x - 1
    #snake_pos.insert_inicio(pos_x, pos_y, None)
    #pos_x = pos_x - 1
    #snake_pos.insert_inicio(pos_x, pos_y, None)

    ObteniendoComida()
    #print ("i("+ str(pos_x) +","+ str(pos_y)+")")
    print_title(window,jugador)
    while key != 27:                #run program while [ESC] key is not pressed
        #window.timeout(150)         #delay of 100 milliseconds
        #600
        gan = gano_nivel()
        if gan == True:
            nivel = nivel + 1 
            ########
            while True:
                tecla = window.getch()
                window.clear()                         
                window.border(0) 
                tit = "*** WINNER nivel(" + str(nivel) + ") ***"
                x_start = round((60-len(tit))/2)
                window.addstr(0,x_start,tit)

                puntos_score = " Score: " + str(score.size) + " "
                window.addstr(0,3,puntos_score)                   
                #ObteniendoComida()
                if tecla == 10: #ENTER

                    ###inicio##reset valores###
                    score = reset_score_g()
                    snake_pos = reset_snake_g()
                    paredes = reset_paredes_g()

                    print_title(window,jugador)
                    pos_x = 5        
                    pos_y = 5 
                    snake_pos.Insert_fin(pos_x, pos_y, None)
                    pos_x = pos_x + 1
                    snake_pos.Insert_fin(pos_x, pos_y, None)
                    pos_x = pos_x + 1
                    snake_pos.Insert_fin(pos_x, pos_y, None)
                    key = KEY_RIGHT       
                    key_ante = KEY_RIGHT   

                    if (nivel >= 2):
                        y_par1 = 12
                        y_par2 = 5
                        paredes.Insert_fin(30,y_par1, "par")
                        y_par1 = y_par1 +1
                        paredes.Insert_fin(30,y_par1, "par")
                        y_par1 = y_par1 +1
                        paredes.Insert_fin(30,y_par1, "par")
                        y_par1 = y_par1 +1
                        paredes.Insert_fin(30,y_par1, "par")
                        y_par1 = y_par1 +1
                        paredes.Insert_fin(30,y_par1, "par")

                    ObteniendoComida()
                    ###fin##reset valores###
                    break
            #######

            
                          

        #contador = contador + 1

        window.timeout(velocidad)  
        #window.timeout(400)  
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

        if (nivel >= 2):
            imprimir_paredes_nada()
            paredes.delete_inicio()
            #paredes2.delete_inicio()

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
        

        if key == KEY_RIGHT:                #right direction
            pos_x = pos_x + 1               #pos_x increase
        elif key == KEY_LEFT:               #left direction
            pos_x = pos_x - 1               #pos_x decrease
        elif key == KEY_UP:                 #up direction
            pos_y = pos_y - 1               #pos_y decrease
        elif key == KEY_DOWN:               #down direction
            pos_y = pos_y + 1               #pos_y increase
        
        if (nivel >= 2):    
            y_par1 = y_par1 + 1
            #y_par2 = y_par2 + 1    

        #verificando si se come algo
        ####################################################
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
        ####################################################

        if(pos_x == eat_x and pos_y == eat_y):
            #velocidad = velocidad - 100
            # 1,3,4, 5 , 0 = + (sumar)
            #if (xtipo_com == 1 or xtipo_com == 3 or xtipo_com == 4 or xtipo_com == 5):
            if (xtipo_com == 1 or xtipo_com == 3 or xtipo_com == 4 or xtipo_com == 5 or xtipo_com == 0):
                snake_pos.Insert_fin(pos_x, pos_y, None)
                score.insertNodo_Final(pos_x, pos_y, None)
                score_total.insertNodo_Final(pos_x, pos_y, None)

            # 2 = * (quita)
            elif (xtipo_com == 2):
            #elif (xtipo_com == 0 or xtipo_com == 2):
    
                tam_score = snake_pos.size
                if (tam_score >= 3):
                    snake_pos.delete_inicio()
                    score.eliminar_ultimo()
                    score_total.eliminar_ultimo()

            #window.addch(eat_y ,eat_x,' ')
            ser_imprimir_serpiente()
            print_title(window, jugador)

            if (xtipo_com == 1 or xtipo_com == 3 or xtipo_com == 4 or xtipo_com == 5 or xtipo_com == 0):
                if key == KEY_RIGHT:               
                    pos_x = pos_x + 1               
                elif key == KEY_LEFT:              
                    pos_x = pos_x - 1               
                elif key == KEY_UP:                 
                    pos_y = pos_y - 1              
                elif key == KEY_DOWN:               
                    pos_y = pos_y + 1              
        
            ObteniendoComida()

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
        ####################################################
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
        ####################################################

        if (y_par1 == height -1): # pos_x == 20
            y_par1 = 1
        elif (y_par1 == 0): # pos_x == 0
            y_par1 = 18

        #if (y_par2 == height -1): # pos_x == 20
        #    y_par2 = 1
        #elif (y_par2 == 0): # pos_x == 0
        #    y_par2 = 18

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

        if (nivel >= 2):
            paredes.Insert_fin(30, y_par1,  "par" )
            #paredes2.Insert_fin(45, y_par2,  "par" )
            imprimir_paredes()

        snake_pos.Insert_fin(pos_x, pos_y, None) 
        ser_imprimir_serpiente()

        #print("------")
        #ser_imprimir_serpiente_para_prueba()

        key_ante = key
        if keystroke is not  -1:    #key is pressed
            key = keystroke         #key direction changes

        #if (contador == 5):   
        #    key = 27 
        ##print ("tecla: " + str(key))
        

        te_moriste_we = is_death_snake()
        if (te_moriste_we == True):
            #print("te_moriste_we: " + str(te_moriste_we))
            tipo_game = 0
            key = 27
            #snake_pos.delete_fin()
            #snake_pos.Lista_imprimir_ade()
            
    
            
        
        ##para pausa
        if (key == 80 or key == 112):
            key = 27
            tipo_game = 1
            #print("-e_y: " + str(eat_y) + " - -e_x: " + str(eat_x))
            #print("xtipo_com : " + str(xtipo_com))
            #print("x : " + str(pos_x))
            #print("y : " + str(pos_y))
        ##print("tttttttt")
        
    curses.endwin() #return terminal to previous state
    return tipo_game

#play_now("-")

#snake_pos.graf_serpiente()
##snake_pos.Lista_imprimir_ade()
#score.graf_score()
##score.Lista_imprimir_ade()

