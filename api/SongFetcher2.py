from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name)

def search_songs_by_artist_genre(artist, genre):
    # Your existing code for making the API request
    # ...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    artist_name = request.form['artist_name']
    genre = request.form['genre']

    songs = search_songs_by_artist_genre(artist_name, genre)

    if songs:
        return jsonify(songs)
    else:
        return jsonify({"error": "No songs found"})

if __name__ == "__main__":
    app.run(debug=True)
