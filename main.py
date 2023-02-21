from typing import Optional
from lexical_db_to_csv import (
    prepare_to_csv_export,
    clean_headers,
    create_entry_dictionaries,
    export_to_csv
)


def create_csv(file_path: str, csv_name: str, allow_senses: Optional[bool] = False) -> None:
    gross_dictionary_data = prepare_to_csv_export(file_path)
    all_headers = clean_headers(gross_dictionary_data[0])
    entries_with_new_headers = create_entry_dictionaries(
        gross_dictionary_data[1], '&&&', allow_senses)
    entries = entries_with_new_headers[1]
    if allow_senses:
        all_headers = all_headers.union(entries_with_new_headers[0])
    headers = sorted(list(all_headers))
    export_to_csv(headers, entries, csv_name)


if __name__ == "__main__":
    create_csv('./chamorro_example.csv', 'test_result_improved.csv', True)
