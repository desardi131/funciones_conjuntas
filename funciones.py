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