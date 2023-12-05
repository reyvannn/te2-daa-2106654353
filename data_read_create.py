import random
import sys
import json

def print_to_json(values, weights, capacity, file_name):
    data = {
        'Values': values,
        'Weights': weights,
        'Capacity': capacity
    }
    with open(f'{file_name}.json', 'w') as f:
        json.dump(data, f)

def create(count, file_name):
    values = [0] * count
    weights = [0] * count
    capacity = random.randint(100, 1000)
    for i in range(count):
        values[i] = random.randint(0, capacity)
        weights[i] = random.randint(1, capacity)
    print_to_json(values, weights, capacity, file_name)

def read(file_name):
    with open(f'{file_name}.json') as f:
        data = json.load(f)
    return data['Values'], data['Weights'], data['Capacity']