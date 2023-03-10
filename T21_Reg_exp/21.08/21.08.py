import re

SENTENCE = r"\d*\.\d+|\d{1,}\."
point = r"(?=\s[A-ZА-ЯІЇЄҐ])"
NUMS = SENTENCE + "|" + point


def _change_numbers(match):
    num = match.group()
    if num.startswith("."):
        return "0" + num
    elif num.endswith("."):
        return num + "0" + "."
    else:
        return num


def change_numbers(string):
    print(re.sub(NUMS, _change_numbers, string))


if __name__ == '__main__':
    with open("21.08_input.txt", "r", encoding="utf-8") as inp:
        for line in inp.readlines():
            change_numbers(line.strip())





