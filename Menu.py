
import curses #import the curses library
import time
from Carga_Mas import Import_data #para importar datos en csv

#####
from CircularDoble import ListaCir #para lista cicrular del usuario
lis_user = ListaCir()
#####

## usuario_actual_play
usuario_actual_play = None

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

data_im = Import_data()


def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,21, '1. Play (Battle Royale)')             #paint option 1
    win.addstr(8,21, '2. Scoreboard')       #paint option 2
    win.addstr(9,21, '3. User Selection')   #paint option 3
    win.addstr(10,21, '4. Reports')         #paint option 4
    win.addstr(11,21, '5. Bulk Loading')    #paint option 5
    win.addstr(12,21, '6. Exit')            #paint option 6
    win.timeout(-1)                         #wait for an input thru the getch() function

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()

def paint_reports(win):
    paint_title(win,' REPORTS ')         
    win.addstr(7,21, '1. Snake Report')            
    win.addstr(8,21, '2. Score Report')      
    win.addstr(9,21, '3. Scoreboard Report')  
    win.addstr(10,21, '4. Users Report')        
    win.addstr(12,21, '(ESC). Salir')            
    #win.timeout(-1)    
               
#para seleccionar reportes
def report_seleccion(win):
     
    while True:
        paint_reports(win)
        tecla = window.getch()
        
        if tecla == 49: #1
            break
        elif tecla == 50: #2
            break
        elif tecla == 51: #3
            break
        elif tecla == 52: #4
            ## inicio verificando si tiene usuarios ingresados
            paint_title(win, '4. Users Report')
            user_actual = lis_user.primero_head
            if (user_actual == None):
                pintar_usuarios(win, "No tiene usuarios ingresados")
                while True:
                    tecla = window.getch()
                    if tecla == 27:
                        break
            else:
                lis_user.graf_users()

            ## fin verificando si tiene usuarios ingresados
        elif tecla == 27:
            break

#empezar a jugar
def play_snake(win):
    if (usuario_actual_play == None):
        pintar_usuarios(win, "Seleccione Usuario para Jugar")
        while True:
            tecla = win.getch()
            if tecla == 27:
                break
    else:     
        while True:
            tecla = win.getch()
            paint_title(win,"Presione una tecla")
            win.addstr(8,21, 'Aceptar')    
            import Jugando_new 
            if tecla == 27:
                break
            

#para seleccionar usuarios
def user_seleccion(win):
    user_actual = lis_user.primero_head

    ##verificando si tiene usuarios ingresados
    if (user_actual == None):
        pintar_usuarios(win, "No tiene usuarios ingresados")
        while True:
            tecla = window.getch()
            if tecla == 27:
                break
    else:     
        user_name = user_actual.user
        user_name = "<--- " + user_name + " --->"
        pintar_usuarios(win, user_name)

        ##key_selec = window.getch()
        #print("00 pirn " + str(window.getch()))
        while True:
            #tecla = stdscr.getch()
            tecla = win.getch()
            if tecla == curses.KEY_RIGHT:
                user_actual = user_actual.siguiente

                paint_title(window,' 3 - USER SELECTION ')
                user_name = user_actual.user
                user_name = "<--- " + user_name + " --->"
                pintar_usuarios(win, user_name)
        
            elif tecla == curses.KEY_LEFT:
                user_actual = user_actual.anterior

                paint_title(window,' 3 - USER SELECTION ')
                user_name = user_actual.user
                user_name = "<--- " + user_name + " --->"
                pintar_usuarios(win, user_name)

            #si se preciona enter se selecciona el usuario
            elif tecla == 10:
                global usuario_actual_play
                usuario_actual_play = user_actual.user
                break
            elif tecla == 27:
                break
            
    

def pintar_usuarios(win, user):
    #stdscr.clear()
    #altura, ancho = stdscr.getmaxyx()
    #paint_title(window, ' USER SELECTION ')
    altura = 20 
    ancho = 60
    ######curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    y = int(altura/2)
    x = int(int(ancho/2) - (len(user)/2))
    #x = int(int(ancho/2) - (len(menu[index])/2))
    #stdscr.addstr(y,x, menu[index], curses.color_pair(2))
    #win.addstr(y,x, user, curses.color_pair(2))
    win.addstr(y,x, user )
    win.refresh()

def import_archiv(win):

    while True:
        tecla = window.getch()
        if tecla == 115:
            paint_title(window,' 5 - BULK LOADING ')
            win.addstr(7,21, 'Importando Datos') 
            window.addstr(8,5, '(Datos importados) Presione una tecla para salir')
            data_im.importando()
            #print("asdasdasdas")
            global lis_user
            lis_user = data_im.retorno_users()
            ##lis_user.Lista_imprimir_ade()
            #lis_user.graf_users()
            tecla = window.getch()
            #window.timeout(-1)   
            break

        elif tecla == 110:
            break

        elif tecla == 27:
            break


def import_archiv_solo_prueba(win):
    sale = False
    key = window.getch()
    if (key == 27 or key == 110):
        sale = True
    if(key==115):
        paint_title(window,' 5 - BULK LOADING ')
        win.addstr(7,21, 'Importando Datos') 
        window.addstr(8,15, '(Datos importados) Presione una tecla para salir')  
        data_im.importando()
        #print("asdasdasdas")
        global lis_user
        lis_user = data_im.retorno_users()
        ##lis_user.Lista_imprimir_ade()
        #lis_user.graf_users()

        sale = False
    while (sale != True):
        key = window.getch()

        sale = True



stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        #import Jugando
        paint_title(window, ' PLAY (Batlle Royal)')
        
        #wait_esc(window)
        play_snake(window)
        
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SCOREBOARD ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' USER SELECTION ')
        #wait_esc(window)
        user_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' REPORTS ')
        #wait_esc(window)
        report_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' 5 BULK LOADING ')
        window.addstr(7,21, '¿Desea importar Usuarios?')            
        window.addstr(8,21, 'S/N')  

        #print(window.getch())
        #if(window.getch() == 110):
        #    paint_menu(window)

        #wait_esc(window)
        import_archiv(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        #print("user actual: " + usuario_actual_play)
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state
