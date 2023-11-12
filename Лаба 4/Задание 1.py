
# TODO импортировать необходимые молули

import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


# TODO считать содержимое csv файла
def task(csv_file: str, delimiter: str = ',') -> str:
    json_data = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=delimiter)

        for row in reader:
            json_data.append(row)
# TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as output_file:
        json.dump(json_data, output_file, indent=4)
    return json.dumps(json_data, indent=4)

if name == 'main':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")