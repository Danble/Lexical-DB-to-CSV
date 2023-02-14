import re

# FIRST PART
def add_headers_to_set(headers_set, text, separator):
  headers_set.add(text.split(separator)[0])
  
# SECOND PART
def remove_string_empty_key_safely(dictionary):
  return dictionary.pop('', None)

def replace_commas_inside_quotes_safely(text, replacement_code):
  commas_between_quotes_regex = '("[^",]+),([^"]+")'
  text = replace_multiple_text_fragments(text, commas_between_quotes_regex, replacement_code, ',')
  return text

def remove_extra_commas(entry):
  full_entries_with_extra_commas_regex = '\\\\([^,])+,[^,\n]+(,,+)'
  match_more_than_two_commas_regex = '(,{2}),+'
  cleaned_entry = re.sub(match_more_than_two_commas_regex, ',,', entry)
  cleaned_entry = replace_multiple_text_fragments(cleaned_entry, full_entries_with_extra_commas_regex)
  return cleaned_entry

def undo_comma_replacement(text, temporal_character_replacement):
  match_temporal_character_inisde_quotes_regex = r'("[^",]+)' + temporal_character_replacement + r'([^"]+")'
  text = replace_multiple_text_fragments(text, match_temporal_character_inisde_quotes_regex, ',', temporal_character_replacement)
  return text

def turn_entry_into_dictionary(elements, temporal_replacement):
  #TODO before adding elements into dictionaries, we need to save the targeted header duplicates and also add them to the headers set
  new_dictionary = {}
  for i in range(0, len(elements), 2):
    if (i < len(elements)-1):
      elements[i+1] = undo_comma_replacement(elements[i+1], temporal_replacement)
      new_dictionary[elements[i]] = elements[i+1]
    remove_string_empty_key_safely(new_dictionary)
  return new_dictionary

def replace_multiple_text_fragments(text, regex, replacement=None, fragment_to_replace=None):
  if re.search(regex, text):
    fragments = re.finditer(regex, text)
    for fragment in fragments:
      if fragment_to_replace and replacement:
        temporal_replacement = fragment[0].replace(fragment_to_replace, replacement)
      elif fragment_to_replace:
        temporal_replacement = fragment[0].replace(fragment_to_replace, fragment[0][:-1])
      elif replacement:
        temporal_replacement = fragment[0].replace(fragment[0], replacement)
      else:
        temporal_replacement = fragment[0].replace(fragment[0], fragment[0][:-1])
      text = text.replace(fragment[0], temporal_replacement)
  return text

#TODO
def find_duplicate_headers_in_array(elements, target_header):
  pass

def allow_duplicates(entry_list, headers_targeted):
  counter = 0
  def my_fn(el):
      if el in headers_targeted:
          counter =+ 1
          return el + str(counter)
      else: return el
  filtered = map(my_fn, entry_list)
  return list(filtered)

# my_set = {'\\ge', '\\xv'}
# my_list = ['\\lx', 'Arroyo', '\\ge', 'brook', '\\xv', '', '\\ge', 'stream', '\\xv', 'the stream flows']

# class Test:
#     def __init__(self, search_set):
#         self.element_counter = {key: 0 for key in search_set}
        
#     def number_duplicates(self, my_list, my_set):
#         for i in range(len(my_list)):
#             if my_list[i] in my_set:
#                 self.element_counter[my_list[i]] += 1
#                 my_list[i] = my_list[i] + str(self.element_counter[my_list[i]])
                
# my_test = Test(my_set)
# my_test.number_duplicates(my_list, my_set)
# print(my_test.element_counter)
# print(my_list)
