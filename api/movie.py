from ctypes import _NamedFuncPointer
from flask import Flask, request, jsonify
import requests
import sqlite3

app = Flask(_NamedFuncPointer)

# SQLite database setup
conn = sqlite3.connect('favorites.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS favorites (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  overview TEXT)''')
conn.commit()
conn.close()

@app.route('/api/movies/search', methods=['POST'])
def search_movies():
    search_query = request.json.get('searchQuery')
    api_key = 'bd74380ad0f3a6bc2db537543036493a'
    
    # Send a request to the TMDb API to fetch search results
    tmdb_api_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={search_query}'
    response = requests.get(tmdb_api_url)
    data = response.json()
    return jsonify(data['results'])

@app.route('/api/movies/favorite', methods=['POST'])
def favorite_movie():
    movie_data = request.json
    
    # Insert the movie into the SQLite database
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO favorites (title, overview) VALUES (?, ?)', (movie_data['title'], movie_data['overview']))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Movie added to favorites"})

@app.route('/api/movies/favorites', methods=['GET'])
def get_favorite_movies():
    # Fetch and return the user's favorite movies from the database
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM favorites')
    favorites = [{'id': row[0], 'title': row[1], 'overview': row[2]} for row in cursor.fetchall()]
    conn.close()
    
    return jsonify(favorites)

if __name__ == '__main__':
    app.run(debug=True)
