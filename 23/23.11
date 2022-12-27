from openpyxl import *


def personproject(Ename):
    wb = load_workbook(Ename)
    ws = wb['Аркуш1']

    wsnew = wb.create_sheet(title='DataPP')

    t = []
    j = ws.min_column
    for i in range(ws.min_row + 1, ws.max_row + 1):
        c = ws.cell(row=i, column=j)
        t.append(c.value)
    q = []
    dct = {}
    wsnew.append(['Person1  ', 'Person2   ', 'Projects', 'Weight'])

    for e in range(len(t)):
        for k in range(e, len(t)):
            if t[e] == t[k] and e != k:
                p1 = ws.cell(row=ws.min_row + e + 1, column=j + 1).value
                p2 = ws.cell(row=ws.min_row + k + 1, column=j + 1).value
                if (p1, p2) not in dct:
                    dct[(p1, p2)] = [t[e]]
                else:
                    dct[(p1, p2)].append(t[e])
                    # print(dct)
    for key, value in dct.items():
        # print(key,value)
        p1 = key[0]
        p2 = key[1]
        q.append(p1)
        q.append(p2)
        proj = '_'.join(value)
        q.append(proj)
        q.append(len(value))
        wsnew.append(q)
        q = []

    wb.save(Ename)


if __name__ == '__main__':
    a = 'ObjPerson.xlsx'  # input('Name of file: ')
    personproject(a)
