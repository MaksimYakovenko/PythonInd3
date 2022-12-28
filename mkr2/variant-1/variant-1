import re
import os

grn = r"\d+\s?\d+ grn|\d+\s?\d+grn"
dol = r"\$\d+"
r = grn+'|'+dol
lst = [0, 0]
with open('variant-1.txt', 'r', encoding='utf-8') as file:
    txt = file.read()
    x = re.findall(r,txt)
    for match in x:
        if 'grn' in match:
            a = match.split('grn')[0]
            a = a.split(' ')
            a = int(' '.join(a))
            lst[0] += a
        else:
            a = match[1:]
            lst[1] += int(a)
print('This much grn:', lst[0])
print('This much dol:', lst[1])
