def typ(typ):
    def type_cheacker(fun):
        def _type_cheaker(*args):
            for i in args:
                if type(i) == typ:
                    continue
                else:
                    raise TypeError('Число не підходить під заданий тип данних')
            return fun(*args)
        return _type_cheaker
    return type_cheacker
@typ(int)
def func(a, b, c):
    print((a + b + c) / 3)
func(1, 3, 5)
try:
    def funcc(a, b, c):
        print(( a + b + c ) / 3 )
except Exception as e:
    funcc(True, '2', 1)





