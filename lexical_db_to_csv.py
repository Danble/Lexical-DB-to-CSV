import csv
from typing import List, Set, Tuple, Dict
from helpers import add_headers_to_set, clean_entry, turn_entry_into_dictionary
from tracker import Tracker


# FIRST PART
def prepare_to_csv_export(file_path: str, separator: str = ',') -> Tuple[Set[str], List[str]]:
    with open(file_path, 'r', encoding="utf-8") as file:
        lexical_db_delimiter = '\\lx'
        entry_string = ''
        gross_headers = set()
        for line in file.readlines():
            # TODO if separator is not comma, replace spaces for commas (not sure if every space should be considered)
            entry_string += line.replace('\n', ',')
            add_headers_to_set(gross_headers, line, separator)
        gross_entries = [lexical_db_delimiter +
                         line for line in entry_string.split(lexical_db_delimiter) if line]
        return (gross_headers, gross_entries)


# SECOND PART
def clean_headers(headers: Set[str]) -> Set[str]:
    if '\n' in headers:
        headers.remove('\n')
    return headers


def create_entry_dictionaries(entries: List[str], temporal_replacement: str) -> List[Dict[str, str]]:
    dictionaries = []
    for entry in entries:
        entry = clean_entry(entry, temporal_replacement)
        dictionary = turn_entry_into_dictionary(entry, temporal_replacement)
        dictionaries.append(dictionary)
    return dictionaries


def export_to_csv(fieldnames: List[str], data: List[Dict[str, str]], csv_name: str) -> None:
    with open(csv_name, 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames, lineterminator='\n')
        writer.writeheader()
        writer.writerows(data)


# MAIN FUNCTION TODO get into its own file
def create_csv(file_path: str, csv_name: str) -> None:
    gross_dictionary_data = prepare_to_csv_export(file_path)
    headers = list(clean_headers(gross_dictionary_data[0]))
    entries = create_entry_dictionaries(gross_dictionary_data[1], '&&&')
    export_to_csv(headers, entries, csv_name)


if __name__ == "__main__":
    create_csv('./test_sheet_2.csv', 'test_result_improved.csv')
