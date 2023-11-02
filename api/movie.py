from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = './api/movies.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    if request.method == 'GET':
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM favorites")
        movies = cursor.fetchall()
        conn.close()
        return jsonify(movies), 200

    elif request.method == 'POST':
        data = request.get_json()
        title = data['title']
        release_date = data['release_date']
        rating = data['rating']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO favorites (title, release_date, rating) VALUES (?, ?, ?)", (title, release_date, rating))
        conn.commit()
        conn.close()

        return jsonify({"message": "Movie added to favorites"}), 201

if __name__ == '__main__':
    app.run(debug=True)
