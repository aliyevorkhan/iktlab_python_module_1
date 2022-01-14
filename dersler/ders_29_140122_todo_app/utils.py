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
    cursorObj.execute("CREATE TABLE IF NOT EXISTS todos(id integer PRIMARY KEY, title text, description text, status integer, deadline text)")
    con.commit()
    print("Table yaradilib")

def insert(con, e):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO todos(id, title, description, status, deadline) VALUES(?, ?, ?, ?, ?)', e)
    con.commit()

def select(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM todos')

    rows = cursorObj.fetchall()
    return rows

def select_by_id(con, id):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM todos WHERE id=?', (id,))

    rows = cursorObj.fetchall()
    return rows


def update(con, e):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE todos SET title=?, description=?, status=?, deadline=? where id = ?', e)
    con.commit()


def delete(con, id):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE FROM todos WHERE id=?', (id,))
    con.commit()
