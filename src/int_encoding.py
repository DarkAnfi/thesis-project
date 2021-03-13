def intEncoding(data_frame, field, encoder):
  for key in encoder.keys():
    index = data_frame[field].isin(encoder[key])
    data_frame.loc[index, field] = key
  return data_frame
