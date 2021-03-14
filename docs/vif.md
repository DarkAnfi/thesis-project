# Factor de inflación de la varianza

Se obtienen los datos del dataset generado mediante [ETL](https://darkanfi.github.io/thesis-project/etl)

```python
df = pd.read_csv('./dataset.csv')
df = df[df['langmark'] != 0]
df = df[df['mathmark'] != 0]
df = df.drop(columns=['langmark', 'mathmark']).reset_index(drop=True)
```

Se realiza una tabla de resumen con los factores de inflación de la varianza

```python
display(pd.DataFrame(
    {
        'Non-Null Count': [f'{n} non-null' for n in data.notnull().sum().values],
        'Dtype': data.dtypes,
        'VIF': [
            variance_inflation_factor(data.values, i)
            for i in range(data.shape[1])
        ],
    },
    data.columns
))
```

|                 | Non-Null Count  | Dtype   | VIF           |
| :-------------- | :-------------: | :-----: | ------------: |
| dependence0     | 19983 non-null  | int64   | 1.452752e+02  |
| dependence1     | 19983 non-null  | int64   | 5.230710e+02  |
| dependence2     | 19983 non-null  | int64   | 5.732778e+02  |
| dependence3     | 19983 non-null  | int64   | 7.298438e+01  |
| dependence4     | 19983 non-null  | int64   | 1.182932e+00  |
| dependence5     | 19983 non-null  | int64   | 1.114469e+01  |
| rural           | 19983 non-null  | int64   | 1.988031e+00  |
| religion0       | 19983 non-null  | int64   | 2.311447e+01  |
| religion1       | 19983 non-null  | int64   | 2.124440e+01  |
| religion2       | 19983 non-null  | int64   | 5.415865e+00  |
| religion3       | 19983 non-null  | int64   | 1.005058e+00  |
| religion4       | 19983 non-null  | int64   | 1.033046e+00  |
| religion5       | 19983 non-null  | int64   | NaN           |
| religion6       | 19983 non-null  | int64   | 7.824093e+00  |
| annualpayment   | 19983 non-null  | int64   | 6.220039e+00  |
| monthlypayment  | 19983 non-null  | int64   | 4.935214e+00  |
| male            | 19983 non-null  | int64   | 6.261608e+06  |
| female          | 19983 non-null  | int64   | 6.385993e+06  |
| enrolled        | 19983 non-null  | int64   | inf           |
| mark            | 19983 non-null  | float64 | 1.335164e+00  |
| attendance      | 19983 non-null  | float64 | 1.298035e+00  |
| priority        | 19983 non-null  | int64   | inf           |
| preferential    | 19983 non-null  | int64   | inf           |
| beneficiary     | 19983 non-null  | int64   | 9.910065e+00  |
| vulnerable      | 19983 non-null  | int64   | inf           |
| langlevel       | 19983 non-null  | int64   | 1.750446e+00  |
| mathlevel       | 19983 non-null  | int64   | 1.783094e+00  |
| notvulnerable   | 19983 non-null  | int64   | inf           |
| slocal1         | 19983 non-null  | float64 | 3.498090e+00  |
| slocal2         | 19983 non-null  | float64 | 3.814333e+00  |
