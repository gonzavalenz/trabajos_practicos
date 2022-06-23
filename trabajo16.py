import random
import time
import os 
import platform

sistema = platform.system()
if sistema == 'Windows': limpiar = 'cls'
else: limpiar = 'clear'

posMapita = []

def configurar():
    while True:
        try:
            mapX = int(input('Ingrese el ancho del mapa\n>'))
            assert 3 <= mapX <= 23
            break
        except:
            print('El ancho tiene que ser igual o mayor a 3 e igual o menor a 23.')
    while True:
        try:
            mapY = int(input('Ingrese el alto del mapa\n>'))
            assert 3 <= mapY <= 23
            break
        except:
            print('El alto tiene que ser igual o mayor a 3 e igual o menor a 23.')
    maxNaufragos = mapX*mapY
    while True:
        try:
            numN = int(input('Ingrese la cantidad de naufragos\n>'))
            assert numN < maxNaufragos 
            break
        except:
            print(f'La cantidad de naufragos tiene que ser menor a {maxNaufragos}.')
    maxVidas = maxNaufragos-1
    while True:
        try:
            vidas = int(input('Ingrese la cantidad de vidas\n>'))
            assert vidas < maxVidas
            break
        except:
            print(f'La cantidad de vidas tiene que ser menor a {maxVidas}')
    return mapX, mapY, numN, vidas

def insertarNaufragos(mapa,numN):
    naufragos = random.sample(posMapita,numN)
    for naufrago in naufragos:
        mapa[naufrago[1]][naufrago[0]] = 'N'
    return mapa

def crearMapa(numX,numY):
    mapita = []
    for y in range(numY):
        subMapita = []
        for x in range(numX):
            subMapita.append('X')
            posMapita.append([x,y])
        mapita.append(subMapita)
    return mapita

def mostrarMapa(mapita,numX,vidasRestantes,naufragos,naufragosEncontrados):
    for i, linea in enumerate(mapita):
        for x in linea:
            print(x,end='  ')
        print(i+1)
    for i in range(numX):
        print(i+1,end='  ')
    print(f'\nVidas: {vidasRestantes}\nNaufragos restantes: {naufragos-naufragosEncontrados}\nNaufragos encontrados: {naufragosEncontrados}')

def buscandoMapa(mapa):
    os.system(limpiar)
    contador = 0
    ancho = len(mapa[0])
    for i in range(len(mapa)):
        os.system(limpiar)
        print('BUSCANDO...')
        for i, linea in enumerate(mapa):
            if contador == i:
                for x in range(ancho):
                    print('_',end='  ')
            else:
                for x in linea:
                    print(x,end='  ')
            print('')
        contador += 1
        time.sleep(0.1)
    os.system(limpiar)    
        
def reemplazarMapa(mapa, pos, c):
    mapa[pos[1]][pos[0]] = c
    

def encontrarNaufrago(mapa,pos):
    return mapa[pos[1]][pos[0]] == 'N' 

def naufragoCerca(mapa,pos):
    if pos[1]-1 > 0: 
        if mapa[pos[1]-1][pos[0]] == 'N': return True
    if pos[1]+1 < len(mapa): 
        if mapa[pos[1]+1][pos[0]] == 'N': return True
    if pos[0]+1 < len(mapa[0]): 
        if mapa[pos[1]][pos[0]+1] == 'N': return True
    if pos[0]-1 > 0:
        if mapa[pos[1]][pos[0]-1] == 'N': return True 
    return False

def pedirPos(maxX,maxY):
    while True:
        try:
            x = int(input('\nIngrese la posición en X:\n>'))
            assert x <= maxX
            break
        except:
            print('Posición no válida.')
    while True:
        try:
            y = int(input('\nIngrese la posición en Y:\n>'))
            assert y <= maxY
            break
        except:
            print('Posición no válida.')
    return [x-1,y-1]

if __name__ == '__main__':    
    os.system(limpiar)
    mapX, mapY, numN, vidas, naufragosSalvados = 5, 5, 3, 10, 0
    while True:
        print('NAUFRAGOS GAME\n\n\t1: Jugar!\n\t2: Configurar\n\t3: Salir\n')
        while True:
            try:
                eleccion = int(input('>'))
                assert eleccion in [1,2,3]
                break
            except:
                print('Opción no válida')
        if eleccion == 1:
            mapaMostrar = crearMapa(mapX,mapY)
            mapaNaufragos = insertarNaufragos(crearMapa(mapX,mapY),numN)
            contadorVidas = vidas
            contadorNaufragos = numN
            naufragosSalvados = 0
            while True:
                os.system(limpiar)
                mostrarMapa(mapaMostrar,mapX,contadorVidas,contadorNaufragos,naufragosSalvados)
                pos = pedirPos(mapX,mapY)
                buscandoMapa(mapaMostrar)
                if encontrarNaufrago(mapaNaufragos,pos):
                    reemplazarMapa(mapaMostrar,pos,'N')
                    reemplazarMapa(mapaNaufragos,pos,'X')
                    naufragosSalvados += 1 
                elif naufragoCerca(mapaNaufragos,pos):
                    reemplazarMapa(mapaMostrar,pos,'*')
                else:
                    contadorVidas -= 1
                mostrarMapa(mapaMostrar,mapX,contadorVidas,contadorNaufragos,naufragosSalvados)
                if naufragosSalvados == numN:
                    print('\n\n\nGANASTE!!! :)\n\n\n')
                    break
                if contadorVidas == 0:
                    print('\n\nPerdiste Perdiste no hay nadie peor que vos!\n\n\n')
                    break
        elif eleccion == 2:
            mapX, mapY, numN, vidas = configurar()
            posMapita = []
            os.system(limpiar)
        elif eleccion == 3:
            os.system(limpiar)
            break

