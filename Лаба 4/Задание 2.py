# TODO решите задачу

import json

def task(file_name: str) -> float:
    with open(file_name, 'r') as file:
        data = json.load(file)
        total_sum = sum(item['score'] * item['weight'] for item in data)

        return round(total_sum, 3)

print(task('input.json'))

