import openpyxl

wb = openpyxl.load_workbook("variant8_input.xlsx")
for ws in wb:
    col = ws.min_column
    r = ws.min_row
    c = ws.cell(row=r, column=col)
    if c.value is None and ws.title == "Лист1":
        continue
    if c.value is None:
        wb.remove(ws)
        print("page is removed")

wb.save("variant8_output.xlsx")

