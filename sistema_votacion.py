def menu():
    nav = int(input(f' BIENVENIDO AL SISTEMA DE VOTACIONES, QUE DESEA HACER HOY {'\n'} 1: VOTAR {'\n'} 2: ADMINISTRAR {'\n'} 0: SALIR {'\n'} => '))
    if nav == 1 :
        votante()
    elif nav == 2 :
        votante()
    elif nav == 0 :
        print(f'{'\n'} SALIENDO DEL SISTEMA ... {'\n'}')
    else:
        print(f'{'\n'} ENTRANA IRRECONOSIBLE, VUELVA A INTENTARLO {'\n'}')
        menu()

def votante():
    print(f'{'\n'} BUENOS DIAS QUERIDO VOTANTE ANTES DE PODER EJERCER SU DERECHO AL VOTO INGRESE SU ID PARA VERIFICAR SI SE ENCUENTRA AUTORIZADO A VOTAR {'\n'}')
    id = int(input(f' => '))
    verificacion_votante(id)

def admin(args):
    print(f' admin')
    menu()

def verificacion_votante(id) :
    print

menu()