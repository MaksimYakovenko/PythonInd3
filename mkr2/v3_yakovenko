from os import listdir
from os.path import isfile, join

path = ''
files = [f for f in listdir(path) if isfile(join(path, f))]

names = {}

for f in files:
    file_name = f.split('.')[0]
    number = file_name[-3]
    names[int(number)] = f

result = ''
for key in sorted(names):
    f_path = names[key]
    with open(f_path) as f:
        contents = f.read()
        result += contents

with open('file.txt', 'w+') as f:
    f.write(result)
