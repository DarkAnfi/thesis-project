# Proceso de ETL

Proceso de extracción, transformación y carga de datos

## Directorio de escuelas

Los datos de los directorios probienen de internet

### Extracción de los datos

Se cargan los datos mediante la función [loadData](https://) la cual recibe como parametro un diccionario con los filtros de los nombres de columnas y una lista de la dirección de los archivos de la fuente de datos.

```python
school_frame = loadData(School.field_filter, School.file_names, delimiter=';', encoding='latin1')
```

La configuración de carga de datos de escuelas se encuentra en la clase [School](https://)

### Transformación de los datos

Habiendo variables nominales como 'depe' y 'orireligiosa' y variables ordinales como 'pagomatricula' y 'pagomensual' es que es necesario realizar [one-hot encoding](https://) e [int enconding](https://) respectivamente.

```python
school_frame = onehotEncoding(school_frame, 'depe', Directorio.depe)
school_frame = onehotEncoding(school_frame, 'orireligiosa', Directorio.orireligiosa)

school_frame = intEncoding(school_frame, 'pagomatricula', Directorio.pago)
school_frame = intEncoding(school_frame, 'pagomensual', Directorio.pago)
```

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

Por último se filtran las columnas que van a ser necesarias para el dataset final y se ordenan por las variables 'agno' y 'rbd'.

```python
school_frame = school_frame[School.fields]
school_frame = school_frame.sort_values(['agno', 'rbd'], ignore_index=True)
```
