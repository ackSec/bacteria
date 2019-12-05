import csv

with open(r"SampleData.csv", 'r+') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row, file=open("output.txt", "a"))
    print(f'Header: {reader.fieldnames}', file=open("output.txt", "a"))
