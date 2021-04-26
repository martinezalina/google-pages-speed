import sqlite3
from sqlite3 import Error
from datetime import datetime


def sql_connection():
    try:
        con = sqlite3.connect('results/database.db')
        return con
    except Error:
        print(Error)

def sql_create_table_metrics(con):
    cursorObj = con.cursor()
    cursorObj.execute('CREATE TABLE metrics(id integer PRIMARY KEY, url text, score real, time datetime)')
    con.commit()

def sql_insert_metric(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO metrics(url, score, time) VALUES(?, ?, ?)', entities)
    con.commit()

def sql_read_metrics(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM metrics')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    con.commit()

def db_init():
    con = sql_connection()
    try:
        sql_create_table_metrics(con)
    except:
        print('db already created')
    return con