from os.path import join

class Simce:
  
  field_filter = {
      'year': ['agno', '"agno"'],
      'rbd': ['rbd', '"rbd"'],
      'langmark': ['prom_lect4b_rbd'],
      'mathmark': ['prom_mate4b_rbd'],
  }
  
  fields = [
      'year',
      'rbd',
      'langmark',
      'mathmark',
      'langlevel',
      'mathlevel',
  ]

  file_names = [
      join('.', 'source', 'simce_2016.csv'),
      join('.', 'source', 'simce_2017.csv'),
      join('.', 'source', 'simce_2018.csv'),
  ]
