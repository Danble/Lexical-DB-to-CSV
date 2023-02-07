import csv
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
def clean_headers(headers_set):
  if '\n' in headers_set:
    headers_set.remove('\n')
  return list(headers_set)

def remove_string_empty_key_safely(dictionary):
  return dictionary.pop('', None)

def clean_entries(entries_array):
  #TODO change this variable, maybe using lambdas
  new_array = []
  for entry in entries_array:
    entry = replace_commas_inside_quotes_safely(entry, '&&&')
    entry = remove_extra_commas(entry)
    elements = entry.split(',')
    new_dictionary = {}
    for i in range(0, len(elements), 2):
      new_dictionary[elements[i]] = elements[i+1] if (i < len(elements)-2) else ''
      remove_string_empty_key_safely(new_dictionary)
    new_array.append(new_dictionary)

  return new_array

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
    #TODO fix for multiple linebreaks in different fields (using finditer maybe)
    replacement = re.search(full_entries_with_extra_commas_regex, cleaned_entry)[0]
    cleaned_entry = cleaned_entry.replace(replacement, replacement[:-1])
  return cleaned_entry

def create_csv(file_path, csv_name):
  gross_dictionary_data = prepare_to_csv_export(file_path)
  headers = clean_headers(gross_dictionary_data[0])
  entries = clean_entries(gross_dictionary_data[1])

  with open(csv_name, 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator='\n')
    writer.writeheader()
    writer.writerows(entries)


create_csv('./test_sheet.txt', 'test.csv')