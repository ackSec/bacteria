import csv

with open(r"", 'r+') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row)
    print(f'Header: {reader.fieldnames}')
