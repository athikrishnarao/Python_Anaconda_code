# Step 1: Install sqlite3 : pip install db-sqlite3

import sqlite3

# Create Connection
con = sqlite3.connect('database.db')
print('Create DB')

# Create Table in DataBase
con.execute('CREATE TABLE IF NOT EXISTS leaf_db(fName,lName,email,password)')
print('Table Created')

# Insert the Data
con.execute('''INSERT INTO leaf_db(fname,lname,email,password) VALUES ('ATHI','Krish','gmail','1234')''')
con.commit()  # For update the database
print("Inserted")

# Update the Database
con.execute('''UPDATE leaf_db set password = '1234587980' WHERE fName='ATHI' ''')
con.commit()
print('Update the Records')

# Read the database
data = con.execute('SELECT * FROM leaf_db')
print(data)
for i in data:
    print(i)

# Close the Connection of the Database
con.close()
print('Close Database')
