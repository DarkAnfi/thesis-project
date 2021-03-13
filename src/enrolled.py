class Enrolled:
  
  field_filter = {
      'year': ['\xef\xbb\xbfagno', 'agno', '\xef\xbb\xbfAGNO'],
      'rbd': ['rbd', 'RBD'],
      'ens': ['cod_ense', 'COD_ENSE'],
      'grade': ['cod_grado', 'COD_GRADO'],
      'gender': ['gen_alu', 'GEN_ALU']
  }
  
  fields = [
      'year',
      'rbd',
      'male',
      'female',
      'enrolled'
  ]
  
  gender = {
      'male': [1],
      'female': [2],
  }
  
  file_names = [
      join('.', 'source', 'matriculas_2016.csv'),
      join('.', 'source', 'matriculas_2017.csv'),
      join('.', 'source', 'matriculas_2018.csv'),
  ]
