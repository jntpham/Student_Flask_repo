from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name)

# Initialize the SQLite database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create the movies table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    )
''')
conn.commit()

@app.route('/api/movies/filter', methods=['POST'])
def filter_movies():
    data = request.get_json()
    lead_actor = data.get('leadActor')
    genre = data.get('genre')
    
    # Use the provided API endpoint to fetch movie data
    api_url = f'https://api.themoviedb.org/3/movie/550?api_key=bd74380ad0f3a6bc2db537543036493a'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        movie_data = response.json()
        # Implement your movie filtering logic here
        # Return a list of filtered movies in JSON format
        filtered_movies = [...]  # Replace with your filtered movie data
        return jsonify(filtered_movies)
    else:
        return jsonify({'error': 'Failed to fetch movie data'})

@app.route('/api/movies/favorite', methods=['POST'])
def favorite_movie():
    data = request.get_json()
    title = data.get('title')

    # Store the favorited movie in the database
    cursor.execute('INSERT INTO movies (title) VALUES (?)', (title,))
    conn.commit()

    return jsonify({'message': 'Movie favorited successfully'})

@app.route('/api/movies/favorites', methods=['GET'])
def get_favorite_movies():
    # Retrieve the list of favorited movies from the database
    cursor.execute('SELECT title FROM movies')
    favorites = [row[0] for row in cursor.fetchall()]
    return jsonify(favorites)

@app.route('/api/movies/random', methods=['GET'])
def get_random_movie():
    # Use the provided API endpoint to fetch a random movie
    api_url = 'https://api.themoviedb.org/3/movie/550?api_key=bd74380ad0f3a6bc2db537543036493a'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        random_movie_data = response.json()
        return jsonify(random_movie_data)
    else:
        return jsonify({'error': 'Failed to fetch random movie data'})

if __name__ == '__main__':
    app.run(debug=True)
