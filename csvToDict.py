import csv

with open(r"SampleData.csv", 'r+', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row, file=open("output", "r+"))
    print(f'Header: {reader.fieldnames}', file=open("output", "a"))

import csv
import rhinoscriptsyntax as rs

def CSVlist():
    #prompt the user for a file to import
    filter = "CSV file (*.csv)|*.csv|*.txt|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            z = float(row[2])
            print x, y, z
            rs.AddPoint(x,y,z)

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    CSVlist()
