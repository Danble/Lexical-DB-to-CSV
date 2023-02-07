import re

# FIRST PART
def add_headers_to_set(headers_set, text, separator):
  headers_set.add(text.split(separator)[0])
  
# SECOND PART
def remove_string_empty_key_safely(dictionary):
  return dictionary.pop('', None)

def replace_commas_inside_quotes_safely(text, replacement_code):
  match_commas_inisde_quotes_regex = '("[^",]+),([^"]+")'
  text = replace_multiple_text_fragments(text, match_commas_inisde_quotes_regex, replacement_code, ',')
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

#TODO create test
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
