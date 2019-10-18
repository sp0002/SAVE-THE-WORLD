import sqlite3


def table_create():
    conn = sqlite3.connect('credit_scores.db')
    c = conn.cursor()

    # Create table - STUDENTS
    c.execute('''CREATE TABLE STUDENTS
                     ([Generated_ID] INTEGER PRIMARY KEY,[Student_Name] text, [Register_number] integer, [Class] text)''')

    # Create table - SCORES
    c.execute('''CREATE TABLE SCORES
                     ([Generated_ID] INTEGER PRIMARY KEY,[Register_Number] integer, [Credit_Score] text)''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    table_create()
