'''
imagen: NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV
imagen comprimida: (N8)BRAVBB(R5)(A7)(V5)
'''

def comprimir_imagen(imagen):
    imagen_comprimida = ''
    c = 0
    while c < len(imagen):
        subcontador = 0
        caracter = imagen[c]
        while c < len(imagen) and caracter == imagen[c]:
            c += 1
            subcontador += 1
        if subcontador > 4:
            imagen_comprimida += f'({caracter}{subcontador})'
        else:
            imagen_comprimida += caracter * subcontador

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

print(comprimir_imagen('NNNNNNNNBRAAVBRRRRRAAAAAAAVVVVVVVVVVVVVVVVVVVVVVV'))
print(descomprimir_imagen('(N8)BRAVB(R5)(A20)V'))