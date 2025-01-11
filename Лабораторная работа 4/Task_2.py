# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def csv_to_json(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
def task() -> None:
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
