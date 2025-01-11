# TODO решите задачу
import json
def task(file_path: str = "input.json") -> float:
    with open(file_path, 'r') as file:
        data = json.load(file)

    total_sum = sum(entry['score'] * entry['weight'] for entry in data)
    return round(total_sum, 3)
print(task())
