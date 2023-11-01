import requests

# Replace your existing '/api/movies/filter' route code
@app.route('/api/movies/filter', methods=['POST'])
def filter_movies():
    data = request.get_json()
    lead_actor = data.get('leadActor')
    genre = data.get('genre')

    # Construct the API URL with the provided lead actor and genre
    api_url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&query={lead_actor}'

    # Make a request to the API to get the actor's ID
    actor_response = requests.get(api_url)
    actor_data = actor_response.json()

    # Check if the API request was successful and if there are results
    if 'results' in actor_data and actor_data['results']:
        actor_id = actor_data['results'][0]['id']

        # Construct the API URL to fetch the actor's movie credits
        movie_credits_url = f'https://api.themoviedb.org/3/person/{actor_id}/movie_credits?api_key={api_key}'

        # Make a request to get the actor's movie credits
        movie_credits_response = requests.get(movie_credits_url)
        movie_data = movie_credits_response.json()

        # Extract and format the movie data as needed
        filtered_movies = []
        for movie in movie_data.get('cast', []):
            if not genre or genre == 'any' or genre in [str(g['id']) for g in movie.get('genre_ids', [])]:
                movie_info = {
                    'title': movie.get('title'),
                    'release_date': movie.get('release_date'),
                    'vote_average': movie.get('vote_average'),
                }
                filtered_movies.append(movie_info)

        return jsonify(filtered_movies)
    else:
        return jsonify([])  # Return an empty list if no results were found for the actor

# Replace your existing '/api/movies/random' route code
@app.route('/api/movies/random', methods=['GET'])
def get_random_movie():
    # Generate a random actor's name (for demonstration purposes)
    random_actor_names = ['Tom Hanks', 'Brad Pitt', 'Meryl Streep', 'Leonardo DiCaprio']
    random_actor_name = random.choice(random_actor_names)

    # Construct the API URL to fetch a random movie using the provided actor name
    api_url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&query={random_actor_name}'

    # Make a request to the API to get the actor's ID
    actor_response = requests.get(api_url)
    actor_data = actor_response.json()

    if 'results' in actor_data and actor_data['results']:
        actor_id = actor_data['results'][0]['id']

        # Construct the API URL to fetch the actor's movie credits
        movie_credits_url = f'https://api.themoviedb.org/3/person/{actor_id}/movie_credits?api_key={api_key}'

        # Make a request to get the actor's movie credits
        movie_credits_response = requests.get(movie_credits_url)
        movie_data = movie_credits_response.json()

        # Extract and format a random movie
        movies = movie_data.get('cast', [])
        if movies:
            random_movie = random.choice(movies)
            movie_info = {
                'title': random_movie.get('title'),
                'release_date': random_movie.get('release_date'),
                'vote_average': random_movie.get('vote_average'),
            }
            return jsonify(movie_info)
    
    return jsonify({'title': 'Random Movie Title'})

# Be sure to import 'requests' and 'random' at the top of your script
import requests
import random
