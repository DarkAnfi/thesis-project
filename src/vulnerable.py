class Vulnerable:
  
  field_filter = {
      'year': ['\xef\xbb\xbfAGNO'],
      'rbd': ['RBD'],
      'ens': ['COD_ENSE'],
      'grade': ['COD_GRADO'],
      'priority': ['PRIORITARIO_ALU'],
      'preferential': ['PREFERENTE_ALU'],
      'beneficiary': ['BEN_SEP'],
  }
  fields = [
      'rbd',
      'rbd',
      'priority',
      'preferential',
      'beneficiary',
      'vulnerable',
  ]

  file_names = [
      join('.', 'source', 'alumnos_2016.csv'),
      join('.', 'source', 'alumnos_2017.csv'),
      join('.', 'source', 'alumnos_2018.csv'),
  ]
