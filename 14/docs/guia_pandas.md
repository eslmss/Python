# Guía Pandas

### install

- Comando terminal
    ```
    pip install pandas
    ```

### import
```
import pandas as pd
```

### Create Dataframe

```
df = pd.DataFrame(data, columns=['columna1', 'columna2', 'columna3'])
```

### Leer archivo CSV

```
df = pd.read_csv('archivo.csv')
```

### Operaciones básicas

```
df.head()        # Muestra las primeras filas del DataFrame
df.tail()        # Muestra las últimas filas del DataFrame
df.shape         # Retorna las dimensiones del DataFrame (filas, columnas)
df.info()        # Resumen de información del DataFrame
df.describe()    # Estadísticas descriptivas del DataFrame
```

### Selección de datos
```
df['columna']              # Acceder a una columna por su nombre
df[['columna1', 'columna2']]  # Acceder a varias columnas
df.loc[filas, columnas]    # Acceder a datos por etiquetas de filas y columnas
df.iloc[filas, columnas]   # Acceder a datos por índices de filas y columnas
df.query('condición')      # Filtrar filas basado en una condición
```

### Manipulación de datos
```
df.dropna()         # Eliminar filas con valores nulos
df.fillna(valor)   # Rellenar valores nulos con un valor específico
df.drop(columnas, axis=1)  # Eliminar columnas específicas
df.rename(columns={'columna': 'nuevo_nombre'})  # Renombrar columnas
df.sort_values('columna')   # Ordenar el DataFrame por una columna
```

### Agregación de datos
```
df.groupby('columna').mean()     # Calcular el promedio por grupos
df.groupby('columna').sum()      # Calcular la suma por grupos
df.groupby('columna').count()    # Contar elementos por grupos
df.pivot_table(index='columna1', columns='columna2', values='valor')  # Tabla dinámica
```

### Operaciones avanzadas
```
df.apply(función)             # Aplicar una función a lo largo de un eje
df.merge(df2, on='columna')   # Combinar DataFrames por una columna en común
df.join(df2, on='columna')    # Unir DataFrames en base a un índice o columna
df.melt(id_vars=['columna1'], value_vars=['columna2', 'columna3'])  # Despivoteo
```

### Visualización de datos
```
df.plot()                 # Graficar el DataFrame
df['columna'].plot()     # Graficar una columna específica
df.plot(kind='bar')      # Graficar un gráfico de barras
df.plot(kind='hist')     # Graficar un histograma
```