# Funcion 3: Detección de outliers

def deteccion_outliers(data,features):
    '''
    Ésta función realiza un bucle para pasar por todas las columnas que indiquemos
    y calcula los valores que se encuentran fuera de los limites de los cuantiles 1 y 3,
    mete en una lista los indices de los valores y cuenta cuantas veces se repiten entre todas las columnas.
    Si el indice lo detecta como outlier en mas de dos columnas mete el indice 
    en la lista de outlier del dataframe.

    Precisa de tener numpy instalado

    Args: 
        -data(DataFrame): Base de datos que tiene todas las columnas que queremos revisar

        -features(columnas): Nombre de todas las columnas que contiene el dataframe a revisar,
        se puede introducir data.columns.

    Return:
        devuelve una lista con los indices que estan fuera de los cuantiles 1 y 3 en 
        mas de dos columnas del DataFrame.

    Agradecimientos a:
     Enes Besinci. Enlace a kaggle-->https://www.kaggle.com/enesbeinci
    '''
    import numpy as np
    from collections import Counter
    outlier_indices = []
    
    for c in features:
        # 1st quartile
        Q1 = np.percentile(data[c],25)
        # 3rd quartile
        Q3 = np.percentile(data[c],75)
        # IQR
        IQR = Q3 - Q1
        # Outlier limite
        outlier_limite = IQR * 1.5
        # detect outlier and their indeces
        outlier_list_col = data[(data[c] < Q1 - outlier_limite) | (data[c] > Q3 + outlier_limite)].index
        # store indeces
        outlier_indices.extend(outlier_list_col)
    
    outlier_indices = Counter(outlier_indices)
    multiples_outliers = list(i for i, v in outlier_indices.items() if v > 2)
    
    return multiples_outliers

# Función 1: Lista de listas

def lista_de_listas(lista):
    '''
    La función lista_de_listas crea una lista individual por cada elemento de la lista argumento, 
    pasando asi a una lisa cuyos elementos son listas con un solo elemento

    esto es especialmente util para poder trabajar con strings de varias palabras
    dentro de una lista.

    ejemplo:
        lista = ['estoy programando en python','hola mundo',1234]
        lista_de_listas(lista)
        return [['estoy programando en python'],['hola mundo'],[1234]]

    Args:
        lista: introducir una lista independientemente de los elementos existentes dentro

    Return:
        lista_vacia: una lista de sublistas, cada sublista es un elemento de la lista original.
        
    '''
    lista_vacia = []
    for i in range((len(lista))):
        lista_vacia.append([]) # introduce una lista vacia en lista_vacia por cada vuelta del bucle

    for n,i in enumerate(lista_vacia):
    
        i.append(lista[n]) # en cada valor de lista vacia(i) realiza un append del elemento correspondiente de lista, indicando su indice mediante n

    return lista_vacia