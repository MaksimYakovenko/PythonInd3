import os

PATH1 = r"C:\Users\Admin\PycharmProjects\pythonProject Yakovenko\22\22.03\dir1"
PATH2 = r"C:\Users\Admin\PycharmProjects\pythonProject Yakovenko\22\22.03\dir2"


def same_names(dir1, dir2):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    common = files1.intersection(files2)

    with open(r"C:\Users\Admin\PycharmProjects\pythonProject Yakovenko\22\22.03\03.txt", "w+", encoding="utf-8") as file:
        for item in common:
            filepath1 = os.path.join(dir1, item)
            filepath2 = os.path.join(dir2, item)
            if not (os.path.isfile(filepath1) or os.path.isfile(filepath2)):
                continue
            if os.path.getsize(filepath1) == os.path.getsize(filepath2):
                continue
            else:
                print(print("Різниця між '{}' і '{}' є {} байтів".format(
                    filepath1,
                    filepath2,
                    os.path.getsize(filepath1) - os.path.getsize(filepath2)),
                    file=file))


if __name__ == "__main__":
    same_names(PATH1, PATH2)
