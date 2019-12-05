import csv
import statistics


def CSVbuilding():
    #prompt the user for a file to import
    #filter = "CSV file (*.csv)|*.csv|*.txt|All Files (*.*)|*.*||"
    #filename = rs.OpenFileName("Open Point File", filter)
    #if not filename: return

    with open('SampleData2.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
#            print(row['set1IT043'])
#           print(row)
            data = row['set1IT042']
            statistics.mean(new_l)


            #if row['Use'] == 'Retail':
            print(data)

if( __name__ == "__main__" ):
    CSVbuilding()
