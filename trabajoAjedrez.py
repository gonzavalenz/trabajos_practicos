# La posición es definida como (x,y)

tablero = [
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*']
]

def jaque_peon(peon, rey):
    if peon[1]+1 == rey[1]:
        if peon[0] + 1 == rey[0] or peon[0] - 1 == rey[0]:
            return True
    return False

def jaque_alfil(alfil, rey):
    return abs(alfil[0] - rey [0]) == abs(alfil[1] - rey [1])

def jaque_torre(torre, rey):
    return torre[0] == rey[0] or torre[1] == rey[1]

def jaque_caballo(caballo, rey):
    valor_absoluto = ((abs(caballo[0]-rey[0])),(abs(caballo[1]-rey[1])))
    return 1 in valor_absoluto and 2 in valor_absoluto

def jaque_reina(reina, rey):
    return jaque_torre(reina,rey) or jaque_alfil(reina,rey)

def jaque_rey(rey1, rey2):
    valor_absoluto = ((abs(rey1[0]-rey2[0])),(abs(rey1[1]-rey2[1])))
    valores_absolutos = [(1,0),(1,1),(0,1)]
    return valor_absoluto in valores_absolutos

def pedir_valores(verif_peon = None):
    while True: 
        try:
            x = int(input('Ingrese la posición en X: '))
            assert 1 <= x <= 8
            break
        except:
            print('Posición no válida.')
    
    while True:
        try:    
            y = int(input('Ingrese la posición en Y: '))
            if verif_peon == 'P':
                assert 1 < y < 8
            else:
                assert 1 <= y <= 8
            break
        except:
            print('Posición no válida.')
            
    return (x,y)

def divisor():
    for i in range(50):
        print('=', end='')
    print('')

def opciones():
    print('''
Piezas para elegir:

    Peon: P         Torre: T        Alfil: A

    Caballo: C      Reina: Q        Rey: K

    Salir: S
    ''')

def eleccion_opcion():
    valores = ['S','T','P','A','C','Q','K']
    while True:
        try:
            opciones()
            opcion = input('Ingrese la opción que desea: ')
            opcion = opcion.upper()
            assert opcion in valores
            divisor()
            break
        except:
            divisor()
            print('Opción no válida.')
        divisor()
    return opcion

def mostrar_resultado(resultado):
    if resultado:
        print('El rey esta en jaque.')
    else:
        print('El rey esta pancho como perro por su casa.')

def mostrar_tablero():
    divisor()
    for i in range(7,-1,-1):
        print(i+1,end='|')
        for x in range(8):
            print(tablero[i][x],end='|')
        print()
    print(' ', end=' ')
    for i in range(1,9):
        print(i, end=' ')
    print('')
    divisor()

def agregar_piezas(tipo_pieza,pos_pieza,pos_rey):
    tablero[pos_pieza[1]-1][pos_pieza[0]-1] = tipo_pieza
    tablero[pos_rey[1]-1][pos_rey[0]-1] = 'K'

def limpiar_tablero():
    for i in range(8):
        for x in range(8):
            tablero[i][x] = '*'
        

if __name__=='__main__':
    divisor()
    print('''
                Bienvenido al TP

    En este programa se puede saber si el rey esta en jaque 
    a partir de las coordenadas de las piezas.
    ''')
    divisor()

    while True:
        divisor()
        eleccion = eleccion_opcion()
        
        if eleccion == 'S':
            exit()
        
        while True:
            try:
                mostrar_tablero()
                print('Ingrese la posición de la pieza: ')
                pieza = pedir_valores(eleccion)
                print('Ingrese la posición del Rey: ')
                rey = pedir_valores()
                break
            except:
                print('Las posiciones son iguales, por favor vuelva a ingresar las posiciones.')
                divisor()
        
        print(pieza,rey)

        if eleccion == 'P':
                resultado = jaque_peon(pieza,rey)
                agregar_piezas(eleccion,pieza,rey)
        elif eleccion == 'T':
            resultado = jaque_torre(pieza,rey)
            agregar_piezas(eleccion,pieza,rey)
        elif eleccion == 'A':
            resultado = jaque_alfil(pieza,rey)
            agregar_piezas(eleccion,pieza,rey)
        elif eleccion == 'C':
            resultado = jaque_caballo(pieza,rey)
            agregar_piezas(eleccion,pieza,rey)
        elif eleccion == 'Q':
            resultado = jaque_reina(pieza,rey)
            agregar_piezas(eleccion,pieza,rey)
        elif eleccion == 'K':
            resultado = jaque_rey(pieza,rey)
            agregar_piezas(eleccion,pieza,rey)
        
        mostrar_tablero()
        mostrar_resultado(resultado)
        divisor()
        limpiar_tablero()