import requests

def fetch_songs_by_artist_genre(artist, genre):
    url = "https://shazam.p.rapidapi.com/artists/get-top-songs"

    querystring = {"id":"567072","l":"en-US"}

    headers = {
        "X-RapidAPI-Key": "50ed2e0992msh34f550a1d72fefcp1ecc97jsn139df4f8c488",
	    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    params = {
        "artist": artist,
        "genre": genre,
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            songs = data.get("tracks", {}).get("hits", [])

            return songs
        else:
            print('Failed to fetch songs. Status code:', response.status_code)
            return None
    except Exception as e:
        print('An error occurred:', str(e))
        return None

# Example usage
artist_name = input("Enter the artist's name: ")
genre = input("Enter the genre: ")

songs = fetch_songs_by_artist_genre(artist_name, genre)

if songs:
    print(f"Songs by {artist_name} in the {genre} genre:")
    for song in songs:
        print(f"Title: {song.get('track', {}).get('title', 'N/A')}, Length: {song.get('track', {}).get('duration', 'N/A')} seconds")
else:
    print("No songs found.")

