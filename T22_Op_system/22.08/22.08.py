import datetime
import os
import os.path as path
import sys
import time
import re


def contents_of_the_folder(folder, filename="output_22_08_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".txt"):
    newout = open(filename, "w", encoding="utf-8")
    oldout = sys.stdout
    sys.stdout = newout
    print(folder, "", datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            print(root, " dir ", dir, "", time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(path.getmtime(path.join(root, dir)))))
        for file in files:
            print(root, " file ", file, "", time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(path.getmtime(path.join(root, file)))))
    sys.stdout = oldout
    newout.close()


def compare(file1, file2):
    newout = open("output_22_08_final.txt", "w", encoding="utf-8")
    oldout = sys.stdout
    sys.stdout = newout
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    if datetime.datetime(*[int(el) for el in re.split("_", file2[-23:-4])]) < datetime.datetime(*[int(el) for el in re.split("_", file1[-23:-4])]):
        f1, f2 = f2, f1
    c1 = f1.readlines()
    c2 = f2.readlines()
    fs1 = [el.split("  ")[:-1] for el in c1[1:]]
    fs2 = [el.split("  ")[:-1] for el in c2[1:]]
    t1 = [el.split("  ")[-1] for el in c1[1:]]
    t2 = [el.split("  ")[-1] for el in c2[1:]]
    if c1 == c2:
        print()
    else:
        print(f"Зміни, які відбулися в {c1[0].split('  ')[0]} з {c1[0].split('  ')[1][:-1]} по {c2[0].split('  ')[1][:-1]}:")
        for el in fs1:
            if el not in fs2:
                if el[1] == "dir":
                    print(f"Видалено папку {el[2]} за адресою {el[0]}")
                else:
                    print(f"Видалено файл {el[2]} за адресою {el[0]}")
            else:
                if t1[fs1.index(el)] != t2[fs2.index(el)]:
                    if el[1] == "dir":
                        print(f"Змінено папку {el[2]} за адресою {el[0]}, час зміни: {t2[fs2.index(el)][:-1]}")
                    else:
                        print(f"Змінено файл {el[2]} за адресою {el[0]}, час зміни: {t2[fs2.index(el)][:-1]}")
        for el in fs2:
            if el not in fs1:
                if el[1] == "dir":
                    print(f"Створено папку {el[2]} за адресою {el[0]}")
                else:
                    print(f"Створено файл {el[2]} за адресою {el[0]}")
    f1.close()
    f2.close()
    sys.stdout = oldout
    newout.close()


if __name__ == "__main__":
    compare("output_22_08_2022_12_03_15_35_49.txt", "output_22_08_2022_12_03_15_39_35.txt")
    # contents_of_the_folder(r"C:\Users\Admin\PycharmProjects\pythonProject Yakovenko\22\22.08")


