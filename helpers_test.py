from helpers import *

def test_add_headers_to_set():
  new_set = set()
  add_headers_to_set(new_set, '\\ph,testing', ',')
  assert new_set == {'\\ph'}

def test_remove_string_empty_key_safely():
  new_dictionary = {1: '1', '': '2', 2: '3'}
  remove_string_empty_key_safely(new_dictionary)
  cleaned_dictionary = new_dictionary
  remove_string_empty_key_safely(cleaned_dictionary)
  assert new_dictionary == {1: '1', 2: '3'}
  assert cleaned_dictionary == {1: '1', 2: '3'}

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
  cleaned_entry = remove_extra_commas('\\lx,test,,\\ph,tɛst,,\\ps')
  assert cleaned_entry == '\\lx,test,\\ph,tɛst,\\ps'
  cleaned_entry = remove_extra_commas('\\lx,test,,,\\ph,tɛst,,,\\ps')
  assert cleaned_entry == '\\lx,test,\\ph,tɛst,\\ps'

def test_undo_comma_replacement():
  cleaned_text = undo_comma_replacement('"brook&&& stream&&&* water"', '&&&')
  assert cleaned_text == '"brook, stream,* water"'

def test_turn_entry_into_dictionary():
  dictionary = turn_entry_into_dictionary(['\\lx', 'Arroyo', '\\ge', '"brook&&& stream"', '\\dt', '24/Jan/2023'], '&&&')
  assert dictionary == {'\\ge': '"brook, stream"', '\\lx': 'Arroyo', '\\dt': '24/Jan/2023'}