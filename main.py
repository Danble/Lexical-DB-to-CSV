from lexical_db_to_csv import (
    prepare_to_csv_export,
    clean_headers,
    create_entry_dictionaries,
    export_to_csv
)


def create_csv(file_path: str, csv_name: str) -> None:
    gross_dictionary_data = prepare_to_csv_export(file_path)
    headers = list(clean_headers(gross_dictionary_data[0]))
    entries = create_entry_dictionaries(gross_dictionary_data[1], '&&&')
    export_to_csv(headers, entries, csv_name)


if __name__ == "__main__":
    create_csv('./test_sheet_2.csv', 'test_result_improved.csv')
