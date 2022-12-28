def matdec(f):
    def _matdec(arg1, arg2):
        res = f(arg1, arg2)
        leng = 0
        dec = {}
        cn = 0
        for index1, lst in enumerate(res):
            leng += len(lst)
            for index2, i in enumerate(lst):
                if i != 0:
                    cn += 1
                    dec[(index1, index2)] = i
        if cn < 0.1 * leng:
            return dec
        return res
    return _matdec


@matdec
def matrix_add(lst1, lst2):
    lst_res = []
    for index, lst_x in enumerate(lst1):
        lst_app = []
        lst_y = lst2[index]
        ln = len(lst_x)
        lst_new = [0] * ln
        for i in range(ln):
            lst_new = lst_x[i] + lst_y[i]
            lst_app.append(lst_new)
        lst_res.append(lst_app)
    return lst_res


print(matrix_add([[1, 2, 3], [1, 2, 3]], [[4, 5, 6], [4, 5, 6]]))
print(matrix_add([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 6], [0, 0, 0], [0, 0, 0]]))