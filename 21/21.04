import re
import datetime as dat


date1 = r"\b\d{1,2}\.\d{1,2}\.\d{1,4}"
date2 = r"_{2}\._{2}\._{4}"


if __name__ =="__main__":
    f = open("21.04.txt", "r", encoding="utf-8")
    txt = f.read()
    for i in re.finditer(date2, txt):
        print(i.group())
    text2 = re.sub(date1, str(dat.date.today()), txt)
    print(text2)
    f.close()

