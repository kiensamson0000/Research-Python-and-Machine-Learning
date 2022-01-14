path = "database_sach.txt"

def luu_file(line):
    try:
        file = open(path, 'a', encoding="UTF-8")
        file.writelines(line)
        file.writelines("\n")
        file.close()
    except:
        pass


def doc_file():
    arr_sach = []
    try:
        file = open(path, 'r', encoding="UTF-8")
        for line in file:
            data = line.strip().split(";")
            arr_sach.append(data)
        file.close()
    except:
        pass
    return arr_sach