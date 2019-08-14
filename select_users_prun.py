from CircularDoble import ListaCir #para lista cicrular del usuario
import curses
import time



menu = ["menu 1--->", "<---menu 2--->", "<---menu 3--->", "<---menu 4"]


def main(stdscr):
    lis_user = ListaCir()
    lis_user.add_ejemplo()
    #lis_user.Insert_nod("pokoyo")
    #lis_user.Insert_nod("nose1")
    #lis_user.Lista_imprimir_ade()

    user_actual = lis_user.primero_head

    curses.curs_set(0)
    index = 0
    #pintar_menu(stdscr,0)
    user_name = user_actual.user
    user_name = "<--- " + user_name + " --->"
    pintar_menu(stdscr, user_name)
    while True:
        tecla = stdscr.getch()
        if tecla == curses.KEY_RIGHT:
            index = index + 1
            user_actual = user_actual.siguiente
        elif tecla == curses.KEY_LEFT:
            index =index - 1
            user_actual = user_actual.anterior
        elif tecla == 27:
            break
        
        if index < 0:
            index = 0
        if index >= len(menu):
            index = len(menu) -1
        #pintar_menu(stdscr, index)
        user_name = user_actual.user
        user_name = "<-1-- " + user_name + " -1-->"
        pintar_menu(stdscr, user_name)
        

def pintar_ventana(stdscr):
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))
    stdscr.box("#","&")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

#def pintar_menu(stdscr, index):
def pintar_menu(stdscr, user):
    stdscr.clear()
    pintar_ventana(stdscr)
    altura, ancho = stdscr.getmaxyx()
    #altura = 20 
    #ancho = 60
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    y = int(altura/2)
    x = int(int(ancho/2) - (len(user)/2))
    #x = int(int(ancho/2) - (len(menu[index])/2))
    #stdscr.addstr(y,x, menu[index], curses.color_pair(2))
    stdscr.addstr(y,x, user, curses.color_pair(2))
    stdscr.refresh()

curses.wrapper(main)

