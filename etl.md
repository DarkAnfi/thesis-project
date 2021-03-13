# Proceso de ETL

Proceso de extracción, transformación y carga de datos

## Directorio de escuelas

Los datos de los directorios probienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://) la cual recibe como parametro un diccionario con los filtros de los nombres de columnas y una lista de la dirección de los archivos de la fuente de datos.

```python
school_frame = loadData(School.field_filter, School.file_names, delimiter=';', encoding='latin1')
```

La configuración de carga de datos de escuelas se encuentra en la clase [School](https://).

### Transformación de los datos

Dado que se necesitan los datos de los estudiantes de 4° básico, las escuelas deben de ser filtradas por aquellas que tengan enseñansa básica mediante las variables 'ens'.

```python
school_frame = school_frame[
    (school_frame['ens01'] == 110) |
    (school_frame['ens02'] == 110) |
    (school_frame['ens03'] == 110) |
    (school_frame['ens04'] == 110) |
    (school_frame['ens05'] == 110) |
    (school_frame['ens06'] == 110) |
    (school_frame['ens07'] == 110) |
    (school_frame['ens08'] == 110) |
    (school_frame['ens09'] == 110) |
    (school_frame['ens10'] == 110) |
    (school_frame['ens11'] == 110) |
    (school_frame['ens12'] == 110)
]
```

Habiendo variables nominales como 'dependence' y 'religion' y variables ordinales como 'annualpayment' y 'monthlypayment' es que es necesario realizar [one-hot encoding](https://) e [int enconding](https://) respectivamente.

```python
school_frame = onehotEncoding(school_frame, 'dependence', School.dependence)
school_frame = onehotEncoding(school_frame, 'religion', School.religion)

school_frame = intEncoding(school_frame, 'annualpayment', School.payment)
school_frame = intEncoding(school_frame, 'monthlypayment', School.payment)
```

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
school_frame = school_frame[School.fields]
school_frame = school_frame.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://) para procesarlos más tarde.

```python
saveData(school_frame, 'school.csv')
```

## Alumnos matriculados

Los datos de los alumnos matriculados probienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://).

```python
enrolled_frame = loadData(Enrolled.field_filter, Enrolled.file_names, delimiter=';', encoding='latin1')
```

La configuración de carga de datos de alumnos matriculados se encuentra en la clase [Enrolled](https://).

### Transformación de los datos

Se necesitan las matriculas de los estudiantes de 4° básico, las cuales se obtienen de filtrar por las variables 'ens' y 'grade'.

```python
enrolled_frame = enrolled_frame[enrolled_frame['ens'] == 110]
enrolled_frame = enrolled_frame[enrolled_frame['grade'] == 4]
```

La variable 'gender' es nominal por lo que se codifica mediante [one-hot encoding](https://).

```python
enrolled_frame = onehotEncoding(enrolled_frame, 'gender', Enrolled.gender)
```

Se realiza una agregación de las variables 'male', 'female' y 'enrolled' mediante la función de suma aprovechando las propiedades del [one-hot encoding](https://).

```python
enrolled_frame['matriculados'] = 1
a = {
    'male': 'sum',
    'female': 'sum',
    'enrolled': 'sum',
}
enrolled_frame = enrolled_frame.groupby(by=['year', 'rbd'], as_index=False).agg(a)
```

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'year' y 'rbd'.

```python
enrolled_frame = enrolled_frame[Enrolled.fields]
enrolled_frame = enrolled_frame.sort_values(['year', 'rbd'], ignore_index=True)
```

### Carga de los datos

Se cargan los datos en un archivo .csv con la función [saveData](https://) para procesarlos más tarde.

```python
saveData(enrolled_frame, 'enrolled.csv')
```
