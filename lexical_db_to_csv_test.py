from lexical_db_to_csv import *

def test_add_headers_to_set():
  new_set = set()
  add_headers_to_set(new_set, '\\ph,testing', ',')
  assert new_set == {'\\ph'}


def test_prepare_to_csv_export():
  myTuple = prepare_to_csv_export('./test_sheet.csv')
  assert myTuple == (
    {
      '\\tlp', '\\ps', '\\pl', '\\n',
      '\\ph', '\\ge', '\\ph2', '\n',
      '\\gn', '\\lx', '\\nc', '\\b',
      '\\tl', '\\re', '\\dt'
    }, 
    [
      '\\lx,,\\ph,,\\tl,,\\pl,,\\ph2,,\\tlp,,\\ps,n,\\nc,,\\n,1157,\\ge,pelican,\\re,pelican,\\gn,pelican,\\dt,17/Sep/2003,,',
      '\\lx,,\\ph,,\\tl,,\\pl,,\\ps,v,\\n,1181,\\ge,soar,\\re,soar,\\gn,planer,\\dt,14/Sep/2003,,',
      '\\lx,ïìtok,\\ph,it\x8dk,\\tl,L [H,\\pl,toktuè,\\ph2,t\x8dktu,\\tlp,H] L,\\b,,\\ps,n,\\nc,5/13,\\n,1404,\\ge,"brook, stream",\\re,brook ; stream,\\gn,ruisseau,\\dt,24/Jan/2005,,',
      '\\lx,itoènwanïì,\\ph,it\x8dNwani,\\tl,H [L] H L,\\pl,,\\ph2,,\\tlp,,\\ps,n,\\nc,,\\n,44,\\ge,umbilical cord,\\re,umbilical cord,\\gn,cordon ombilical,\\dt,11/Jan/2005,,',
      '\\lx,soñileki,\\ph,s\x8dNilEki,\\tl,H H] H H,\\pl,soñtulektu,\\ph2,s\x8dNtulEktu,\\tlp,,\\ps,n,\\nc,?/?,\\n,23,\\ge,molar tooth,\\re,molar tooth,\\gn,molaire,\\dt,12/Jan/2005'
    ]
  )

def test_clean_headers():
  cleaned_headers = clean_headers({
                      '\\tlp', '\\ps', '\\pl', '\\n', '\\ph', '\\ge', '\\ph2', '\n', 
                      '\\gn', '\\lx', '\\nc', '\\b', '\\tl', '\\re', '\\dt'
                    },)
  assert cleaned_headers == clean_headers({
                      '\\tlp', '\\ps', '\\pl', '\\n', '\\ph', '\\ge', '\\ph2', '\n', 
                      '\\gn', '\\lx', '\\nc', '\\b', '\\tl', '\\re', '\\dt'
                    },)

def test_remove_string_empty_key_safely():
  new_dictionary = {1: '1', '': '2', 2: '3'}
  remove_string_empty_key_safely(new_dictionary)
  cleaned_dictionary = new_dictionary
  remove_string_empty_key_safely(cleaned_dictionary)
  assert new_dictionary == {1: '1', 2: '3'}
  assert cleaned_dictionary == {1: '1', 2: '3'}

def test_clean_entries():
  new_array = clean_entries([
      '\\lx,ïìtok,\\ph,it\x8dk,\\tl,L [H,\\pl,toktuè,\\ph2,t\x8dktu,\\tlp,H] L,\\b,,\\ps,n,\\nc,5/13,\\n,1404,\\ge,"brook, stream",\\re,brook ; stream,\\gn,ruisseau,\\dt,24/Jan/2005,,'
  ])
  assert new_array == [{
      '\\lx': 'ïìtok',
      '\\ph': 'it\x8dk',
      '\\tl': 'L [H',
      '\\pl': 'toktuè',
      '\\ph2': 't\x8dktu',
      '\\tlp': 'H] L',
      '\\b': '',
      '\\ps': 'n',
      '\\nc': '5/13',
      '\\n': '1404',
      '\\ge': '"brook&&& stream"',
      '\\re': 'brook ; stream',
      '\\gn': 'ruisseau',
      '\\dt': '24/Jan/2005'
  }]

def test_replace_commas_inside_quotes_safely():
  text = replace_commas_inside_quotes_safely('"just, a, comma" , "change my , for an *"', '*')
  assert text == '"just* a* comma" , "change my * for an *"'

def test_remove_extra_commas():
  cleaned_entry = remove_extra_commas('\\lx,test,\\ph,,,,,\\ps')
  assert cleaned_entry == '\\lx,test,\\ph,,\\ps'
  cleaned_entry = remove_extra_commas('\\lx,test,,\\ph,,\\ps')
  assert cleaned_entry == '\\lx,test,\\ph,,\\ps'
  cleaned_entry = remove_extra_commas('\\lx,test,,,,,,,,,,\\ph,,\\ps')
  assert cleaned_entry == '\\lx,test,\\ph,,\\ps'
  cleaned_entry = remove_extra_commas('\\lx,test,,\\ph,,,\\ps')
  assert cleaned_entry == '\\lx,test,\\ph,,\\ps'
