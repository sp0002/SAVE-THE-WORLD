import csv
import sqlite3


def import_namelist():
    conn = sqlite3.connect('credit_scores.db')
    c = conn.cursor()
    reader = csv.DictReader(open('Demo_Class_list.csv', 'rt'))
    dict_list = []

    count = 0
    for line in reader:
        count = count + 1
        dict_list.append(line)

    for i in range(count):
        list1 = list(dict_list[i].values())
        sql = "INSERT INTO STUDENTS (Student_Name, Register_Number, Class) VALUES ('%s', '%s', '%s')" % (list1[0], list1[1], list1[2])
        c.execute(sql)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    import_namelist()
