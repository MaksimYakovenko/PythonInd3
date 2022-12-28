import openpyxl


def create_xlsx(filename, *sheets):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    for title, table in sheets:
        ws = wb.create_sheet(title)
        for row in table:
            ws.append(row)

    wb.save(filename)


if __name__ == '__main__':
    playgrounds = (
        "playgrounds", (
            ("Id", "Name", "Address", "Responsible", "Manager"),
            ("S01", "Рубежанська філія ТТС", "Рубіжне, вул. Шевченка, 22", "Іваненко І.І.", "Костенко К.К."),
            ("S02", "Печеринська філія ТТС", "Печерин, вул. Шкільна, 14", "Петренко П.П.", "Костенко К.К.")
        )
    )
    works = (
        "works", (
            ("Id", "Name"),
            ("W01", "Прокладання кабелю 25 м"),
            ("W02", "Тестування обладнення")
        )
    )
    acts = (
        "acts", (
            ("Id", "No", "Date", "Sum", "S_id"),
            ("A01", 34, "18.07.2016", 17580, "S01"),
            ("A02", 75, "19.07.2016", 23250, "S02")
        )
    )
    items = (
        "items", (
            ("W_id", "A_id"),
            ("W01", "A01"),
            ("W02", "A01")
        )
    )
    create_xlsx("data.xlsx", playgrounds, works, acts, items)
