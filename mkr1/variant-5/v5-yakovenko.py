#variant 5

def filter_line(f):
    def _filter_line(file):
        with open(file, 'r') as f:
            sym = [",", ":", ";", ".", "-", "!", "?", "/", "\n"]
            l = ""
            for line in f:
                line = line.lower()  # для пониження регістру
                for s in line:
                    for el in sym:
                        if s == el:
                            lst = line.split(el)  # створюємо список, елементами якого є частини рядка, поділені ","
                            line = " ".join(lst)
                l += line
            return l
    return _filter_line


def isSym(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] != word[-1]:
            return False
        else:
            res = isSym(word[1:-1])
            return res
        return s[0] == s[-1] and isSym(s[1:-1])


@filter_line
def read_file(file_name):
    sym_word = []
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                sym_word.append(isSym(word))
        return sym_word


if __name__ == "__main__":
    print(read_file("Text.txt"))
