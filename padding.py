# padding.py
# Kevin Joan Delgado Pérez A01706328
# Versión 1
# Herramientas computacionales: El arte de la programación

import numpy as np

def padding(imagen, psize):

    imagen_row, imagen_col = imagen.shape #asignar el alto y ancho de la imagen

    padded_imagen = np.zeros((imagen_row + (2 * psize), imagen_col + (2 * psize))) #Realizar el padding llenándolo con ceros
    print("Padded with zeros: ")
    print(padded_imagen)
 
    padded_imagen[psize: psize + imagen_row, psize: psize + imagen_col] = imagen #Realizar el padding, escribiendo los valores y respetando las correspondientes con el psize
    print("Padded image: ")
    print(padded_imagen)
    
    return padded_imagen #Regresa el resultado de la unión de ambos paddings

if __name__ == '__main__':
    imagen = np.array([[1,2,3,4,5,6],
                     [7,8,9,10,11,12],
                     [18,17,16,15,14,13],
                     [19,20,21,22,23,24],
                     [100,90,80,70,0,99]])
    
    psize = 1
    padding(imagen, psize)