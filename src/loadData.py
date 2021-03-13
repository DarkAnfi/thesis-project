import pandas as pd

def loadData(field_filter, file_names, encoding=None, sep=',', delimiter=None, engine='python'):
  df = pd.DataFrame(columns=field_filter.keys())
  for file_name in file_names:
    df = appendFile(df, file_name, field_filter, encoding, sep, delimiter, engine)
  return df

def appendFile(data_frame, file_name, field_filter, encoding, sep, delimiter, engine):
  df = pd.read_csv(file_name, encoding=encoding, sep=sep, delimiter=delimiter, engine=engine, na_values=[' ', '', '.'])
  df_cols = df.columns
  for key in field_filter.keys():
    if key not in df_cols:
      df[key] = -1
    for field in field_filter[key]:
      if field in df_cols:
        df[key] = df[field]
        if(df[key].dtype == 'float64'):
          df[key] = df[key].fillna(-1).astype('int64')
        break
  data_frame = data_frame.append(df[field_filter.keys()], ignore_index=True)
  return data_frame
