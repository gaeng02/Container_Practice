from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("data.db")

cur = con.cursor()
cur.execute('CREATE TABLE Favorites(Name TEXT, URL TEXT)')
cur.executemany(
    'INSERT INTO Favorites VALUES (?, ?)',
    [('Github', 'https://github.com/gaeng02'),
    ('Dockerhub', 'https://hub.docker.com/repositories/gaeng02'),
    ('BaekJoon', 'https://www.acmicpc.net/user/gaeng_02')
    ]
)
con.commit()
con.close()


@app.route('/get_data', methods=['GET'])
def get_data() :
    
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Favorites')
    data = cur.fetchall()
    con.close()

    return jsonify(data)


if (__name__ == '__main__') : 
    app.run(host="0.0.0.0", port=5001)
