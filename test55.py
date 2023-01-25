# 列と行の操作 #
from openpyxl import load_workbook
wb = load_workbook(filename='output.xlsx')
sheet_name = wb.shettnames[0]
ws1 = wb[sheet_name]
ws1.insert_cols(2, 3)
wb.save('output.xlsx')
