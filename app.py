from flask import Flask, render_template, url_for
from flask_cors import CORS
import base64
import sqlite3
import json

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST', 'GET'])
def index():
    name = 'Gaitho Kevin Karobia'
    img = url_for('static', filename='img/Kevin_Karobia.jpg')
    email = 'gkkarobia@gmail.com'
    desc = "If Pirus and Crips all got along They d probably gun me down by the end of this song Seem like the whole"
    link = 'https://sites.google.com/10academy.org/10-academy-batch-3-kevin'

    data = fetchData()
    for i in range(len(data)):
        data[i] = list(data[i])
        data[i][2] = base64.b64encode(data[i][2]).decode('ascii')

    return render_template('index.html', name=name, image=img, mail=email,
                           description=desc, portLink=link, data=json.dumps(data))

@app.route('/upload', methods=['POST', 'GET'])
def me():
    return render_template()

def fetchData():
    # create a connection to db
    conn = sqlite3.connect('batch3.sqlite')
    cursor = conn.cursor()

    # select all values from the fellows table
    sqlFetchQuery = """SELECT * FROM fellows"""
    cursor.execute(sqlFetchQuery)
    record = cursor.fetchall()
    cursor.close()
    conn.close()
    return record
