from flask import Flask, request, jsonify
import requests
import sqlite3

app = Flask(__name)

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
    actor_query = request.json.get('actorQuery')
    api_key = 'bd74380ad0f3a6bc2db537543036493a'
    
    # Send a request to the TMDb API to fetch movies by actor
    tmdb_api_url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&query={actor_query}'
    response = requests.get(tmdb_api_url)
    data = response.json()
    
    # Extract movie data from the response
    movies = []
    for person in data['results']:
        for known_for in person.get('known_for', []):
            if known_for['media_type'] == 'movie':
                movies.append(known_for)
    
    return jsonify(movies)

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
