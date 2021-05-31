from openpyxl import Workbook
from openpyxl import load_workbook
arquivo_excel = Workbook()
wb = load_workbook('X.xlsx') #document .xlsx
ws = wb['Folha1'] #page 
for line in ws:    
	line[1].value = (str (line[1].value)).replace("+55","").replace("-", "").replace("(","").replace(")","").replace(" ","").replace(".","") #line and what you want remove 

	print (line[1].value)
wb.save(filename = 'Teste.xlsx')

