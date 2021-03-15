# Way1
file_obj=open('text1.txt',mode='w')
file_obj.write("In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources")
file_obj.close()

#Way2
with open('text2.txt',mode='w') as file:
    file.write("In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources")

