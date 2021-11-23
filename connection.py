import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'


def export_data(data, fieldnames, file):
    with open(file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def import_data(file):
    data = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new = dict(row)
            data.append(new)
    return data
