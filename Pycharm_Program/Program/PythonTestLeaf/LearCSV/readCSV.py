import csv
#Way1
with open('text.csv') as f:
    data = csv.reader(f)
    print(list(data))
#Way2
with open('text.csv') as a:
    data = csv.reader(a)
    for row in data:
        for col in row:
            print(col)
        print(" ")

#Way3
'''with open('text.csv') as a:
    data = csv.reader(a)
    for row in data:
        print(row[0].ljust(15), row[1].ljust(15), row[2])'''

#way4
with open('text.csv') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row["f_name"].ljust(15),row["l_name"].ljust(15),row["email"])

