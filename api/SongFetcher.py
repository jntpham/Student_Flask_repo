import requests

def fetch_songs_by_artist_genre(artist, genre):
    url = "https://shazam.p.rapidapi.com/charts/list"

    # Set your headers and parameters as required
    headers = {
        "Authorization": "50ed2e0992msh34f550a1d72fefcp1ecc97jsn139df4f8c488"
    }
    params = {
        "artist": artist,
        "genre": genre,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract and process the song data here
        songs = data.get("songs", [])

        # Return the list of songs
        return songs
    else:
        print('Failed to fetch songs. Status code:', response.status_code)
        return None

# Example usage
artist_name = input("Enter the artist's name: ")
genre = input("Enter the genre: ")

songs = fetch_songs_by_artist_genre(artist_name, genre)

if songs:
    print(f"Songs by {artist_name} in the {genre} genre:")
    for song in songs:
        print(f"Title: {song['title']}, Length: {song['length']} seconds")
else:
    print("No songs found.")
