from helpers import *
#TODO improve tests
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

#TODO break in two loops
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

# def test_turn_entry_into_dictionary():
#   dictionary = turn_entry_into_dictionary(['\\lx', 'Arroyo', '\\ge', '"brook&&& stream"', '\\dt', '24/Jan/2023'], '&&&')
#   assert dictionary == {'\\ge': '"brook, stream"', '\\lx': 'Arroyo', '\\dt': '24/Jan/2023'}
#   dictionary = turn_entry_into_dictionary(['\\lx', 'Arroyo', '\\ge', 'brook', '\\ge', 'stream', '\\dt', '24/Jan/2023'], '')
#   assert dictionary == {'\\lx': 'Arroyo', '\\ge': 'brook', '\\ge2': 'stream', '\\dt': '24/Jan/2023'}

def test_replace_multiple_text_fragments():
  little_tale = 'Once upon a time a "Dino, Dinosaur, Rex" was tired and it says: "this life is awful, terrible and sad"...'
  commas_between_quotes_regex = '("[^",]+),([^"]+")'
  replaced_text = replace_multiple_text_fragments(little_tale, commas_between_quotes_regex, '*', ',')
  assert replaced_text == 'Once upon a time a "Dino* Dinosaur* Rex" was tired and it says: "this life is awful* terrible and sad"...'

# def test_allow_duplicates():
#   duplicates = allow_duplicates(['\\lx', 'Arroyo', '\\ge', 'brook', '\\xv', '', '\\ge', 'stream', '\\xv', 'the stream flows'], {'\\ge', '\\xv'})
#   assert duplicates == ''