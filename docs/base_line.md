# Modelos de línea base

## Fuente de datos

```python
df = pd.read_csv('./dataset.csv')
cs = df.columns.drop([
    'langlevel', 'mathlevel',
    'langmark', 'mathmark',
    'slocal1', 'slocal2',
]).values.tolist()
cs.append(slocal)
cs.append(f'{target}level')
df = df[df[f'{target}mark'] != 0]
df = df.reset_index()[cols]
```

```python
X = df.drop(columns=f'{target}level').values
y = df[[f'{target}level']].values
```

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size   = 0.7,
    random_state = 2021,
    shuffle      = True
)
```

## Regresión Lineal Múltiple con Ordinal Ridge

```python
model = RidgeCV(
    alphas          = np.logspace(-10, 2, 200),
    fit_intercept   = True,
    normalize       = True,
    store_cv_values = True
).fit(X_train, y_train)
model = OrdinalRidge(
    alpha           = model.alpha_,
    fit_intercept   = True,
    normalize       = True
).fit(X_train, y_train)
```

### Reporte de clasificación

```python
y_pred = model.predict(X_train).astype(int)
print(classification_report(y_train, y_pred))
```

<table>
  <thead><th></th><th>langlevel</th><th>mathlevel</th></thead>
  <tbody>
    <tr>
      <td><strong>slocal1</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td>0.62</td>
              <td>0.07</td>
              <td>0.13</td>
              <td>2830</td>
            </tr>
            <tr>
              <td>1</td>
              <td>0.62</td>
              <td>0.95</td>
              <td>0.75</td>
              <td>8266</td>
            </tr>
            <tr>
              <td>2</td>
              <td>0.75</td>
              <td>0.28</td>
              <td>0.41</td>
              <td>2938</td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td>0.63</td>
              <td>14034</td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td>0.66</td>
              <td>0.44</td>
              <td>0.43</td>
              <td>14034</td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td>0.65</td>
              <td>0.63</td>
              <td>0.56</td>
              <td>14034</td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <td><strong>slocal2</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

```python
y_pred = model.predict(X_test).astype(int)
print(classification_report(y_test, y_pred))
```

<table>
  <thead><th></th><th>langlevel</th><th>mathlevel</th></thead>
  <tbody>
    <tr>
      <td><strong>slocal1</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td>0.59</td>
              <td>0.06</td>
              <td>0.10</td>
              <td>1225</td>
            </tr>
            <tr>
              <td>1</td>
              <td>0.61</td>
              <td>0.95</td>
              <td>0.74</td>
              <td>3463</td>
            </tr>
            <tr>
              <td>2</td>
              <td>0.77</td>
              <td>0.28</td>
              <td>0.41</td>
              <td>1327</td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td>0.62</td>
              <td>6015</td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td>0.66</td>
              <td>0.43</td>
              <td>0.42</td>
              <td>6015</td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td>0.64</td>
              <td>0.62</td>
              <td>0.54</td>
              <td>6015</td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <td><strong>slocal2</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

### ROC y AUC

```python
test = (np.dot(X_test, model.coef_.T) + model.intercept_)
pred = pd.get_dummies(y_test.flatten())
sigm = lambda x: 1 / (1 + np.power(np.e, -x))
score = sigm(1 - np.abs(test - np.array([0, 1, 2])))
score = score / score.sum(axis = 1).reshape(-1, 1)
score = pd.DataFrame(score).fillna(0)
```

```python
plt_roc_auc(pred, score, ['Insuficiente','Elemental','Adecuado'])
```

|         | langlevel | mathlevel |
| ------- | --------- | --------- |
| **slocal1** | ![bl1_l1.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl1_l1.png "Linear Regresor ROC") | ![bl1_m1.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl1_m1.png "Linear Regresor ROC") |
| **slocal2** | ![bl1_l2.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl1_l2.png "Linear Regresor ROC") | ![bl1_m2.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl1_m2.png "Linear Regresor ROC") |

## Regresión Logística Multinomial

```python
model = LogisticRegression(
    max_iter=100,
    random_state = 2021
).fit(X_train, y_train)
```

### Reporte de clasificación

```python
y_pred = model.predict(X_train).astype(int)
print(classification_report(y_train, y_pred))
```

<table>
  <thead><th></th><th>langlevel</th><th>mathlevel</th></thead>
  <tbody>
    <tr>
      <td><strong>slocal1</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td>0.46</td>
              <td>0.04</td>
              <td>0.07</td>
              <td>2830</td>
            </tr>
            <tr>
              <td>1</td>
              <td>0.62</td>
              <td>0.95</td>
              <td>0.75</td>
              <td>8266</td>
            </tr>
            <tr>
              <td>2</td>
              <td>0.72</td>
              <td>0.29</td>
              <td>0.41</td>
              <td>2938</td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td>0.63</td>
              <td>14034</td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td>0.60</td>
              <td>0.43</td>
              <td>0.41</td>
              <td>14034</td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td>0.61</td>
              <td>0.63</td>
              <td>0.54</td>
              <td>14034</td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <td><strong>slocal2</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

```python
y_pred = model.predict(X_test).astype(int)
print(classification_report(y_test, y_pred))
```

              precision    recall  f1-score   support

           0       0.44      0.04      0.07      1225
           1       0.61      0.95      0.74      3463
           2       0.72      0.27      0.39      1327

    accuracy                           0.61      6015
   macro avg       0.59      0.42      0.40      6015
weighted avg       0.60      0.61      0.53      6015

<table>
  <thead><th></th><th>langlevel</th><th>mathlevel</th></thead>
  <tbody>
    <tr>
      <td><strong>slocal1</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td>0.44</td>
              <td>0.04</td>
              <td>0.07</td>
              <td>1225</td>
            </tr>
            <tr>
              <td>1</td>
              <td>0.61</td>
              <td>0.95</td>
              <td>0.74</td>
              <td>3463</td>
            </tr>
            <tr>
              <td>2</td>
              <td>0.72</td>
              <td>0.27</td>
              <td>0.39</td>
              <td>1327</td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td>0.61</td>
              <td>6015</td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td>0.59</td>
              <td>0.42</td>
              <td>0.40</td>
              <td>6015</td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td>0.60</td>
              <td>0.61</td>
              <td>0.53</td>
              <td>6015</td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <td><strong>slocal2</strong></td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <table>
          <thead><th></th><th>precision</th><th>recall</th><th>f1-score</th><th>support</th></thead>
          <tbody align="right">
            <tr>
              <td>0</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>accuracy</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>macro avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>weighted avg</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

### ROC y AUC

```python
test = (np.dot(X_test, model.coef_.T) + model.intercept_)
pred = pd.get_dummies(y_test.flatten())
sigm = lambda x: 1 / (1 + np.power(np.e, -x))
score = sigm(1 - np.abs(test - np.array([0, 1, 2])))
score = score / score.sum(axis = 1).reshape(-1, 1)
score = pd.DataFrame(score).fillna(0)
```

```python
plt_roc_auc(pred, score, ['Insuficiente','Elemental','Adecuado'])
```

|         | langlevel | mathlevel |
| ------- | --------- | --------- |
| **slocal1** | ![bl2_l1.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl2_l1.png "Multinomial Logistic Regresor ROC") | ![bl2_m1.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl2_m1.png "Multinomial Logistic Regresor ROC") |
| **slocal2** | ![bl2_l2.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl2_l2.png "Multinomial Logistic Regresor ROC") | ![bl2_m2.png](https://raw.githubusercontent.com/DarkAnfi/thesis-project/main/src/bl2_m2.png "Multinomial Logistic Regresor ROC") |


\< [Factor de inflación de la varianza](https://darkanfi.github.io/thesis-project/vif) \| [Índice](https://darkanfi.github.io/thesis-project) \| [Modelos de aprendizaje profundo](https://darkanfi.github.io/thesis-project/deep_learning) \>
