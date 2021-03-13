from os.path import join

class School:
  
  field_filter = {
      'year': ['\xef\xbb\xbfAGNO', 'AGNO', '\xef\xbb\xbf\xc3\xafagno'],
      'city': ['cod_com_rbd', 'COD_COM_RBD'],
      'rbd': ['rbd', 'RBD'],
      'dependence': ['cod_depe', 'COD_DEPE'],
      'rural': ['rural_rbd', 'RURAL_RBD'],
      'religion': ['ori_religiosa', 'ORI_RELIGIOSA'],
      'annualpayment': ['pago_matricula', 'PAGO_MATRICULA'],
      'monthlypayment': ['pago_mensual', 'PAGO_MENSUAL'],
      'ens01': ['ens_01', 'ENS_01'],
      'ens02': ['ens_02', 'ENS_02'],
      'ens03': ['ens_03', 'ENS_03'],
      'ens04': ['ens_04', 'ENS_04'],
      'ens05': ['ens_05', 'ENS_05'],
      'ens06': ['ens_06', 'ENS_06'],
      'ens07': ['ens_07', 'ENS_07'],
      'ens08': ['ens_08', 'ENS_08'],
      'ens09': ['ens_09', 'ENS_09'],
      'ens10': ['ens_10', 'ENS_10'],
      'ens11': ['ens_11', 'ENS_11'],
      'ens12': ['ens_12', 'ENS_12'],
  }
  
  dependence = {
      'dependence0': [1],
      'dependence1': [2],
      'dependence2': [3],
      'dependence3': [4],
      'dependence4': [5],
      'dependence5': [6],
  }
  
  religion = {
      'religion0': [1],
      'religion1': [2],
      'religion2': [3],
      'religion3': [4],
      'religion4': [5],
      'religion5': [6],
      'religion6': [7],
  }
  
  payment = {
      0: [-1, 0, 'SIN INFORMACI\xc3\x83\xc2\x93N', 'Sin informaci\xc3\x83\xc2\xb3n', 'SIN INFORMACION'],
      1: [1, 'Gratuito', 'GRATUITO'],
      2: [2, '$1.000 a $10.000', '$1.000 A $10.000'],
      3: [3, '$10.001 a $25.000', '$10.001 A $25.000'],
      4: [4, '$25.001 a $50.000', '$25.001 A $50.000'],
      5: [5, '$50.001 a $100.000', '$50.001 A $100.000'],
      6: [6, 'M\xc3\x83\xc2\xa1s de $100.000', 'M\xc3\x83\xc2\x81S DE $100.000', 'MAS DE $100.000'],
  }
  
  fields = [
      'year',
      'city',
      'rbd',
      'dependence0', 'dependence1', 'dependence2', 'dependence3', 'dependence4', 'dependence5',
      'rural',
      'religion0', 'religion1', 'religion2', 'religion3', 'religion4', 'religion5', 'religion6',
      'annualpayment',
      'monthlypayment'
  ]
  
  file_names = [
      join('.', 'source', 'directorio_2016.csv'),
      join('.', 'source', 'directorio_2017.csv'),
      join('.', 'source', 'directorio_2018.csv'),
  ]
