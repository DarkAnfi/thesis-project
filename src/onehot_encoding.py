def onehotEncoding(data_frame, field, encoder):
  for key in encoder.keys():
    data_frame[key] = 0
    index = data_frame[field].isin(encoder[key])
    data_frame.loc[index, key] = 1
  return data_frame.drop(columns=[field])
