import csv
from helpers import *
# CLEANERS
def clean_headers(headers_set):
  if '\n' in headers_set:
    headers_set.remove('\n')
  return list(headers_set)

def clean_entries(entries_array, temporal_comma_replacement):
  #TODO change this variable, maybe using lambdas
  new_array = []
  for entry in entries_array:
    entry = replace_commas_inside_quotes_safely(entry, temporal_comma_replacement)
    entry = remove_extra_commas(entry)
    elements = entry.split(',')
    new_dictionary = {}
    for i in range(0, len(elements), 2):
      if (i < len(elements)-2):
        elements[i+1] = undo_comma_replacement(elements[i+1], temporal_comma_replacement)
        new_dictionary[elements[i]] = elements[i+1]
      remove_string_empty_key_safely(new_dictionary)
    new_array.append(new_dictionary)

  return new_array

# MAIN FUNCTION
def create_csv(file_path, csv_name):
  gross_dictionary_data = prepare_to_csv_export(file_path)
  headers = clean_headers(gross_dictionary_data[0])
  entries = clean_entries(gross_dictionary_data[1], '&&&')

  with open(csv_name, 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator='\n')
    writer.writeheader()
    writer.writerows(entries)


create_csv('./test_sheet.txt', 'test.csv')