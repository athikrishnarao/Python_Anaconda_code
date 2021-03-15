with open('Nayanthara.txt') as file_obj:
    values = file_obj.read()
    dict1={}
    for i in values.split():
        if i in dict1:
            dict1[i]=dict1[i]+1
        else:
            dict1[i]=1
print(dict1)

