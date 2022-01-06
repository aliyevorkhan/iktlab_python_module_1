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
    cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    con.commit()

def insert2(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()

def update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    con.commit()

def select1(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def select2(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def delete1(con):
    cursorObj = con.cursor()
    print(cursorObj.execute('DELETE FROM employees').rowcount)

def delete2(con):
    cursorObj = con.cursor()
    print(cursorObj.execute('DELETE FROM employees WHERE salary>800').rowcount)

if __name__ == '__main__':
    con = create_connection()
    #table yarat
    create_table(con)

    # ilk isci melumatlarini insert et insert1 ile
    insert1(con)

    # ikinci isci melumatlarini insert et insert2 ile
    entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
    insert2(con, entities)

    # isci melumatlarini yenile
    update(con)

    # table'daki butun setirleri getir select1 ile
    select1(con)

    # tableda maasi 800den yuxari olan setirleri getir select2 ile
    select2(con)

    # table'dan butun melumatlari sil delete1 ile
    delete1(con)

    # table'dan maasi 800den yuxari olan setirleri sil delete2 ile
    delete2(con)


    con.close()
