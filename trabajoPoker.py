import random

mazo = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP', 'AP', '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '10T', 'JT', 'QT', 'KT', 'AT']
random.shuffle(mazo)


valoresEspeciales1 = {
    'A': 1,
    'J': 11,
    'Q': 12,
    'K': 13
}


palos_posibles = ['C', 'D', 'P', 'T']
valores_posibles = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def generarMano():
    # Elegir 5 cartas del mazo 
    return random.sample(mazo,5)

def ingresarMano():
    # Ingresar las cartas
    mano = []
    for i in range(5):
        while True:
            try:
                carta = input('Ingrese una carta: ')
                carta = carta.upper()
                assert carta in mazo         
                assert carta not in mano
                mano.append(carta)
                break
            except:
                print('La carta no es válida.')
    return mano


def cartasIguales(mano, *args):
    # Si la mano tiene la cantidad de cartas iguales que se pasa como parametro
    cont = [0 for i in range(14)]
    for carta in mano:
        num = carta[0:len(carta)-1]
        if num in valoresEspeciales1:
            num = valoresEspeciales1[num]
        cont[int(num)] += 1
    if cont.count(2) == 2:
        cont[0] = 5
    for num in args:
        if num not in cont:
            return False
    return True

def manoColor(mano):
    # Si la mano tiene el mismo color 
    return len(set([carta[-1] for carta in mano])) == 1
    
def reemplazarValores(valores):
    # Reemplazar J, Q, K y A
    for i in range(len(valores)):
        if valores[i] in valoresEspeciales1:
            valores[i] = valoresEspeciales1[valores[i]]
        valores[i] = int(valores[i])
    return valores

def valoresMano(mano):
    # Ordenar los valores de una mano
    valores = [mano[i][0:len(mano[i])-1] for i in range(5)]
    valores = reemplazarValores(valores)
    valores = sorted(valores)
    return valores

def escalera(mano):
    # Si los valores estan en escalera
    lista = valoresMano(mano)
    for i in range(4):
        if int(lista[i])+1 != int(lista[i+1]):
            return False
    return True

def escaleraMayor(mano):
    # Si es una escalera de 10, J, Q, K, A
    listaAux = ['10','J','Q','K','A']
    mano = [mano[i][0:(len(mano[i])-1)] for i in range(5)]
    for valor in listaAux:
        if valor not in mano:
            return False
    return True

while True:
    print('''
1: Generar mano.
2: Ingresar mano.
3: Salir
''')
    while True:
        try: 
            eleccion = input('>')
            assert eleccion in ('1','2','3')
            break
        except:
            print('Opción no válida.')
            
    if eleccion == '1':
        mano = generarMano()
    elif eleccion == '2':
        mano = ingresarMano()
    else: break

    print('')
    for carta in mano: print(carta,end='  ')
    print('')
    if manoColor(mano) and escaleraMayor(mano):
        print('Escalera Real')
    elif escalera(mano) and manoColor(mano):
        print('Escalera de color')
    elif cartasIguales(mano,4,1):
        print('Poker')
    elif cartasIguales(mano,3,2):
        print('Full')
    elif manoColor(mano):
        print('Color')
    elif escalera(mano) or escaleraMayor(mano):
        print('Escalera')
    elif cartasIguales(mano,3,1):
        print('Trio')
    elif cartasIguales(mano,5,2,1):
        print('Doble parejas')
    elif cartasIguales(mano,2,1):
        print('Pareja')
    else:
        print('Carta alta')