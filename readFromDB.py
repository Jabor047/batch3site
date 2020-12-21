import sqlite3

def readData():
    try:
        conn = sqlite3.connect('batch3.db')
        cursor = conn.cursor()

        sqlFetchQuery = """SELECT * FROM fellows"""
        cursor.execute(sqlFetchQuery)
        record = cursor.fetchall()
        cursor.close()
        global record

    except sqlite3.Error as err:
        print("Failed to fetch from db ", err)
    finally:
        if (conn):
            conn.close()
