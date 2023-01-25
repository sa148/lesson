# 既存のファイル読み込み #
from openpyxl import load_workbook
wb = load_workbook(filename='output.xlsx')
sheet_names = wb.sheetnames
print(sheet_names)