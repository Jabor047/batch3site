from flask import url_for
import pandas as pd
import sqlite3
import os

def convertToBinaryData(filename):
    # path = os.getcwd() + filename
    with open(filename, 'rb') as file:
        binData = file.read()
    return binData

def insertData(name, img, email, desc, link):
    try:
        sqliteConn = sqlite3.connect('batch3.sqlite')
        cursor = sqliteConn.cursor()
        print('Connected to DataBase')

        # check if table exists create it if doesn't
        createTableQuery = """ CREATE TABLE IF NOT EXISTS fellows
                               (id INTEGER PRIMARY KEY, name TEXT NOT NULL, img BLOB NOT NULL,
                               email TEXT NOT NULL, desc TEXT NOT NULL, link TEXT NOT NULL)"""
        cursor.execute(createTableQuery)

        sqliteInsertQuery = """ INSERT INTO fellows (name, img, email, desc, link) VALUES (?, ?, ?, ?, ?) """
        photo = convertToBinaryData(img)

        dataTuple = (name, photo, email, desc, link)
        cursor.execute(sqliteInsertQuery, dataTuple)
        sqliteConn.commit()
        print(f'Data belonging to {name} has been uploaded')
        cursor.close()
    except sqlite3.Error as err:
        print(" Failed to insert data to table", err)
    finally:
        if (sqliteConn):
            sqliteConn.close()

def loadinfo(csvfile):
    df = pd.read_csv(csvfile)
    df.dropna(inplace=True)
    df.reset_index(inplace=True)

    for i in range(df.shape[0]):
        name = df['Name'][i]
        email = df['Email'][i]
        link = df['Profile Link'][i]
        desc = df['Two-line description'][i]

        photoname = name.split()[0] + '.jpg'
        photopath = os.getcwd() + '/static/img/' + photoname

        insertData(name, photopath, email, desc, link)

if __name__ == '__main__':
    loadinfo('10 Academy Profiles.csv')
