from lexical_db_to_csv import *

def test_add_headers_to_set():
  new_set = set()
  add_headers_to_set(new_set, '\\ph,testing', ',')
  assert new_set == {'\\ph'}


def test_prepare_to_csv_export():
  myTuple = prepare_to_csv_export('./test_sheet.csv')
  assert myTuple == (
    {
      '\\lx', '\\dt',
      '\\extra_header', '\\ph', 'ph',
      '\\ps', '\n'
    }, 
    [
      '\\lx,test,\\ph,,\\ps,n,\\dt,17/Sep/2022,,',
      '\\lx,test2,\\ph,tɛst tuː,\\ps,n,\\dt,06/Feb/2023,,',
      '\\lx,test3,ph,,\\ps,,\\extra_header,,\\dt,07/Feb/2023'
    ]
  )

def test_clean_headers():
  cleaned_headers = clean_headers({
                      '\\ps', '\\ph', '\n', 
                    },)
  assert cleaned_headers == clean_headers({
                      '\\ps', '\\ph',
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
      '\\lx,Arroyo,\\ph,,,\\ge,"brook, stream",\\re,brook ; stream,,\\dt,24/Jan/2023,,'
  ])
  assert new_array == [{
      '\\lx': 'Arroyo',
      '\\ph': '',
      '\\ge': '"brook&&& stream"',
      '\\re': 'brook ; stream',
      '\\dt': '24/Jan/2023'
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
