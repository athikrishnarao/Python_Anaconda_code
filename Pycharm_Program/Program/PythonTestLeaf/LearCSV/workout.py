import csv
with open('text.csv') as file_obj:
    reader = csv.DictReader(file_obj)
    for dictcol in reader:
        print(dictcol['f_name'])