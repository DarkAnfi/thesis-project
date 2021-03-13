# Proceso de ETL

Proceso de extracción, transformación y carga de datos

## Directorio de escuelas

Los datos de los directorios provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://) la cual recibe como parametro un diccionario con los filtros de los nombres de columnas y una lista de la dirección de los archivos de la fuente de datos.

```python
df1 = loadData(School.field_filter, School.file_names, delimiter=';', encoding='latin1')
```

La configuración de carga de datos de escuelas se encuentra en la clase [School](https://).

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

Habiendo variables nominales como 'dependence' y 'religion' y variables ordinales como 'annualpayment' y 'monthlypayment' es que es necesario realizar [one-hot encoding](https://) e [int enconding](https://) respectivamente.

```python
df1 = onehotEncoding(df1, 'dependence', School.dependence)
df1 = onehotEncoding(df1, 'religion', School.religion)

df1 = intEncoding(df1, 'annualpayment', School.payment)
df1 = intEncoding(df1, 'monthlypayment', School.payment)
```

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df1 = df1[School.fields]
df1 = df1.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://) para procesarlos más tarde.

```python
saveData(df1, './dataset/school.csv')
```

## Alumnos matriculados

Los datos de los alumnos matriculados provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://).

```python
df2 = loadData(Enrolled.field_filter, Enrolled.file_names, delimiter=';', encoding='latin1')
```

La configuración de carga de datos de alumnos matriculados se encuentra en la clase [Enrolled](https://).

### Transformación de los datos

Se necesitan las matriculas de los estudiantes de 4° básico, las cuales se obtienen de filtrar por las variables 'ens' y 'grade'.

```python
df2 = df2[df2['ens'] == 110]
df2 = df2[df2['grade'] == 4]
```

La variable 'gender' es nominal por lo que se codifica mediante [one-hot encoding](https://).

```python
df2 = onehotEncoding(df2, 'gender', Enrolled.gender)
```

Se realiza una agregación de las variables 'male', 'female' y 'enrolled' mediante la función de suma aprovechando las propiedades del [one-hot encoding](https://).

```python
df2['enrolled'] = 1
a = {
    'male': 'sum',
    'female': 'sum',
    'enrolled': 'sum',
}
df2 = df2.groupby(by=['year', 'rbd'], as_index=False).agg(a)
```

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df2 = df2[Enrolled.fields]
df2 = df2.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://) para procesarlos más tarde.

```python
saveData(df2, './dataset/enrolled.csv')
```

## Rendimiento académico

Los datos del rendimiento académico de los alumnos provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://).

```python
df3 = loadData(Performance.field_filter, Performance.file_names, delimiter=';', encoding='latin1')
```

La configuración de carga de datos del rendimiento académico se encuentra en la clase [Performance](https://).

### Transformación de los datos

Se necesita saber el rendimiento académico de los estudiantes de 4° básico, el cual se obtienen al filtrar las variables 'ens' y 'grade'.

```python
df3 = df3[df3['ens'] == 110]
df3 = df3[df3['grade'] == 4]
```

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

Se realiza una agregación de las variables 'mark' y 'attendance' mediante la función de media.

```python
a = {
    'mark': 'mean',
    'attendance': 'mean',
}
df3 = df3.groupby(by=['year', 'rbd'], as_index=False).agg(a)
```

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df3 = df3[Performance.fields]
df3 = df3.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://) para procesarlos más tarde.

```python
saveData(df3, './dataset/performance.csv')
```

## Alumnos vulnerables

Los datos de los alumnos vulnerables provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://).

```python
df4 = loadData(Vulnerable.field_filter, Vulnerable.file_names, delimiter=';', encoding='latin1')
```

La configuración de carga de datos de alumnos vulneables se encuentra en la clase [Vulnerable](https://).

### Transformación de los datos

Se necesitan los datos de los estudiantes de 4° básico, por lo que se filtran por las variables 'ens' y 'grade'.

```python
df4 = df4[df4['ens'] == 110]
df4 = df4[df4['grade'] == 4]
```

Se realiza una agregación de las variables 'priority', 'preferential', 'beneficiary' y 'vulnerable' mediante la función de suma aprovechando las propiedades del [one-hot encoding](https://).

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

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
df4 = df4[Vulnerable.fields]
df4 = df4.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://) para procesarlos más tarde.

```python
saveData(df4, './dataset/vulnerable.csv')
```

## SIMCE

Los datos de los resultados SIMCE provienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://).

```python
df5 = loadData(Simce.field_filter, Simce.file_names, sep='[|\t]', encoding='latin1')
```

La configuración de carga de datos de los resultados SIMCE se encuentra en la clase [Simce](https://).

### Transformación de los datos

Dado que pueden existir registros invalidos para 'langmark' y 'mathmark' es que se reemplazan por 0.

```python
for field in ['langmark', 'mathmark']:
  df5.loc[df5[field] < 0, field] = 0
```

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

Se cargan los datos en un archivo .csv con la función [saveData](https://) para procesarlos más tarde.

```python
saveData(df5, './dataset/simce.csv')
```

## Dataset final

### Extracción de los datos
```python
df6 = pd.read_csv('./dataset/school.csv')
df6.merge(df6, pd.read_csv('./dataset/enrolled.csv'), how='inner', on=['agno', 'rbd'])
df6.merge(df6, pd.read_csv('./dataset/performance.csv'), how='inner', on=['agno', 'rbd'])
df6.merge(df6, pd.read_csv('./dataset/vulnerable.csv'), how='inner', on=['agno', 'rbd'])
df6.merge(df6, pd.read_csv('./dataset/simce.csv'), how='inner', on=['agno', 'rbd'])
```

### Transformación de los datos

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
    else:
      S1 = np.power(np.e, -p[0, j] / P[0]) - np.power(np.e, -p[1, j] / P[1])
      df6.loc[E.index, 'slocal1'] = S1.T
    a = 0.5
    S2 = 1 - (np.asarray(np.power(p, a)) * np.asarray(np.power(P, (1-a)))).sum(axis=0) 
    df6.loc[E.index, 'slocal2'] = S2.T * np.asarray(np.power(-1, np.floor(p[0, j] - P[0]) + 1))[0]
```

Se eliminan las variables que no son necesarias para el dataset.

```python
df6 = df6.drop(columns=['year', 'city', 'rbd'])
```

## Carga de los datos

```python
saveData(df6, './dataset/dataset.csv')
```
