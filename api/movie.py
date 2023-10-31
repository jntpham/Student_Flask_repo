from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Make an HTTP GET request to the TMDb API
    api_key = 'bd74380ad0f3a6bc2db537543036493a'  # Replace with your TMDb API key
    url = f'https://api.themoviedb.org/3/movie/550?api_key={api_key}'

    try:
        response = requests.get(url)
        data = response.json()
        movies = data.get('movies', [])  # Assuming the movie data is in a 'movies' key
    except requests.exceptions.RequestException as e:
        print('Error fetching movie data:', e)
        movies = []

    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
