import csv
from helpers import *
from tracker import Tracker

# tracking_headers

# FIRST PART
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

def clean_entries(entries_array, temporal_comma_replacement):
  dictionary_array = []
  for entry in entries_array:
    entry = replace_commas_inside_quotes_safely(entry, temporal_comma_replacement)
    entry = remove_extra_commas(entry)
    elements = entry.split(',')
    #TODO before adding elements into dictionaries, we need to save the targeted header duplicates and also add them to the headers set
    dictionary_array.append(turn_entry_into_dictionary(elements, temporal_comma_replacement))
  return dictionary_array

#TODO create test
def export_to_csv(fieldnames, data, csv_name):
  with open(csv_name, 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames, lineterminator='\n')
    writer.writeheader()
    writer.writerows(data)

# MAIN FUNCTION
def create_csv(file_path, csv_name):
  gross_dictionary_data = prepare_to_csv_export(file_path)
  headers = clean_headers(gross_dictionary_data[0])
  entries = clean_entries(gross_dictionary_data[1], '&&&')
  export_to_csv(headers, entries, csv_name)
  

create_csv('./test_sheet.csv', 'test_result_improved.csv')