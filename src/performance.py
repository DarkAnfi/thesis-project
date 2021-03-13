class Performance:
  
  field_filter = {
      'year': ['\xef\xbb\xbfagno', 'agno', '\xef\xbb\xbfAGNO'],
      'rbd': ['rbd', 'RBD'],
      'ens': ['cod_ense', 'COD_ENSE'],
      'grade': ['cod_grado', 'COD_GRADO'],
      'mark': ['prom_gral', 'PROM_GRAL'],
      'attendance': ['asistencia', 'ASISTENCIA'],
  }
  
  fields = [
      'year',
      'rbd',
      'mark',
      'attendance'
  ]
  
  file_names = [
      join('.', 'source', 'rendimiento_2016.csv'),
      join('.', 'source', 'rendimiento_2017.csv'),
      join('.', 'source', 'rendimiento_2018.csv'),
  ]
