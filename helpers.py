import re

# FIRST PART
def add_headers_to_set(headers_set, text, separator):
  headers_set.add(text.split(separator)[0])
  
def prepare_to_csv_export(file_path, separator=',') :
  with open(file_path, 'r', encoding="utf-8") as file:
    lexical_db_delimiter = '\\lx'
    entry_string = ''
    gross_headers = set()

    for line in file.readlines():
      #TODO if separator is not comma, replace spaces for commas (not sure if every space shoid be considered)
      entry_string += line.replace('\n', ',')
      add_headers_to_set(gross_headers, line, separator)
    gross_entries = [lexical_db_delimiter + line for line in entry_string.split(lexical_db_delimiter) if line]

    return (gross_headers, gross_entries)
  
# SECOND PART
def remove_string_empty_key_safely(dictionary):
  return dictionary.pop('', None)

def replace_commas_inside_quotes_safely(text, replacement_code):
  if re.search('("[^",]+),([^"]+")', text):
      strings_in_quotes = re.finditer('("[^",]+),([^"]+")', text)
      for fragment_in_quotes in strings_in_quotes:        
        temporal_replacement = fragment_in_quotes[0].replace(',', replacement_code)
        text = text.replace(fragment_in_quotes[0], temporal_replacement)
  return text

def remove_extra_commas(entry):
  full_entries_with_extra_commas_regex = '\\\\([^,])+,[^,\n]+(,,+)'
  match_more_than_two_commas_regex = '(,{2}),+'
  cleaned_entry = re.sub(match_more_than_two_commas_regex, ',,', entry)
  if re.search(full_entries_with_extra_commas_regex, cleaned_entry):
    replacements = re.finditer(full_entries_with_extra_commas_regex, cleaned_entry)
    for replacement in replacements:
      temporal_replacement = replacement[0].replace(replacement[0], replacement[0][:-1])
      cleaned_entry = cleaned_entry.replace(replacement[0], temporal_replacement)
  return cleaned_entry