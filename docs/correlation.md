# Correlación

Se obtienen los datos del dataset generado mediante [ETL](https://darkanfi.github.io/thesis-project/etl)

```python
df = pd.read_csv('./dataset.csv')
df = df[df['langmark'] != 0]
df = df[df['mathmark'] != 0]
df = df.drop(columns=['langmark', 'mathmark']).reset_index()
```

Son 19.983 los registros validos para calcular su matríz de correlación.

```python
corr_matrix = df.select_dtypes(include=['int', 'float']).corr(method='pearson')
```

Se grafica un mapa de calor de la matríz de correlación ordenada por 'langlevel'.

```python
corr_matrix = corr_matrix.sort_values('langlevel')
corr_matrix = corr_matrix[corr_matrix.index]
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
sns.heatmap(
  corr_matrix,
  square = True,
  ax     = ax
)
ax.tick_params()
plt.show()
```

![langmark corr matrix heatmap](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/lang_heatmap.png "Corr matrix heatmap for langmark")

Se grafica un mapa de calor de la matríz de correlación ordenada por 'mathlevel'.

```python
corr_matrix = corr_matrix.sort_values('mathlevel')
corr_matrix = corr_matrix[corr_matrix.index]
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
sns.heatmap(
  corr_matrix,
  square = True,
  ax     = ax
)
ax.tick_params()
plt.show()
```

![mathmark corr matrix heatmap](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/math_heatmap.png "Corr matrix heatmap for mathmark")

\< [Proceso de ETL](https://darkanfi.github.io/thesis-project/etl) \| [Indice](https://darkanfi.github.io/thesis-project) \| [Factor de inflación de la varianza](https://darkanfi.github.io/thesis-project/vif) \>
