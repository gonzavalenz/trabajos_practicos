'''
El agente 0069 lleva años utilizando un método de codificación de mensajes secretos.
Si X es el mensaje original, éste se codifica en dos etapas:
1. X se transforma en X' reemplazando cada sucesión de caracteres consecutivos
que no sean vocales por su imagen especular.
X' se transforma en la sucesión de caracteres X'' obtenida al ir tomando sucesivamente:
el primer carácter de X', luego el último, luego el segundo, luego el penúltimo, etc.
Por ejemplo, para X = "Bond, James Bond", resultan:
X' = "BoJ ,dnameB sodn"
y
X'' = "BnodJo s, dBneam"
Lo que el pobre agente 0069 no sabe es que el señor Fon Noiman ha analizado algunos
mensajes cifrados y ha dado con el mecanismo que está utilizando. Lo único que le
queda a Fon Noiman es hacer el programa que, dado un mensaje cifrado, lo descifre.
'''

def encriptado1(cadena):
    cadena = 'a' + cadena  + 'a'
    nueva_cadena = ''
    vocales = 'aeiouAEOIU'
    i = 0
    while i < len(cadena):
        aux = ''
        if cadena[i] in vocales:
            nueva_cadena += cadena[i]
            while i + 1 < len(cadena) and cadena[i+1] not in vocales:
                i += 1
                aux += cadena[i]
            else:
                i += 1
            nueva_cadena += aux[::-1]
    return nueva_cadena[1:len(cadena)-1]

def encriptado2(cadena):
    nueva_cadena = ''
    agregar_ultimo_car = False
    if len(cadena) % 2 == 0:
        cadena_invertida = cadena[len(cadena):len(cadena)//2-1:-1]
        cadena = cadena[:len(cadena)//2:]
    else:
        cadena_invertida = cadena[len(cadena):(len(cadena)//2):-1]
        cadena = cadena[0:len(cadena)//2+1:]
        agregar_ultimo_car = True
    i = 0
    while len(cadena_invertida) != i:
        nueva_cadena += cadena[i] + cadena_invertida[i]
        i += 1
    if agregar_ultimo_car:
        nueva_cadena += cadena[len(cadena)-1]
    return nueva_cadena

def encriptado(cadena):
    return encriptado2(encriptado1(cadena))


def desencriptado1(cadena):
    nueva_cadena = ''
    cadena1 = '' 
    cadena2 = ''
    i = 0
    while len(cadena) > 1:
        cadena1 += cadena[i]
        cadena = cadena[1:] 
        cadena2 += cadena[i]       
        cadena = cadena[1:]
    cadena2 = cadena2[::-1]
    if len(cadena) > 0:
        cadena1 += cadena
    nueva_cadena = cadena1 + cadena2
    return nueva_cadena

def descifrar(cadena):
    return encriptado1(desencriptado1(cadena))

while True:
    print('''
1: Encriptar
2: Descifrar
3: Salir''')
    while True:
        try:
            eleccion = input('\n>')
            assert eleccion in ['1','2','3']
            break
        except:
            print('Opción no válida.')
    if eleccion == '1':
        frase = input('Ingrese la frase que quiere encriptar\n>')
        print(encriptado(frase))
    elif eleccion == '2':
        frase = input('Ingrese la frase que quiere descifrar\n>')
        print(descifrar(frase))
    else: 
        break