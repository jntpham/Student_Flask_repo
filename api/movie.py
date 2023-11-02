from flask_cors import CORS
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'movies.db'


@app.route('/favorites', methods=['POST'])
def add_favorite():
    movie_data = request.get_json()
    title = movie_data.get('title')
    release_date = movie_data.get('release_date')
    rating = movie_data.get('rating')

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO favorites (title, release_date, rating) VALUES (?, ?, ?)", (title, release_date, rating))
        conn.commit()

    return jsonify({"message": "Movie added to favorites successfully!"})


@app.route('/favorites', methods=['GET'])
def get_favorites():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, release_date, rating FROM favorites")
        movies = cursor.fetchall()

    return jsonify(movies)


if __name__ == '__main__':
    app.run(debug=True)
CORS(app)
