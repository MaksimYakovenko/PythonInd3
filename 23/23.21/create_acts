import openpyxl
from docx import Document
from docx.shared import Pt, Cm


def set_column_width(column, width):
    """Встановлює ширину рядка таблиці."""
    for cell in column.cells:
        cell.width = width


def create_act(acts_no: int, datafile: str):
    wb = openpyxl.load_workbook(datafile)
    ws = wb["acts"]
    for row in ws.rows:
        if row[1].value == acts_no:
            # print(row)
            act_id, no, act_sum, act_date, s_id = [c.value for c in row]  # s_id - playground_id
            # print(act_id, act_no, act_sum, act_date, act_s_id)
            break
    else:
        return

    ws = wb["playgrounds"]
    for row in ws.rows:
        if row[0].value == s_id:
            # print(row)
            s_id, playground_name, address, responsible, manager = [c.value for c in row]
            # print(act_s_id, playgrounds_name, playgrounds_address, responsible, manager)
            break
    else:
        return

    works = {}
    ws = wb["items"]
    for row in ws.rows:
        if row[1].value == act_id:
            work_id, act_id = [c.value for c in row]
            # print(acts_id, works_id)
            works[work_id] = {"work_name": work_id}
    # print(works)

    ws = wb["works"]
    for row in ws.rows:
        if row[0].value in works:
            work_id, work_name = [c.value for c in row]
            works[work_id] = work_name
    # print(works)

    # Стоворюємо документ у Word
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"  # Тип шрифту
    style.font.size = Pt(14)
    paragraph = doc.add_paragraph(f"«")
    paragraph.alignment = 0
    # Додаємо номер акту та дату.
    table = doc.add_table(1, 2)
    row = table.rows[0]
    paragraph = row.cells[0].add_paragraph(f"Рахунок № {acts_no}")
    paragraph.alignment = 0
    paragraph = row.cells[1].add_paragraph(f"Дата {act_sum}")
    paragraph.alignment = 2
    # Додаємо ім`я Виконавця та його адресу.
    doc.add_paragraph(f"Даний акт засвідчує, що Виконавцем на майданчику {manager} за адресою {address} були виконані "
                      f"такі роботи:")
    headers = ("№", "Назва роботи")
    # Створюємо таблицю замовлень.
    table = doc.add_table(1, len(headers), "Table Grid")
    row = table.rows[0]
    for cell, header in zip(row.cells, headers):
        cell.text = header

    for i in enumerate(works.values(), 1):

        values = (
            i
        )
        # Додаємо рядки до таблиці
        row = table.add_row()
        for cell, value in zip(row.cells, values):
            cell.text = str(value)

    # Встановлюємо розміри клітинок таблиці
    widths = (Cm(1.0), Cm(10.0))
    for column, width in zip(table.columns, widths):
        set_column_width(column, width)

    # Додаємо розрахунок суми кількості виконаних робіт.
    doc.add_paragraph(f"Сума виконаних робіт складає {act_date} грн.")

    # Додаємо ім`я Замовника та ім`я Виконавця.
    table = doc.add_table(1, 2)
    row = table.rows[0]
    paragraph = row.cells[0].add_paragraph(f"Від Замовника \n \n {responsible}")
    paragraph.alignment = 0
    paragraph = row.cells[1].add_paragraph(f"Від Виконавця \n \n {manager}")
    paragraph.alignment = 2

    paragraph = doc.add_paragraph("»")
    paragraph.alignment = 0
    # Зберігаємо наш документ.
    doc.save(f"acts.docx")


if __name__ == '__main__':
    create_act(34, "data.xlsx")
