# Proceso de ETL

Proceso de extracción, transformación y carga de datos

## Directorio de escuelas

Los datos de los directorios provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://github.com/DarkAnfi/thesis-project/blob/main/src/load_data.py) la cual recibe como parametro un diccionario con los filtros de los nombres de columnas y una lista de la dirección de los archivos de la fuente de datos.

```python
df1 = loadData(School.field_filter, School.file_names, delimiter=';', encoding='latin1')
```

Se cargaron un total de 48.058 registros de escuelas.

La configuración de carga de datos de escuelas se encuentra en la clase [School](https://github.com/DarkAnfi/thesis-project/blob/main/src/school.py).

### Transformación de los datos

Dado que se necesitan los datos de los estudiantes de 4° básico, las escuelas deben de ser filtradas por aquellas que tengan enseñansa básica mediante las variables 'ens'.

```python
df1 = df1[
    (df1['ens01'] == 110) |
    (df1['ens02'] == 110) |
    (df1['ens03'] == 110) |
    (df1['ens04'] == 110) |
    (df1['ens05'] == 110) |
    (df1['ens06'] == 110) |
    (df1['ens07'] == 110) |
    (df1['ens08'] == 110) |
    (df1['ens09'] == 110) |
    (df1['ens10'] == 110) |
    (df1['ens11'] == 110) |
    (df1['ens12'] == 110)
]
```

Se filtran 24.816 registros de los 48.058 originales.

Habiendo variables nominales como 'dependence' y 'religion' y variables ordinales como 'annualpayment' y 'monthlypayment' es que es necesario realizar [one-hot encoding](https://github.com/DarkAnfi/thesis-project/blob/main/src/onehot_encoding.py) e [int enconding](https://github.com/DarkAnfi/thesis-project/blob/main/src/int_encoding.py) respectivamente.

```python
df1 = onehotEncoding(df1, 'dependence', School.dependence)
df1 = onehotEncoding(df1, 'religion', School.religion)

df1 = intEncoding(df1, 'annualpayment', School.payment)
df1 = intEncoding(df1, 'monthlypayment', School.payment)
```

Se codifican 3.918 datos a dependence0, 16.252 datos a dependence1, 22.747 datos a dependence2, 4.679 datos a dependence3, 210 datos a dependence4, 252 datos a dependence5, 19.757 datos a religion0, 12.156 datos a religion1, 1.721 datos a religion2, 1 dato a religion3, 10 datos a religion4, 0 datos a religion5, 3.186 datos a religion6, 10.605 datos 0 a annualpayment, 33.081 datos 1 a annualpayment, 2.347 datos 2 a annualpayment, 170 datos 3 a annualpayment, 252 datos 4 a annualpayment, 306 datos 5 a annualpayment, 1.297 datos 6 a annualpayment, 10.893 datos 0 a monthlypayment, 30.408 datos 1 a monthlypayment, 544 datos 2 a monthlypayment, 1.379 datos 3 a monthlypayment, 1.974 datos 4 a monthlypayment, 1.451 datos 5 a monthlypayment y 1.409 datos 6 a monthlypayment.

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df1 = df1[School.fields]
df1 = df1.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://github.com/DarkAnfi/thesis-project/blob/main/src/save_data.py) para procesarlos más tarde.

```python
saveData(df1, './dataset/school.csv')
```

## Alumnos matriculados

Los datos de los alumnos matriculados provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://github.com/DarkAnfi/thesis-project/blob/main/src/load_data.py).

```python
df2 = loadData(Enrolled.field_filter, Enrolled.file_names, delimiter=';', encoding='latin1')
```

Se cargaron 10.691.791 registros en total.

La configuración de carga de datos de alumnos matriculados se encuentra en la clase [Enrolled](https://github.com/DarkAnfi/thesis-project/blob/main/src/enrolled.py).

### Transformación de los datos

Se necesitan las matriculas de los estudiantes de 4° básico, las cuales se obtienen de filtrar por las variables 'ens' y 'grade'.

```python
df2 = df2[df2['ens'] == 110]
df2 = df2[df2['grade'] == 4]
```

Se filtran un total de 731.976 registros de los 10.691.791 originales.

La variable 'gender' es nominal por lo que se codifica mediante [one-hot encoding](https://github.com/DarkAnfi/thesis-project/blob/main/src/onehot_encoding.py).

```python
df2 = onehotEncoding(df2, 'gender', Enrolled.gender)
```

Se codifican 374.113 datos de gender en male y 357.862 datos de gender en female.

Se realiza una agregación de las variables 'male', 'female' y 'enrolled' mediante la función de suma aprovechando las propiedades del [one-hot encoding](https://github.com/DarkAnfi/thesis-project/blob/main/src/onehot_encoding.py).

```python
df2['enrolled'] = 1
a = {
    'male': 'sum',
    'female': 'sum',
    'enrolled': 'sum',
}
df2 = df2.groupby(by=['year', 'rbd'], as_index=False).agg(a)
```

Los datos quedan agrupados en un total de 22.325 escuelas.

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df2 = df2[Enrolled.fields]
df2 = df2.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://github.com/DarkAnfi/thesis-project/blob/main/src/save_data.py) para procesarlos más tarde.

```python
saveData(df2, './dataset/enrolled.csv')
```

## Rendimiento académico

Los datos del rendimiento académico de los alumnos provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://github.com/DarkAnfi/thesis-project/blob/main/src/load_data.py).

```python
df3 = loadData(Performance.field_filter, Performance.file_names, delimiter=';', encoding='latin1')
```

Se cargan un total de 9.767.517 registros de rendimiento académico.

La configuración de carga de datos del rendimiento académico se encuentra en la clase [Performance](https://github.com/DarkAnfi/thesis-project/blob/main/src/performance.py).

### Transformación de los datos

Se necesita saber el rendimiento académico de los estudiantes de 4° básico, el cual se obtienen al filtrar las variables 'ens' y 'grade'.

```python
df3 = df3[df3['ens'] == 110]
df3 = df3[df3['grade'] == 4]
```

Se filtraron 778.424 registros de los 9.767.517 registros originales

En las fuentes de datos originales la variable promedio general, alojada en la variable 'mark', es una cadena de texto que representa un número flotante separado por 'coma', por lo que se realiza una transformación de esta variable para que pueda ser tratado como un dato flotante como tal.

```python
df3['mark'] = df3['mark'].replace({',':'.'}, regex=True)
df3['mark'] = pd.to_numeric(df3['mark'], downcast='float')
```

Por otro lado la variable promedio anual de asistencia de los estudiantes, alojada en la variable 'attendance' es un número entero que representa el porcentaje de asistencia. Siendo esta variable un porcentaje, es ideal que este mismo este acotado entre 0 y 1.

```python
df3['attendance'] = pd.to_numeric(df3['attendance'], downcast='float')
df3['attendance'] = df3['attendance'] / 100.
```

Se filtran aquellos promedios generales distintos de 0.0.

```python
df3 = df3[df3['mark'] != 0.0]
```

Se filtraron 733.306 registros de los 778.424 registros anteriores

Se realiza una agregación de las variables 'mark' y 'attendance' mediante la función de media.

```python
a = {
    'mark': 'mean',
    'attendance': 'mean',
}
df3 = df3.groupby(by=['year', 'rbd'], as_index=False).agg(a)
```

Los datos quedan agrupados en un total de 22.330 escuelas.

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df3 = df3[Performance.fields]
df3 = df3.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://github.com/DarkAnfi/thesis-project/blob/main/src/save_data.py) para procesarlos más tarde.

```python
saveData(df3, './dataset/performance.csv')
```

## Alumnos vulnerables

Los datos de los alumnos vulnerables provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://github.com/DarkAnfi/thesis-project/blob/main/src/load_data.py).

```python
df4 = loadData(Vulnerable.field_filter, Vulnerable.file_names, delimiter=';', encoding='latin1')
```

Se cargaron 8.902.761 registros.

La configuración de carga de datos de alumnos vulneables se encuentra en la clase [Vulnerable](https://github.com/DarkAnfi/thesis-project/blob/main/src/vulnerable.py).

### Transformación de los datos

Se necesitan los datos de los estudiantes de 4° básico, por lo que se filtran por las variables 'ens' y 'grade'.

```python
df4 = df4[df4['ens'] == 110]
df4 = df4[df4['grade'] == 4]
```

Se filtraron 549.135 registros de los 8.902.761 registros originales.

Se realiza una agregación de las variables 'priority', 'preferential', 'beneficiary' y 'vulnerable' mediante la función de suma.

```python
df4['vulnerable'] = 1
a = {
    'priority': 'sum',
    'preferential': 'sum',
    'beneficiary': 'sum',
    'vulnerable': 'sum',
}
df4 = df4.groupby(by=['year', 'rbd'], as_index=False).agg(a)
```

Los datos quedan agrupados en un total de 21.960 escuelas.

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df4 = df4[Vulnerable.fields]
df4 = df4.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://github.com/DarkAnfi/thesis-project/blob/main/src/save_data.py) para procesarlos más tarde.

```python
saveData(df4, './dataset/vulnerable.csv')
```

## SIMCE

Los datos de los resultados SIMCE provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://github.com/DarkAnfi/thesis-project/blob/main/src/load_data.py).

```python
df5 = loadData(Simce.field_filter, Simce.file_names, sep='[|\t]', encoding='latin1')
```

Se cargaron un total de 22.365 registros.

La configuración de carga de datos de los resultados SIMCE se encuentra en la clase [Simce](https://github.com/DarkAnfi/thesis-project/blob/main/src/simce.py).

### Transformación de los datos

Dado que pueden existir registros invalidos para 'langmark' y 'mathmark' es que se reemplazan por 0.

```python
for field in ['langmark', 'mathmark']:
  df5.loc[df5[field] < 0, field] = 0
```

Hubo 1.470 datos invalidos para 'langmark' y 1.479 datos invalidos para 'mathmark'.

Según los niveles de aprendizaje SIMCE, se categorizan las variables 'langmark' y 'mathmark' en las variables 'langlevel' y 'mathlevel' respectivamente.

```python
df5['langlevel'] = 1
df5.loc[df5['langmark'] < 241, 'langlevel'] = 0
df5.loc[df5['langmark'] >= 284, 'langlevel'] = 2

df5['mathlevel'] = 1
df5.loc[df5['mathmark'] < 245, 'mathlevel'] = 0
df5.loc[df5['mathmark'] >= 295, 'mathlevel'] = 2
```

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df5 = df5[Simce.fields]
df5 = df5.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://github.com/DarkAnfi/thesis-project/blob/main/src/save_data.py) para procesarlos más tarde.

```python
saveData(df5, './dataset/simce.csv')
```

## Dataset final

Los datos provienen de los archivos generados anteriormente.

### Extracción de los datos

Se realiza un merge entre todas las fuentes de datos, agrupadas por 'year' y 'rbd'

```python
df6 = pd.read_csv('./dataset/school.csv')
df6.merge(df6, pd.read_csv('./dataset/enrolled.csv'), how='inner', on=['year', 'rbd'])
df6.merge(df6, pd.read_csv('./dataset/performance.csv'), how='inner', on=['year', 'rbd'])
df6.merge(df6, pd.read_csv('./dataset/vulnerable.csv'), how='inner', on=['year', 'rbd'])
df6.merge(df6, pd.read_csv('./dataset/simce.csv'), how='inner', on=['year', 'rbd'])
```

Se tiene un total de 21.791 registros

### Transformación de los datos

Se calculan los índices de segregación de Rojas (2019) y Alonso-Villar y Del Río (2010).

```python
df6['notvulnerable'] = df6['enrolled'] - df6['vulnerable']
df6['slocal1'] = 0.0
df6['slocal2'] = 0.0
year_list = df6['year'].drop_duplicates()
city_list = df6['city'].drop_duplicates()
for year in year_list:
  for city in city_list:
    E = df6[(df6['year'] == year) & (df6['city'] == city)][['vulnerable', 'notvulnerable']]
    c = np.matrix(E).T
    J = c.shape[1]
    j = np.arange(J)
    t = c.sum(axis=0)
    p = c / t
    C = c.sum(axis=1)
    T = C.sum()
    P = C / T
    if np.any(P == 0):
      df6.loc[E.index, 'slocal1'] = 0.0
      df6.loc[E.index, 'slocal2'] = 0.0
    else:
      a = 0.5
      S1 = np.power(np.e, -p[0, j] / P[0]) - np.power(np.e, -p[1, j] / P[1])
      S2 = 1 - (np.asarray(np.power(p, a)) * np.asarray(np.power(P, (1-a)))).sum(axis=0) 
      df6.loc[E.index, 'slocal1'] = S1.T
      df6.loc[E.index, 'slocal2'] = S2.T * np.asarray(np.power(-1, np.floor(p[0, j] - P[0]) + 1))[0]
```

Se eliminan las variables que no son necesarias para el dataset.

```python
df6 = df6.drop(columns=['year', 'city', 'rbd'])
```

## Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://github.com/DarkAnfi/thesis-project/blob/main/src/save_data.py) para procesarlos más tarde.

```python
saveData(df6, './dataset.csv')
```

\| [Indice](https://darkanfi.github.io/thesis-project) \| [Correlación](https://darkanfi.github.io/thesis-project/correlation) \>
