import sqlite3
import os

def convertToBinaryData(filename):
    # path = os.getcwd() + filename
    with open(filename, 'rb') as file:
        binData = file.read()
    return binData

def insertData(fellowID, name, img, email, desc, link):
    try:
        sqliteConn = sqlite3.connect('batch3.sqlite')
        cursor = sqliteConn.cursor()
        print('Connected to DataBase')

        # check if table exists create it if doesn't
        createTableQuery = """ CREATE TABLE IF NOT EXISTS fellows
                               (id INTEGER PRIMARY KEY, name TEXT NOT NULL, img BLOB NOT NULL,
                               email TEXT NOT NULL, desc TEXT NOT NULL, link TEXT NOT NULL)"""
        cursor.execute(createTableQuery)

        sqliteInsertQuery = """ INSERT INTO fellows (id, name, img, email, desc, link) VALUES (?, ?, ?, ?, ?, ?) """
        photo = convertToBinaryData(img)

        dataTuple = (fellowID, name, photo, email, desc, link)
        cursor.execute(sqliteInsertQuery, dataTuple)
        sqliteConn.commit()
        print(f'Data belonging to {name} has been uploaded')
        cursor.close()
    except sqlite3.Error as err:
        print(" Failed to insert data to table", err)
    finally:
        if (sqliteConn):
            sqliteConn.close()

fellowID = 1925
name = 'Thomas Shelby'
img = "/mnt/e/projects/batch3site/static/img/tommy.jpg"
email = 'gkkarobia@gmail.com'
desc = "Everyone's a whore, Grace. We just sell different parts of ourselves."
link = 'https://sites.google.com/10academy.org/10-academy-batch-3-kevin'

insertData(fellowID, name, img, email, desc, link)
