import openpyxl


def create_act(acts_no: int, datafile: str):
    wb = openpyxl.load_workbook(datafile)
    ws = wb["acts"]
    for row in ws.rows:
        if row[1].value == acts_no:
            # print(row)
            act_id, act_no, act_sum, act_date, s_id = [c.value for c in row]  # s_id - playground_id
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
    print(works)


if __name__ == '__main__':
    create_act(34, "data.xlsx")