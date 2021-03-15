import openpyxl

# Create the object for workbook
wb = openpyxl.Workbook()

# Grap the active sheet
sh = wb.active

# Change the Sheet name or set the sheet name
sh.title = "Validation"
sh['A1']="fName"
sh['B1']="lName"
sh['C1']="email"

sh['A2']="Athi"
sh['B2']="Krish"
sh['C2']="Gamil"

wb.save('Testing1.xlsx')