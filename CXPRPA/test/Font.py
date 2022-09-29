from openpyxl import load_workbook
from openpyxl.styles import Font, colors, Alignment

excel_address = r"测试.xlsx"
wb = load_workbook(excel_address)
sht = wb.get_sheet_by_name("Sheet_test")

sht["A1"] = "测试"
font_set = Font(name='Arial', size=24, italic=True, color=colors.BLUE, bold=True, underline='doubleAccounting')
sht['A1'].font = font_set


sht["A5"] = "测试"
sht['A5'].alignment = Alignment(horizontal='center', vertical='center')

sht["A6"] = "测试"
sht['A6'].alignment = Alignment(horizontal='left', vertical='bottom')

sht["A7"] = "测试"
sht['A7'].alignment = Alignment(horizontal='right', vertical='top')


sht["A9"] = "测试测试测试测试测试测试"
sht['A9'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)

sht["A10"] = "测试测试测试测试测试测试"
sht['A10'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=False)

wb.save(excel_address)