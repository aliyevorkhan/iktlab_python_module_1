import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def create_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    con.commit()

def insert1(con):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO employees VALUES(2, 'Ali', 888, 'HR', 'Manager', '2017-01-04')")
    con.commit()

def insert2(con, e):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', e)
    con.commit()

def select1(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def select2(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, name FROM employees WHERE salary >= 800.0')

    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def update1(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Ali" where id = 2')
    con.commit()

def update2(con, e):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = ?, salary = ? where id = ?', e)
    con.commit()

    # e = ("Rogers", 1200, "PR", "Manager")
    # cursorObj.execute('UPDATE employees SET name = ?, salary = ?, department = ? , position =?, hireDate=? where id = ?', e)

def delete1(con):
    cursorObj = con.cursor()
    print(cursorObj.execute('DELETE FROM employees').rowcount)
    con.commit()

def delete2(con):
    cursorObj = con.cursor()
    print(cursorObj.execute('DELETE FROM employees WHERE salary>800').rowcount)
    con.commit()

def drop_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP TABLE employees')
    con.commit()

if __name__ == '__main__':
    con = create_connection()
    # create_table(con)
    # insert1(con)
    # entities = (3, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
    # insert2(con, entities)
    select1(con)
    # select2(con)
    # update1(con)
    updated_entities = ("Rogers", 999, 3)
    update2(con, updated_entities)
    # delete2(con)
    # delete1(con)
    # drop_table(con)
