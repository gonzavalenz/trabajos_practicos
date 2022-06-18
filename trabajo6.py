'''
imagen: NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV
imagen comprimida: (N8)BRAVB(R5)(A7)(V5)
'''

def comprimir_imagen(imagen):
    contador = 1
    imagen_comprimida = ''
    for c, i in zip(imagen,range(len(imagen))):
        if i != 0:
            if c == imagen[i-1]:
                contador += 1
                if i + 1 < len(imagen):
                    if c != imagen[i+1]:
                        imagen_comprimida += f'({c}{contador})'
                        contador = 1
                else:
                    imagen_comprimida += f'({c}{contador})'
            else:
                if c != imagen[i+1]:
                    imagen_comprimida += f'{c}'
        else:
            if c != imagen[i+1]:
                imagen_comprimida = f'{c}'
    return imagen_comprimida

def descomprimir_imagen(imagen):
    imagen = imagen.replace('(','')
    imagen = imagen.replace(')','')
    numeros = '0123456789'
    imagen_descomprimida = ''
    for c, i in zip(imagen,range(len(imagen))):
        if c in numeros:
            numero = c
            contador = 1
            while imagen[i+contador] in numeros:
                numero += c
                contador += 1
            imagen_descomprimida += f'{imagen[i-1]}'*int(numero)
        else:
            if i + 1 < len(imagen) and imagen[i+1] not in numeros:
                imagen_descomprimida += c
            elif i+1 == len(imagen):
                imagen_descomprimida += c
    return imagen_descomprimida

print(comprimir_imagen('NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV'))
print(descomprimir_imagen('(N8)BRAVB(R5)(A20)V'))