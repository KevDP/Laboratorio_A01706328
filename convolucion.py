# convolucion.py
# Kevin Joan Delgado Pérez A01706328
# Versión 2: Usadas nuevas coordenadas (output_x,output_y) para delimitar mejor las casillas de salida
# Herramientas computacionales: El arte de la programación

import numpy as np

def suma_matrices(matriz,kernel):
    """multiplicar la matriz cortada y la de kernel para devolver la suma"""

    m_row, m_col = matriz.shape                       #asignar el tamaño de la matriz (en filas y columnas)
    k_row, k_col = kernel.shape                       #asignar el tamaño del kernel (en filas y columnas)
    resultado = 0.0                                   #instanciar la resultante en ceros

    for row in range (m_row):                                #recorrer filas de la matriz
        for col in range (m_col):                            #recorrer columnas de la matriz
            resultado+= matriz[row,col] * kernel[row,col]       #acumular el resultado de cada una de las multiplicaciones entre las filas y columnas de la matriz y el kernel
    return resultado                                         #devolver resultante

def convolucion(imagen,kernel):
    """Aplica una convolucion sin padding (válida) con una dimension y para devolver una resultante"""

    imagen_row, imagen_col = imagen.shape #asignar el alto y ancho de la imagen
    kernel_row, kernel_col = kernel.shape #asignar el alto y ancho del filtro
    
    output_x = (imagen_col - (kernel_col / 2) * 2) + 1 #asigna el ancho del output
    output_y = (imagen_row - (kernel_row / 2) * 2) + 1 #asigna el alto del output
    
    output_x_int = int (output_x) #cambiar los valores a enteros
    output_y_int = int (output_y) #cambiar los valores a enteros
   
    salida = np.zeros([output_y_int, output_x_int]) #matriz donde se guardan las resultantes de las coordenadas
   
    for row in range(output_y_int): #recorrer las filas de la imagen
        for col in range(output_x_int): #recorrer las columnas de la imagen
                salida[row,col] = suma_matrices( 
                                    imagen[row:row + kernel_row, 
                                    col:col + kernel_col],kernel) #relizar la suma entre las filas de la matriz con la del kernel y lo mismo con las columnas
             

    return salida                              #obtener la salida con todas las resultantes

if __name__ == '__main__':
    imagen = np.array([[1,2,3,4,5,6],
             [7,8,9,10,11,12],
             [0,0,1,16,17,18],
             [0,1,0,7,23,24],
             [1,7,6,5,4,3]])
    
    imagen2 = np.array([[10,4,50,30,20],
             [80,0,0,0,6],
             [0,0,1,16,17],
             [0,1,0,7,23],
             [1,0,6,0,4]])
    
    kernel = np.array([[1,1,1],
              [0,0,0],
              [2,10,3]])
    
    kernel2 = np.array([[1,0,1],
              [0,0,0],
              [1,0,3]]) 
    
    print(convolucion(imagen,kernel))
    print("\n")
    print(convolucion(imagen2,kernel2))