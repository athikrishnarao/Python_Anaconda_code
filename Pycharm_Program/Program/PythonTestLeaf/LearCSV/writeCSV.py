import csv

with open ('text.csv',mode ='w',newline="") as fil_obj:
    write = csv.writer(fil_obj)
    head = ["f_name","l_name","email"]
    write.writerow(head)

    data =[["Athi","R","gmail"],["Krish","K","Yahoo"],["Rao","R","outlook"]]
    write.writerows(data)